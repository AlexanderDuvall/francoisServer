#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  helloworld.py
#  
#  Copyright 2022  <team1elet4208-2022@raspberrypi>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  

import cv2
import numpy as np
import matplotlib 
matplotlib.use('TkAgg')
from matplotlib import pyplot as plt
#import tkinter
#from _tkinter import *

#img = cv2.imread('/home/team1elet4208-2022/project/env/lib/python3.10/site-packages/Temp/plastic-bottles',cv2.IMREAD_COLOR)
#cv2.line(img, (0,0), (150,150), (255,255,255),)
#plt.figure()
#plt.imshow(img,interpolation='nearest')
#plt.show()

#cv2.waitKey(0)
#cv2.destroyAllWindows()


#thres = 0.45 # Threshold to detect object

classNames = []
classFile = "/home/team1elet4208-2022/Desktop/Object_Detection_Files/coco.names"
with open(classFile,"rt") as f:
    classNames = f.read().rstrip("\n").split("\n")

configPath = "/home/team1elet4208-2022/Desktop/Object_Detection_Files/ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt"
weightsPath = "/home/team1elet4208-2022/Desktop/Object_Detection_Files/frozen_inference_graph.pb"

net = cv2.dnn_DetectionModel(weightsPath,configPath)
net.setInputSize(320,320)
net.setInputScale(1.0/ 127.5)
net.setInputMean((127.5, 127.5, 127.5))
net.setInputSwapRB(True)


def getObjects(img, thres, nms, draw=True, objects=[]):
    classIds, confs, bbox = net.detect(img,confThreshold=thres,nmsThreshold=nms)
    #print(classIds,bbox)
    if len(objects) == 0: objects = classNames
    objectInfo =[]
    if len(classIds) != 0:
        for classId, confidence,box in zip(classIds.flatten(),confs.flatten(),bbox):
            className = classNames[classId - 1]
            if className in objects:
                objectInfo.append([box,className])
                if (draw):
                    cv2.rectangle(img,box,color=(0,255,0),thickness=2)
                    cv2.putText(img,classNames[classId-1].upper(),(box[0]+10,box[1]+30),
                    cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),2)
                    cv2.putText(img,str(round(confidence*100,2)),(box[0]+200,box[1]+30),
                    cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),2)
                    
    return img,objectInfo


if __name__ == "__main__":

    cap = cv2.VideoCapture(0)
    cap.set(3,640)
    #cap.set(4,480)
    #cap.set(10,70)
    

    while True:
#        success, img = cap.read()
        img = cv2.imread("/home/team1elet4208-2022/test.jpeg")
        result, objectInfo = getObjects(img,0.45,0.2)
        print("adsfdsafsadf")
        print(objectInfo);
        #print(objectInfo)
        cv2.waitKey(1)
        exit()
