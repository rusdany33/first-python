# -*- coding: utf-8 -*-
"""
Created on Fri Oct 29 15:48:04 2021

@author: rusda
"""

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>selamat datang di Web ku</p>"
    