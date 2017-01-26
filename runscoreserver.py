import os
import flask
import time
import datetime
import csv
import requests
from collections import deque
from tempfile import NamedTemporaryFile
import shutil
from flask import Flask,request ,render_template, redirect, url_for
from numpy import genfromtxt

app=Flask(__name__)

#Hardcore declaration of array with intial state given
w, h = 6 ,6 
Matrix = [[0 for x in range(w)] for y in range(h)]
#Sports Names
Matrix[0][0] = 'Cricket'
Matrix[1][0] = 'Football'
Matrix[2][0] = 'Badminton(B)'
Matrix[3][0] = 'Badminton(G)'
Matrix[4][0] = 'Table Tennis(B)'
Matrix[5][0] = 'Table Tennis(G)'
#Status of Game
Matrix[0][1] = 'Yet To Start'
Matrix[1][1] = 'Yet To Start'
Matrix[2][1] = 'Yet To Start'
Matrix[3][1] = 'Yet To Start'
Matrix[4][1] = 'Yet To Start'
Matrix[5][1] = 'Ongoing'
#Team 1
Matrix[0][2] = 'BPHC'
Matrix[1][2] = 'BPHC'
Matrix[2][2] = 'BPHC'
Matrix[3][2] = 'BPHC'
Matrix[4][2] = 'BPHC'
Matrix[5][2] = 'BPHC'

#just for easy code
Matrix[0][3] = 'Vs'
Matrix[1][3] = 'Vs'
Matrix[2][3] = 'Vs'
Matrix[3][3] = 'Vs'
Matrix[4][3] = 'Vs'
Matrix[5][3] = 'Vs'

#Team 2
Matrix[0][4] = 'BPHC' 
Matrix[1][4] = 'BPHC'
Matrix[2][4] = 'BPHC'
Matrix[3][4] = 'BPHC'
Matrix[4][4] = 'BPHC'
Matrix[5][4] = 'BPHC'

#Score String 

Matrix[0][5] = '245/3(20) and 112/3(12)'
Matrix[1][5] = '3-2'
Matrix[2][5] = '21-16, 12-1'
Matrix[3][5] = '21-11, 21-3'
Matrix[4][5] = '12-1,12-6,12-2'
Matrix[5][5] = '12-1,12-6,12-2'

#Change_value
change_location = 00


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




@app.route('/update', methods=['GET', 'POST'])
def main_updater():
	global change_location
	
	if request.method == 'POST':
		d = request.form['dhtml']
		change_location = int(d)
		#print d
		return redirect(url_for('input_page'))
	# count = 0
	return render_template('score_updater.html', params = Matrix)

@app.route('/input',methods=['GET','POST'])
def input_page():
	global change_location
	if request.method == 'GET':
		return render_template('input_page.html')

	if request.method == 'POST':
		d = request.form['change_']
		print ("well=" + d)
		print("9chell = "+ str(change_location))
		x = int(change_location%10 -1) 
		y = int(change_location/10 -1)
		print("qchell = "+ str(change_location))
		Matrix[x][y] = str(d)
	# count = 0
	return redirect(url_for('main_updater'))

@app.route('/tvscreen', methods=['GET', 'POST'])
def screen_tv_show():
    return render_template('main_monitor_score.html', params=Matrix)


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
