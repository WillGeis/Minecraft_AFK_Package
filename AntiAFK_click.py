import pyautogui
import random
import time

def click():
    print("Press 'R' for random time, press 'T' for fixed time.")
    choice = input("Enter your choice: ")
    if choice.casefold() == 'r':
        while True:
            wait_time = random.randint(1, 100)
            pyautogui.click()
            print(f"Mouse clicked {wait_time} seconds")
            time.sleep(10 + wait_time)
    elif choice.casefold() == 't':
        clickfixed()

def clickfixed():
    print("Enter the fixed time interval in seconds:")
    choice2 = input()
    if not choice2.isdigit():
        print("Please enter a valid number.")
        clickfixed()
        return
    wait_time = int(choice2)
    while True:
        pyautogui.click()
        print("Mouse clicked.")
        time.sleep(10 + wait_time)

if __name__ == "__main__":
    click()