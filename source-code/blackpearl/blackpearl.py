#!/usr/bin/env python
#
# filename: 039.py
# author:   DTT,Lan Le, Phuc
# date:     18-Nov-2015
# purpose:  flask server
#
from flask import Flask, render_template, request
from movement import Movement
import json

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/movement', methods=['POST'])
def handle_movement():
    ''' handle movement action sent from web browser. '''
    if request.method == 'POST':
        action = request.form['action']
        print 'Log - action: '+action
        
        movement = Movement()
        movement.handleAction(action)
        
        return json.dumps({'logContent':'passed!'})

if __name__ == '__main__':
	app.run(host="10.0.0.4", port=8080, debug=True, threaded=True)
