from NumberSystem.bit_calc import bit_calc
from NumberSystem.bit_conversion import main_conversions
from NumberSystem.bw_operations import main_bitwise_operations

import os

def clear_screen():
    # Clear the screen based on the operating system
    if os.name == 'nt':  # For Windows
        os.system('cls')
    else:  # For Unix/Linux/Mac
        os.system('clear')


def num_system_menu():
    while True:
        print("=== NUMBER SYSTEM ===\n")
        print("1. Binary Calculator")
        print("2. Binary Conversion")
        print("3. Bitwise Operations")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")
        clear_screen()  # Clear the screen before displaying the menu


        if choice == '1':
            bit_calc()
        elif choice == '2':
            main_conversions()
        elif choice == '3':
          main_bitwise_operations()
        elif choice == '4':
            print("[ Exited NUMBER SYSTEM MENU ]\n")
            break
        else:
            print("Invalid choice, please try again.")
            input("Press Enter to continue...") 

if __name__ == "__main__":
    num_system_menu()
