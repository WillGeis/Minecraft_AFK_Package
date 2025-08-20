import pyautogui
import random
import time

def click():
    while True:
        pyautogui.click()
        print("Mouse clicked.")
        time.sleep(4)

if __name__ == "__main__":
    click()