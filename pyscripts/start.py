import os
import webbrowser
import time
import pyautogui

webbrowser.open("/home/pi/Desktop/GIH/fingerprint/hello.mp3")



webbrowser.open('http://127.0.0.1:8887', new=0, autoraise=True)
webbrowser.open('http://127.0.0.1:8887/attend.html', new=0, autoraise=True)
time.sleep(10)
pyautogui.press('f11')
pyautogui.hotkey('ctrl', 'tab')
os.system("python password.py")
