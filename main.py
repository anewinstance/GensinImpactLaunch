import pygame
from pygame.locals import *
from PIL import Image
import numpy as np
import pyautogui
import time
import cv2
from config import *
import psutil
import os

#ts=time.time()
#初始化
pygame.init()
pygame.mixer.init()
displayInfo = pygame.display.Info()
if launchSound=="":
    launchSound="default.mp3"
pygame.mixer.music.load(launchSound)
DW,DH=displayInfo.current_w,displayInfo.current_h
def Launch():
    os.startfile(launchPath)
    time.sleep(soundDelay)
    pygame.mixer.music.play()
    time.sleep(15)
    flag=0
    while 1:
        #print("没有退出")
        pl = psutil.pids()
        for pid in pl:
            if procressName in psutil.Process(pid).name():
                #print("已退出")
                flag=1
                break
        if flag:
            break
        time.sleep(10)

#主循环
while 1:
    #截图+转换格式
    img = pyautogui.screenshot(region=[0, 0, 1920, 1080])
    imgresize=img.resize(imageSize).convert("1")
    imgc=cv2.cvtColor(np.array(img),cv2.COLOR_BGR2GRAY)

    if judgeMethod==1:
        imgwhite=imgc>=255*(launchThreshold/100)
        wpc=np.count_nonzero(imgwhite)
        #print(wpc,"/",1920*1080) #Debug
        if(wpc/(DW*DH)>=launchThreshold/100):
            Launch()

    elif judgeMethod==0:
        #旧方案:求平均值
        average=np.mean(np.mat(imgc))
        if average>=250:
            Launch()
            #print("启动！！！")
        #print(average)  #输出平均值
    
    time.sleep(judgeDelay)
#print(time.time()-ts,type(imgc),np.mean(np.mat(imgc))) #Debug
#cv2.imshow("233",imgc)
#cv2.waitKey(0)