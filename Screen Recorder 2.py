# SCREEN RECORDER PROJECT

#(here tkinter library import the GUI for screen recorder frame )
from tkinter import Frame

#(turtle lib import the screensize to align the screen resolution)
from turtle import screensize

#(here i have used opencv contrib package of python)
import cv2

#(Then i have used numpy lib of python)
import numpy as np

#(This is pyautogui lib of python)
import pyautogui

#(for specifying screen resolution)
screen_size = (1920,1080)

 #(This command is used to save the video in MP4 format)
fourcc = cv2.VideoWriter_fourcc(*"XVID")

out = cv2.VideoWriter("output.avi",fourcc,20.0,(screen_size))
                    #(format , encoding/decoding , frame rate , resolution )

#(While loop is used to stop the recording)
while True:
    #(here pyautogui take the screenshot per frame & align them in order to make a video)
    img = pyautogui.screenshot()

    #(here i have declared an array using numpy)
    frame = np.array(img)

    #(This command is used for RGB colour accuracy of the video)
    frame = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    out.write(frame)
    cv2.imshow("Screen Recorder",frame)

    #(this is for stoping the recording)
    if cv2.waitKey(1)==ord("q"):
        break
