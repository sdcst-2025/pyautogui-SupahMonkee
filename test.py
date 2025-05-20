import pyautogui as p
import time as t
#p.mouseInfo()

while True:
    t.sleep(0.5)
    x = p.pixel(100,100)
    print('found',x)
