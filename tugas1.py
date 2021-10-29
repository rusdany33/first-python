# -*- coding: utf-8 -*-
"""
Created on Sat Oct 30 03:40:22 2021

@author: rusda
"""

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    html="""
    <html>
    <head>
    <title></title>
    </head>
<style type="text/css">
    body{
        background-color: grey;
    }
    h1{
        font-family: sans-serif;
        font-size: 30px;
        color: salmon;
    }
    h2{
        color:saddlebrown;
    }
</style>
<body>
    <center><h1><p>Hai Semuanya</p></h1></center>
    <center><h2> <p>perkenalkan nama saya rusdany maestro</p></h2></center>
    <center><h2><br>saya lahir di Sidoarjo <br>sekarang sedang menempuh Studi di D4 Teknik Informatika</h2></center>
</body>
</html>>
         """
    return html