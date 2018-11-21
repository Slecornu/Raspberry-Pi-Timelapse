# -*- coding: utf-8 -*-
"""
Created on Thu Sep  6 20:39:47 2018

@author: Sam Le-Cornu
"""
from picamera import PiCamera
from time import sleep
import os, datetime

def main():
    folder = createFolder()

    #waiting for sunrise
    hour = 0
    while(hour != 6):
        print(hour)
        sleep(60)
        now = datetime.datetime.now()
        hour = now.hour

    name = 1
    extention = '.jpg'
    camera = PiCamera()
    camera.start_preview()
    while True:
        sleep(1)
        n = str(name)
        if(len(n) > 6):
            #finish taking Pictures
            print("timelapse ended on 1,000,000 pictures...")
            break;
        while len(n) < 6:
            n = "0"+n
        path = folder + n + extention
        camera.capture(path)
        print(path)
        name += 1
    camera.stop_preview()


def createFolder():
    name = raw_input("Name of timelaspe:")
    directory = '/home/pi/Pictures/timelapse/'+ name + '/'
    if os.path.isdir(directory):
        print("Folder exists, please enter a new directory:")
        return createFolder()
    else:
        os.makedirs(directory)
        return directory

main()
print("MAIN")
