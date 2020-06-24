#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 17:49:52 2020

@author: tianlu
"""


import cv2

video = cv2.VideoCapture(0)

while True:
    check,frame = video.read()
    cv2.imshow("capturing", frame)
    key = cv2.waitKey(1)
    
    if key==ord('q'):
        break

video.release()
cv2.destroyAllWindows()
