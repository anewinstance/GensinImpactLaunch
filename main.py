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
import tkinter as tk
from threading import Thread

#ts=time.time()
#初始化
pygame.init()
pygame.mixer.init()
displayInfo = pygame.display.Info()
if launchSound=="":
    launchSound="default.mp3"
pygame.mixer.music.load(launchSound)
DW,DH=displayInfo.current_w,displayInfo.current_h
threadKill=0

def splashoff():
    root.destroy()


def splash():
    global root 
    root = tk.Tk()
    root.geometry(f"{DW}x{DH}+0+0")
    root.overrideredirect(1)
    root.wm_attributes("-toolwindow", True)
    root.wm_attributes("-topmost", True)
    root.after(soundDelay*1000,splashoff)
    root.mainloop()

def Launch():
    try:
        os.startfile(launchPath+" "+launchFlag)
    except Exception as e:
        print("可执行文件路径异常(无法启动)")
        print("如果你遇到了此问题，你可以把错误代码提供给支持人员（有没有支持人员就是另外一回事了）")
        print("错误代码：", e)
    pyautogui.keyDown('winleft')
    pyautogui.press("down")
    pyautogui.press("down")
    pyautogui.keyUp('winleft')
    sp=Thread(target=splash,daemon=True)
    sp.start()
    time.sleep(soundDelay)
    #播放声音
    pygame.mixer.music.play()
    time.sleep(15)
    while 1:
        try:
            pl = psutil.pids()
            flag=0
            for pid in pl:
                if procressName in psutil.Process(pid).name():
                    print("没有退出")
                    flag=1
        except:
            pass
        if not flag:
            print("已退出")
            break
        time.sleep(antiRelaunch)

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