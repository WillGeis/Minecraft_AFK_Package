import pyautogui
import random
import time

def click():
    print("Press 'R' for random time, press 'T' for fixed time.")
    choice = input("Enter your choice: ")
    if choice.casefold() == 'R'.casefold():
        while True:
            time = random.randint(1, 100)
            pyautogui.click()
            print("Mouse clicked." + time)
            time.sleep(10 + time)
    elif choice.casefold() == 'T'.casefold():
        clickfixed()
        

def clickfixed():
    print("Enter the fixed time interval in seconds:")
    choice2 = input()
    if input.isdigit() == False:
        print("Please enter a valid number.")
        clickfixed()
    while True:
        time = choice2
        pyautogui.click()
        print("Mouse clicked.")
        time.sleep(10 + time)

if __name__ == "__main__":
    click()