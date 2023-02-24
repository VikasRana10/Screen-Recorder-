"""# SCREEN RECORDER PROJECT
import datetime
from PIL import ImageGrab                 #(here i have used pillow lib of python)
import numpy as np                        #(here i have used numpy lib of python)
import cv2                                #(here i have used opencv contrib package of python)
from win32api import GetSystemMetrics     #(this pacakge is used to adjust the recorder with screen resolution)

width = GetSystemMetrics(0)
height = GetSystemMetrics(0)
time_stamp = datetime.datetime.now().strftime('%Y-%m-%d %H-%M-%S')   #(this is a dynamic timestamp for recorded video)
file_name = f'{time_stamp}.mp4'

fourcc = cv2.VideoWriter_fourcc('m','p','4','v')   #(This command is used to save the video in MP4 format)
captured_video = cv2.VideoWriter(file_name, fourcc, 20.0, (width, height))
                                #(format , encoding/decoding , frame rate , resolution )


webcam = cv2.VideoCapture(0)    #(this is to capture the video) 

#print(width, height)-> used to find out the screen resolution

while True:                                                  #(While loop is used to stop the recording)
    img = ImageGrab.grab(bbox=(0, 0, width, height))         #(here i have declare the coordiantes to grab the image)
    img_np = np.array(img)                                   #(here i have declared an array using numpy)
    img_final = cv2.cvtColor(img_np, cv2.COLOR_BGR2RGB)      #(its is used for RGB colour accuracy)
    _, frame = webcam.read()                                 #(this is for reading the captured image)
    fr_height, fr_width, _ = frame.shape
    img_final[0:fr_height, 0: fr_width, :] = frame[0: fr_height, 0: fr_width, :]
    cv2.imshow('webcam', frame)

    cv2.imshow('VRSCREEN', img_final)                        #(here i have used CV2 pacakge to show image)
    captured_video.write(img_final)                          #(this is for captured video)
    if cv2.waitKey(10) == ord('q'):                          #(this is for stoping the recording)
        break
"""