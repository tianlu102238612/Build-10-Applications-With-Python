#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 17 18:57:30 2020

@author: tianlu
"""


import mysql.connector

con = mysql.connector.connect(
    user = "ardit700_student",
    password = "ardit700_student",
    host = "108.167.140.122",
    database = "ardit700_pm1database"
    )

word = input("enter word: ")

cursor = con.cursor()
query = cursor.execute("SELECT * FROM Dictionary WHERE EXPRESSION = '%s'" %word)
results = cursor.fetchall()

for result in results:
    print(result)