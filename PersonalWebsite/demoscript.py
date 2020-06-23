#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 18 15:10:55 2020

@author: tianlu
"""


from flask import Flask, render_template

demoapp = Flask(__name__)

@demoapp.route('/')
def home():
    return render_template("home.html")

@demoapp.route('/about/')
def about():
    return render_template("about.html")

if __name__ == "__main__":
    demoapp.run()