import webbrowser

import pyautogui
import time
import os

# webbrowser.open('http://127.0.0.1:8887/attend.html', new=0, autoraise=True)
# time.sleep(7)
# pyautogui.press('f11')
# time.sleep(4)



pyautogui.hotkey('ctrl', 'tab')
webbrowser.open("/home/pi/Desktop/GIH/fingerprint/attend.mp3")
time.sleep(3)
pyautogui.hotkey('ctrl', 'tab')
os.system("python /home/pi/Desktop/GIH/search.py")