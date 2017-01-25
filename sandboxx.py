#This file is for writing code snippets since I hate clutterd and too much code

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


dict = {'Sports':'-1' ,'Team1':'BPHC','Team2':'-1','Score':'-1','Status':'-1'}

@app.route('/', methods=['GET','POST'])
def main_updater():
	if request.method == 'GET':
		return render_template('score_updater.html')

	if request.method == 'POST':
		Sports = request.form['sports_drop']
		Team1 = request.form['team1']
		Team2 = request.form['team2']
		Score = request.form['disp_score']
		Status = request.form['status_match']
		
		print(Sports+Team1)
		return Team1



if __name__=='__main__':
	# try:
	# 	thread.start_new_thread(sendToServer , (10,))
	# except:
	# 	print "Error: unable to start thread"

	app.debug=True
	app.run(host='0.0.0.0',port=8090)
