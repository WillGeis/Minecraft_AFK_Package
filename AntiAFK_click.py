import pyautogui
import random
import time

def click():
    while True:
        time = random.randint(1, 100)
        pyautogui.click()
        print("Mouse clicked.")
        time.sleep(10 + time * .001 + time)

if __name__ == "__main__":
    click()