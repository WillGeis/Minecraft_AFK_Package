import pyautogui
import random
import time

def jiggle_mouse():
    while True:
        # Generate random movement change based on resolution of monitor
        dx = random.randint(-200, 200)
        dy = random.randint(-200, 200)
        
        # to use this you need to run pip install pyautogui in powershell
        x, y = pyautogui.position()
        
        # Move the mouse
        pyautogui.moveTo(x + dx, y + dy)
        print(f"Mouse moved to: ({x + dx}, {y + dy})")
        
        # Wait for 4 seconds
        time.sleep(4)

if __name__ == "__main__":
    jiggle_mouse()
