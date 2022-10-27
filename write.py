import pyautogui
import time
import random

time.sleep(5)

text = "Text"
for _ in range(1):
    pyautogui.typewrite(text)
    pyautogui.press('enter')
    time.sleep(1)
