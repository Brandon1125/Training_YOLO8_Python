#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 21 19:05:51 2023

@author: gera
"""

import cv2
from ultralytics import YOLO
import time

#img_name = "/home/gera/Desktop/data_nums/images/train/test_664.jpg"
# img_name = "/media/gera/ESD-ISO/0Frames3/0f3_0 (1).jpg"
# img = cv2.imread(img_name)
# model = YOLO("/home/gera/Desktop/vale/runs/detect/train2/weights/best.pt")

# pred = model.predict(img)[0]
# pred = pred.plot()
# cv2.namedWindow('Imagen')
# cv2.imshow('imag', pred)
#cv2.destroyAllWindows()

#cv2.imwrite(f"{img_name}.jpg",pred)

#######################################################
#model = YOLO("/home/gera/Desktop/vale/runs/detect/train2/weights/best.pt")
model = YOLO("C:/Users/mtto_/OneDrive/Escritorio/Proyect/Augmentation/Train YOLO8/runs/detect/train4/weights/last.pt")
# res= model.predict(
#     source='/home/gera/Desktop/recorte.avi',
#     conf=0.40,
#     save=True)

#video = cv2.VideoCapture("/home/gera/Desktop/recorte.avi")
# video = cv2.VideoCapture("C:/Users/mtto_/OneDrive/Escritorio/test.mp4")
# red, frame = video.read()
# frame = cv2.resize(frame, (0,0),fx=0.3,fy=0.3) 
# """
#video = cv2.VideoCapture("C:/Users/mtto_/OneDrive/Escritorio/test.mp4")
"""
while True:
    red, frame = video.read()
    
    if red:
        frame = cv2.rotate(frame, cv2.ROTATE_90_CLOCKWISE)
        frame = cv2.resize(frame, (0,0),fx=0.3,fy=0.3)                        
        res = model.predict(frame,conf=0.20, save=False)[0]
        # for label in res:
        #     lbl = str(label.boxes.cls)
        #     coord = label.boxes.xyxy[0]
        #     x_min = int(coord[0])
        #     y_min = int(coord[1])
        #     x_max = int(coord[2])
        #     y_max = int(coord[3])
            
        #     cv2.putText(frame, lbl, (x_min,y_min), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 0), 1)
        #     cv2.rectangle(frame, (x_min,y_min),(x_max,y_max), (255, 0, 255),2)
            
        # res= model.predict(
        #     source=frame,
        #     conf=0.20,
        #     save=False)
        
        frame = res.plot()
        # label = res[3]
        # lbl = str(label.boxes.cls)
        # cv2.putText(frame, lbl, (x_min,y_min), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 0), 1)
        #keypoints = res.keypoints  # Keypoints object for pose outputs
        # frame = keypoints.plot()
        frame = cv2.resize(frame, (0,0),fx=0.5,fy=0.5)# by vale
        
        cv2.imshow("violentin", frame)
        # time.sleep(0.5)
        
    else: break
    if cv2.waitKey(1) & 0xff == ord(" "):
        break

video.release()
cv2.destroyAllWindows()
"""



#img = cv2.imread("C:/Users/mtto_/OneDrive/Escritorio/Proyect/Augmentation/Train YOLO8/Dataset/train/aug_9Tablero_C - copia.png")
img = cv2.imread("C:/Users/mtto_/OneDrive/Escritorio/Proyect/Augmentation/Data/Tablero_C - copia.png")
#img = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
img = cv2.resize(img, (640, 640))
res = model.predict(img, conf=0.1, save=False)[0]

frame = res.plot()
cv2.imwrite("Result.png", frame)
cv2.imshow("s", frame)
cv2.waitKey(0)
