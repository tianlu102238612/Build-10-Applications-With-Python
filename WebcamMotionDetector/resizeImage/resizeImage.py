#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 11:51:12 2020

@author: tianlu
"""

import cv2

img=cv2.imread("galaxy.jpg",0)

resized_img = cv2.resize(img,(int(img.shape[1]/2),int(img.shape[0]/2)))
cv2.imwrite("Galaxy_resized.jpg", resized_img)

cv2.imshow("Galaxy",resized_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.waitKey(1)