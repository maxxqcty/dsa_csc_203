from crypto_menu import crypto_menu
from greedy_menu import greedy_menu
from mst_menu import mst_menu
from num_system_menu import num_system_menu
from num_theory_menu import num_theory_menu
import os
import sys

def clear_screen():
    # Clear the screen based on the operating system
    if os.name == 'nt':  # For Windows
        os.system('cls')
    else:  # For Unix/Linux/Mac
        os.system('clear')


def main_menu():
    while True:
        print("=== CSC203 LESSONS ===\n")
        print("1. NUMBER SYSTEMS")
        print("2. NUMBER THEORIES")
        print("3. CRYPTOGRAPHY")
        print("4. GREEDY ALGORITHMS")
        print("5. MINIMUM SPANNING TREE")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")
        clear_screen()  # Clear the screen before displaying the menu


        if choice == '1':
            num_system_menu()
        elif choice == '2':
            num_theory_menu()
        elif choice == '3':
          crypto_menu()
        elif choice == '4':
          greedy_menu()
        elif choice == '5':
          mst_menu()
        elif choice == '6':
            print("Program Finished.")
            sys.exit() 
            break
        else:
            print("Invalid choice, please try again.")

main_menu()
