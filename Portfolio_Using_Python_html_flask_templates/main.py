from flask import Flask, render_template, request
import requests
import json

app = Flask('app')

API_KEY = "0c064bf24b52b7b932f6a82713a2f773"
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/edu')
def edu():
    return render_template('edu.html')

@app.route('/exp')
def exp():
    return render_template('exp.html')

@app.route('/skills')
def skills():
    return render_template('skills.html')

@app.route('/Contact')
def contact():
    return render_template('Contact.html')

@app.route('/dash')
def dash():
    return render_template('dash.html')

@app.route('/gis')
def gis():
    return render_template('gis.html')
@app.route('/iss')
def iss():
    return render_template('iss.html')
@app.route('/case_r')
def case_r():
    return render_template('case_r.html')
@app.route('/Case_study_1')
def Case_study_1():
    return render_template('Case_study_1.html')

app.run(host='0.0.0.0', port=8080)
