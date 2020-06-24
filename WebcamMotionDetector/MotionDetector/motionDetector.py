#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 18:24:59 2020

@author: tianlu
"""


import cv2
from datetime import datetime
import pandas


first_frame = None
status_list = [None,None]
times = []
dataFrame = pandas.DataFrame(columns=["Start","End"])

video = cv2.VideoCapture(0)

while True:
    check,frame = video.read()
    
    status = 0
    
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray_frame = cv2.GaussianBlur(gray_frame,(21,21),0)
    
    
    if first_frame is None:
        first_frame = gray_frame
        continue
    
    delta_frame = cv2.absdiff(first_frame, gray_frame)
    thresh_frame = cv2.threshold(delta_frame,30,255,cv2.THRESH_BINARY)[1]
    thresh_frame = cv2.dilate(thresh_frame, None,iterations=2)
    
    (cnts,_) = cv2.findContours(thresh_frame.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    
    for coutour in cnts:
        if cv2.contourArea(coutour)< 1000:
            continue
        status = 1
        (x,y,w,h)=cv2.boundingRect(coutour)
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),3)
    
    status_list.append(status)
    
    if status_list[-1]==1 and status_list[-2]==0:
        times.append(datetime.now())
        
    if status_list[-1]==0 and status_list[-2]==1:
        times.append(datetime.now())
    
    cv2.imshow("gray",gray_frame)
    cv2.imshow("delta", delta_frame)
    cv2.imshow("Threshold",thresh_frame)
    cv2.imshow("ColorFrame", frame)
    
    key = cv2.waitKey(1)
    
    if key == ord('q'):
        if status == 1:
            times.append(datetime.now())
        break;

for i in range(0,len(times),2):
    dataFrame = dataFrame.append({"Start":times[i],"End":times[i+1]},ignore_index=True)


dataFrame.to_csv("motionTimes.csv")
video.release()
cv2.destroyAllWindows()   
cv2.waitKey(0)
    
    
        
        

