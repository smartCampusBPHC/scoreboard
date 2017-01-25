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
from numpy import genfromtxt

app=Flask(__name__)


#live_scores = genfromtxt('my_file.csv', delimiter=',')

dict = {'Sports':'-1' ,'MatchNumber':'-1','Gender':'M','Team1':'BPHC','Team2':'-1','Score':'-1','Status':'-1'}
# def edit_live(Sports,MatchNumber,Gender,Team1,Team2,Score,Status):
#     with open('diopter.csv','rb') as fread:
#         with open('diopter.csv','wb') as fwrite:
#             reader = csv.reader(fread) #open csv

            # next(reader,None)
            # for row in reader:
            #     if row[1] == Sports:


#Supposed to give out a list of all 
# def edit_complete_list(Sports,MatchNumber,Gender,Team1,Team2,Score,Status):
    
#     pass




@app.route('/', methods=['GET', 'POST'])
def front():
    return render_template('score_updater.html')


@app.route('/tvscreen', methods=['GET', 'POST'])
def screen_tv_show():
    return render_template('screen_tv.html')

@app.route('/updater', methods=['GET','POST'])
def main_updater():
    return 0

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
