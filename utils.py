from pygetwindow import Point,Rect
from PIL import Image
import cv2
import numpy as np
import math
import pyautogui

def psnr(img1, img2):
    mse = np.mean( (img1 - img2) ** 2 )
    if mse == 0:
        return 100
    PIXEL_MAX = 255.0
    return 20 * math.log10(PIXEL_MAX / math.sqrt(mse))

def compare(anchor, widget):
    screenshot = pyautogui.screenshot(region=(widget.abs_left, widget.abs_top, widget.width, widget.height))
    screenshot = cv2.cvtColor(np.array(screenshot),cv2.COLOR_RGB2BGR)
    print(psnr(anchor, screenshot))
    if psnr(anchor, screenshot)>35:
        return True
    else:
        return False

def save_png(widget,filename):
    screenshot = pyautogui.screenshot(region=(widget.abs_left, widget.abs_top, widget.width, widget.height))
    screenshot = cv2.cvtColor(np.array(screenshot),cv2.COLOR_RGB2BGR)
    cv2.imwrite(filename,screenshot)

class Widget():
    def __init__(self, left, top, right, bottom) -> None:
        """
        初始化顺序口诀：左上右下
        """
        self.top = top
        self.bottom = bottom
        self.left = left
        self.right = right
        self.width = right - left
        self.height = bottom- top
        self.center = Point((self.left + self.right)//2,(self.top + self.bottom)//2)
    def set_abs_pos(self,window_topleft):
        self.abs_left = window_topleft[0] + self.left
        self.abs_top = window_topleft[1] + self.top
        self.abs_right= window_topleft[0] + self.right
        self.abs_bottom= window_topleft[1] + self.bottom
        self.abs_center= Point(self.center[0]+window_topleft[0],self.center[1]+window_topleft[1])
