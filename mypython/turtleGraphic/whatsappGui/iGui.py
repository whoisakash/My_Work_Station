import pyautogui as pg
import time

print("program will rn i 5 sec")
time.sleep(5)

for i in range(5):
    pg.write("i am ready")
    time.sleep(0.5)
    pg.press("Enter")