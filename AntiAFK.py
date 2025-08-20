import pyautogui
import random
import time

def jiggle_mouse():
    while True:
        dx = random.randint(-200, 200)
        dy = random.randint(-200, 200)
        x, y = pyautogui.position()
        target_x = x + dx
        target_y = y + dy

        steps = max(abs(dx), abs(dy))
        if steps == 0:
            steps = 1

        for i in range(1, steps + 1):
            new_x = int(x + (dx * i / steps))
            new_y = int(y + (dy * i / steps))
            pyautogui.moveTo(new_x, new_y, duration=0.01)

        print(f"Mouse moved to: ({target_x}, {target_y})")
        time.sleep(4)

if __name__ == "__main__":
    jiggle_mouse()