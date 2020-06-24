#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 17:15:35 2020

@author: tianlu
"""


import cv2

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

img = cv2.imread("images/photo.jpg")

multifaces_img = cv2.imread("images/news.jpg")

gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray_img,
scaleFactor=1.05,
minNeighbors=5)

multi_faces = face_cascade.detectMultiScale(multifaces_img,
scaleFactor=1.5,
minNeighbors=5)

for x,y,a,b in faces:
    img = cv2.rectangle(img,(x,y),(x+a,y+b),(0,255,0),3)
    
for h,i,j,k in multi_faces:
    multi_img = cv2.rectangle(multifaces_img,(h,i),(h+j,i+k),(0,255,0),3)


#cv2.imshow("detect face",img)
cv2.imshow("detect face",multi_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.waitKey(1)
