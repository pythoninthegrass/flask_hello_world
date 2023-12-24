#!/usr/bin/env python

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/hello')
def hello():
    return 'Hello, World!'


@app.route('/')
def home():
    return render_template('index.html')
