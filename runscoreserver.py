import os
import flask
import time
import datetime
import requests
from collections import deque

from flask import Flask,request ,render_template

app=Flask(__name__)

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME']:
            error = 'Invalid username'
        elif request.form['password'] != app.config['PASSWORD']:
            error = 'Invalid password'
        else:
            session['logged_in'] = True
            flash('You were logged in')
            return redirect(url_for('show_entries'))
return render_template('login.html', error=error)# n=150
# #total no of token available
# tokens=list()
# time_hist=dict()

# token_que = deque()

# for i in range(n):
# 	time_hist[i]=list()

# time_start_sec=dict()
# time_end_sec=dict()

# def time_min(sec):
# 	return datetime.datetime.fromtimestamp(sec).strftime('%Y-%m-%d %H:%M:%S')

# def sendToServer(timeout):
# 	print "started thread"
# 	while (True):
# 		if token_que:
# 			q = token_que[0]
# 			payload = {'token': str(q)}
# 			try:
# 				r = requests.post('http://mess1-bot.mybluemix.net/ready',data=payload)
# 				print r.status_code
# 				if r.text == "Got it!!":
# 					token_que.popleft()
# 			except:
# 				print "Connection Error"
# 				time.sleep(5)



# @app.route("/")
# def display():
# 	if request.method=='GET':
# 		if len(tokens)<15:
# 			return render_template('main_monitor.html', params=tokens)
# 		else:
# 			return render_template('main_monitor.html',params=tokens[0:15])

# @app.route("/anc_mess1/", methods=['GET','POST'])
# def main():
# 	if request.method=='GET':
# 		return render_template('form.html',params=tokens)
	
# 	if request.method=='POST':
# 		# print 2
# 		if "q" in request.form.keys():  
# 			q=request.form['q']
# 			if q and q.isdigit():
# 				q=int(q)
# 				if q>150:
# 					pass
# 				else:
# 					if q in tokens:         
# 						pass
# 					else:
# 						time_start_sec[q]=time.time()
# 						tokens.append(q)
# 						tokens.sort()
# 						token_que.append(q)


# 		if "d" in request.form.keys():
# 			d=request.form['d']
# 			if d and d.isdigit():
# 				d = int(d)
# 				time_end_sec[d]=time.time()
# 				time_hist[d].append((time_min(time_start_sec[d]) ,time_min(time_end_sec[d]) ,(time_end_sec[d]-time_start_sec[d])/60))
# 				tokens.remove(d)
# 				if d in token_que:
# 					token_que.remove(d)				 
# 				tokens.sort()
		
		
			
# 		return render_template('form.html',params=tokens)

# @app.route("/info/",methods=['GET','POST'])
# def info():
# 	if request.method=='GET':
# 		return render_template('info.html')
# 	else:
# 		if 'q' in request.form.keys():
# 			q = request.form['q']
# 			if q.isdigit():
# 				q = int(q)
# 				return render_template('info.html', time_hist = time_hist, obj = q)




if __name__=='__main__':
	# try:
	# 	thread.start_new_thread(sendToServer , (10,))
	# except:
	# 	print "Error: unable to start thread"

	app.debug=True
	app.run(host='0.0.0.0',port=80)
