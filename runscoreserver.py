import os
import flask
import time
import datetime
import csv
import requests
from collections import deque

from tempfile import NamedTemporaryFile
import shutil

from flask import Flask,request ,render_template

app=Flask(__name__)



@app.route('/', methods=['GET', 'POST'])
def front():
    return render_template('screen_web.html')


@app.route('/tvscreen', methods=['GET', 'POST'])
def screen_tv_show():
    return render_template('screen_tv.html')

@app.route('/updater', methods=['GET','POST'])
def main_updater():
    
    pass


def edit_live(Sports,MatchNumber,Gender,Team1,Team2,Score,Status):
    with open('diopter.csv','rb') as fread:
        with open('diopter.csv','wb') as fwrite:
            reader = csv.reader(fread) #open csv

            next(reader,None)
            for row in reader:
                if row[1] == Sports:


    pass

def edit_complete_list(Sports,MatchNumber,Gender,Team1,Team2,Score,Status):
    
    pass


# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     error = None
#     if request.method == 'POST':
#         if request.form['username'] != app.config['USERNAME']:
#             error = 'Invalid username'
#         elif request.form['password'] != app.config['PASSWORD']:
#             error = 'Invalid password'
#         else:
#             session['logged_in'] = True
#             flash('You were logged in')
#             return redirect(url_for('football'))
#     return render_template('login.html', error=error)# n=150

# @app.route('/football',methods=['GET','POST'])
# def football():
#     return redirect(url_for('football'))





if __name__=='__main__':
	# try:
	# 	thread.start_new_thread(sendToServer , (10,))
	# except:
	# 	print "Error: unable to start thread"

	app.debug=True
	app.run(host='0.0.0.0',port=8060)
