# -*- coding: utf-8 -*-
"""
Created on Tue Nov  1 17:32:33 2022

@author: NAVEEN REDDY
"""

import gzip, dill
from flask import Flask, request, render_template, redirect
app = Flask(__name__) 
@app.route('/')
def main():
    return redirect('/index')
@app.route('/index', methods=['GET'])
def index():
    return render_template('index.html')
@app.route('/about')
def about():
    return "this is page is all about my ML model"
@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'GET':
        tweet = request.args.get('tweet')
    else:
        tweet = request.form['text']
    
    with gzip.open("model.dill.gz", 'rb') as f:
        model = dill.load(f)
        
    proba = model.predict_proba([tweet])[0,1] #it's will return two columns, index 0 is negative index 1 is positive
    return "positive sentiment: {}".format(proba)
    
    
if __name__ == '__main__':
    app.run()