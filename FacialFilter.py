# -*- coding: utf-8 -*-
"""
Created on Tue Jun 22 15:47:16 2021

@author: jackb
"""

import cv2
import sys
import PillowEdgeDetect

faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

video_capture = cv2.VideoCapture(0)
img_counter = 0


while True:
  #capture frame by frame
  ret, frame = video_capture.read()
  #cv2.imshow('frame', frame)
  gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
  k = cv2.waitKey(1)
  faces = faceCascade.detectMultiScale(gray,scaleFactor=1.5,minNeighbors=5,minSize=(30,30),flags=cv2.CASCADE_SCALE_IMAGE)
  print(faces)
  
  #draw rectangle around faces
  for (x,y,w,h) in faces:
      cv2.rectangle(frame,(x,y),
                    (x+w,y+h),(0,255,0),
                    2)
      frame = PillowEdgeDetect.filterRectangle(frame,(x,y,w,h))
      print(type(frame))
  
  #display result
  print(frame)
  cv2.imshow('FaceDetection',frame)

  if k%256 == 27: #ESC pressed
    break
  elif k%256 == 32: #SPACE pressed
    img_name = "FaceDetect_webcam_{}.png".format(img_counter)
    cv2.imwrite(img_name, frame)
    print("{} written".format(img_name))
    img_counter += 1

#Release the capture
video_capture.release()
cv2.destroyAllWindows()
