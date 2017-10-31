from flask import Flask, render_template, request
from flask.ext.sqlalchemy import SQLAlchemy
import os
import pandas as pd
from sqlalchemy import create_engine
from recommend import best_college, get_info, append_values
import json

app = Flask(__name__)

app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
engine = create_engine(os.environ['DATABASE_URL'])
df = pd.read_sql_query('select * from "pandas_db"', con =engine)

@app.route('/')
def index():
    '''Render html page'''
    return render_template("index2.html")

@app.route('/importance', methods= ['POST'])
def importance():
    '''Render importance page'''
    ethnicity = str(request.form['ethnicity'])
    demographic = [str(request.form['ethnicity']), str(request.form['fam_inc']), str(request.form['dependence'])]
    return render_template("index.html", ethnicity=ethnicity)

# @app.route('/importance')
# def predict():
#     demographic = [str(request.form['ethnicity']), str(request.form['fam_inc']), str(request.form['dependence'])]
#     return render_template("index.html")

@app.route('/predict', methods=['GET','POST'])
def predict():
    return str(request.form['ethnicity'])
    # return render_template("index.html")
    '''Return results'''
    # json_url = os
    # json.load()
    # return json.load(demo
    # d = {1:'Public',2:'Private nonprofit',3:'Private for-profit'}
    # info_list = get_info(int(request.form['tuition']),str(request.form['first']),str(request.form['second']),str(request.form['third']),str(request.form['fourth']))
    # results  = best_college(df,info_list)
    # School = results['INSTNM'].values
    # State = results['STABBR'].values
    # Control = results['CONTROL'].replace(d).values
    # return render_template("table.html",school = School, state = State, control = Control)
if __name__ == '__main__':
    app.run(debug=True)
