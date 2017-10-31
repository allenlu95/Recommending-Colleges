import pandas as pd
# from sklearn.preprocessing import StandardScaler, normalize
import numpy as np
import matplotlib.pyplot as plt
plt.scatter([1,2,3,4],[3816,1594,399,20])
plt.xlabel('Cut off number')
plt.ylabel('Amount of Data')
plt.show()
# #Combine out of state with in-state completion rate
# def create_completion(df):
#     df['C150_4'].fillna(df['C150_L4'], inplace=True)
#     del df['C150_L4']
#     df['Tuition'] = df['TUITIONFEE_IN'].fillna(df['TUITIONFEE_PROG'])
#     return df

#TODO differentiation between In state and Out of state
#demographic
def best_college(df, information):
    # if demographic[0] == 'White':
    #     df['C150_4'] = df['C150_4_WHITE']
    # elif demographic[0] == 'Black':
    #     df['C150_4'] = df['C150_4_BLACK']
    # elif demographic[0] == 'Hispanic':
    #     df['C150_4'] = df['C150_4_HISP']
    # elif demographic[0] == 'Asian':
    #     df['C150_4'] = df['C150_4_ASIAN']
    # if demographic[1] == 'Below $30,000':
    #     df['MD_EARN_WNE_P10'] = df['MN_EARN_WNE_INC1_P10']
    # elif demographic[1] == 'Between $30,000 and $75,000':
    #     df['MD_EARN_WNE_P10'] = df['MN_EARN_WNE_INC2_P10']
    # else:
    #     df['MD_EARN_WNE_P10'] = df['MN_EARN_WNE_INC3_P10']
    # if demographic[2] == 'Dependent':
    #     df['DEBT_MDN_SUPP'] = df['FIRSTGEN_DEBT_MDN']
    # else:
    #     df['DEBT_MDN_SUPP'] = df['IND_DEBT_MDN']

    starting_dict = {0:'MD_EARN_WNE_P10', 1:'C150_4', 2:'DEBT_MDN_SUPP', 3:'LOAN_EVER'}
    df = df.dropna(axis=0,subset=['C150_4','DEBT_MDN_SUPP', 'Tuition'])
    df = df[df['Tuition'] < information[4]]
    df['DEBT_MDN_SUPP'] = -1*df.loc[:,'DEBT_MDN_SUPP']
    df['LOAN_EVER'] = -1*df.loc[:,'LOAN_EVER']
    # need to set some bounds
    limit = 1
    for index in np.argsort(information[:-1])[::-1]:
        restriction_rate = int(round(df.shape[0]*limit))
        df = df.sort_values(by=starting_dict[index],ascending = False).iloc[:restriction_rate]
        # limit -=.2
        final = index
    return df.sort_values(by = starting_dict[final],ascending = False).head()
def append_values(request1, request2, request3, request4, value):
    if request1 == value:
        return 1
    elif request2 == value:
        return 2
    elif request3 == value:
        return 3
    elif request4 == value:
        return 4

def get_info(tuition, request1, request2, request3, request4):
    return_list = []
    return_list.append(append_values(request1,request2,request3,request4, 'Future Earnings'))
    return_list.append(append_values(request1,request2,request3,request4, 'Completion rate'))
    return_list.append(append_values(request1,request2,request3,request4, 'Future Debt'))
    return_list.append(append_values(request1,request2,request3,request4, 'Loan Access'))
    return_list.append(tuition)
    return return_list


if __name__ == '__main__':
    # int(round(df.shape[0]*.7))
    # round(.7/2)
    # 3490*.4
    # 1396*.1
    # .5**4
    # .7-.25-.25
#In terms of Earnings, Completion, Debt, Loan
    information1 = [1,2,3,4,100000]
    # demographic = ['White','Between $30,000 and $75,000','Dependent']
    # information2 = [2,4,3,1, 100000]
    # information3 = [3,4,2,1,100000]
    # information4 = [4,3,2,1,100000]

    # df = create_completion(df)
    recommend_college1 =  best_college(df,information1)[['INSTNM','MD_EARN_WNE_P10']]
    print df.sort_values(by = 'MD_EARN_WNE_P10', ascending =False)[['INSTNM', 'MD_EARN_WNE_P10']]
    # recommend_college2 = best_college(df,information2)
    # recommend_college3 =  best_college(df,information3)
    # recommend_college4 = best_college(df,information4)
    print recommend_college1
    # print recommend_college1['MD_EARN_WNE_P10']
    # print recommend_college2['MD_EARN_WNE_P10']
    # print recommend_college3['MD_EARN_WNE_P10']
    # print recommend_college4['MD_EARN_WNE_P10']
