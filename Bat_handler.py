import AntiAFK
import AntiAFK_click

def Bat_Handler():
    print("Bat Handler is running...")
    print("Press 1 for mouse jiggle, 2 for click, or 3 to exit.")
    choice = input("Enter your choice: ")

    if choice == '1':
        AntiAFK.jiggle_mouse()
    elif choice == '2':
        AntiAFK_click.click()
    elif choice == '3':
        print("Exiting Bat Handler.")
    else:
        print("Invalid choice. Please try again.")
        Bat_Handler()

if __name__ == "__main__":
    Bat_Handler()