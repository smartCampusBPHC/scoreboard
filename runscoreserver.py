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

#Hardcore declaration of array with intial state given
w, h = 6 ,5 
Matrix = [[0 for x in range(w)] for y in range(h)]
#Sports Names
Matrix[0][0] = 'Cricket'
Matrix[0][1] = 'Football'
Matrix[0][2] = 'Badminton(B)'
Matrix[0][3] = 'Badminton(G)'
Matrix[0][4] = 'Table Tennis(B)'
Matrix[0][5] = 'Table Tennis(G)'
#Status of Game
Matrix[1][0] = 'Yet To Start'
Matrix[1][1] = 'Yet To Start'
Matrix[1][2] = 'Yet To Start'
Matrix[1][3] = 'Yet To Start'
Matrix[1][4] = 'Yet To Start'
Matrix[1][5] = 'Ongoing'
#Team 1
Matrix[2][0] = 'BPHC'
Matrix[2][1] = 'BPHC'
Matrix[2][2] = 'BPHC'
Matrix[2][3] = 'BPHC'
Matrix[2][4] = 'BPHC'
Matrix[2][5] = 'BPHC'
#Team 2
Matrix[3][0] = 'BPHC' 
Matrix[3][1] = 'BPHC'
Matrix[3][2] = 'BPHC'
Matrix[3][3] = 'BPHC'
Matrix[3][4] = 'BPHC'
Matrix[3][5] = 'BPHC'

#Score String 

Matrix[4][0] = '245/3(20) and 112/3(12)'
Matrix[4][1] = '3-2'
Matrix[4][2] = '21-16, 12-1'
Matrix[4][3] = '21-11, 21-3'
Matrix[4][4] = '12-1,12-6,12-2'
Matrix[4][5] = '12-1,12-6,12-2'




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
def main_updater():
	if request.method == 'POST':
		d = request.method['selected_element']
		

    return render_template('score_updater.html', params = Matrix)


@app.route('/tvscreen', methods=['GET', 'POST'])
def screen_tv_show():
    return render_template('screen_tv.html')

@app.route('/updater', methods=['GET','POST'])
def main_xx():
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
