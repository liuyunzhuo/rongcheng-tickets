import pygetwindow as gw
import pyautogui
from utils import Widget, psnr, compare, save_png
import os
import time
import cv2
import numpy as np
from PIL import Image
import datetime


year = 2024
month = 4
day = 17
hour = 22
minutes = 36
seconds = 0

os.system("D:\微信\WeChat\WechatAppLauncher.exe -launch_appid=wxffa42ecd6c0e693d")
# 获取窗口
while True:
    window = gw.getWindowsWithTitle('成都蓉城足球俱乐部')
    if window != []:
        window = window[0]
        break

# 票务控件
piaoWu = Widget(237,730,275,773)
piaoWu.set_abs_pos(window.topleft)
anchor_piaoWu = cv2.imread('images\piaoWu.png')

# 票务标题控件
piaoWuTitle = Widget(184,69,228,95)
piaoWuTitle.set_abs_pos(window.topleft)
anchor_piaoWuTitle = cv2.imread('images\piaoWuTitle.png')

# 点击刷新控件
dianJiShuaXin = Widget(921-755,638-130,997-755,652-130)
dianJiShuaXin.set_abs_pos(window.topleft)

# 目标时间
target_date = datetime.datetime(year, month, day, hour, minutes, seconds)

while True:
    print("正在点击票务按钮...")
    if compare(anchor_piaoWu, piaoWu):
        while True:
            pyautogui.click(piaoWu.abs_center[0],piaoWu.abs_center[1])
            if compare(anchor_piaoWuTitle, piaoWuTitle):
                break
        break

while True:
    current_date = datetime.datetime.now()
    if current_date > target_date:
        # 执行某些操作
        pyautogui.click(dianJiShuaXin.abs_center[0],dianJiShuaXin.abs_center[1])
        print("完成操作")
        break
    else:
        print(f"当前时间已经在{year}年{month}月{day}日{hour}点{minutes}分{seconds}秒之前！")