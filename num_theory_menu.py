from NumberTheory.egyptian_fraction import egy_run
from NumberTheory.euclidean_algorithm import euc_run
from NumberTheory.fibonacci import fib_run
from NumberTheory.gcd_lcd import gcd_lcd
from NumberTheory.mod import mod_run
from NumberTheory.prime import prime_run
import os

def clear_screen():
    # Clear the screen based on the operating system
    if os.name == 'nt':  # For Windows
        os.system('cls')
    else:  # For Unix/Linux/Mac
        os.system('clear')

def num_theory_menu():
    while True:
      
        print("=== NUMBER THEORY ===\n")
        print("1. Egyptian Fraction")
        print("2. Euclidean Algorithm")
        print("3. Fibonacci Sequence")
        print("4. GCD and LCD")
        print("5. Modular Arithmetic")
        print("6. Find Primes in Range")
        print("7. Exit")

        choice = input("Enter your choice (1-7): ")
        clear_screen()  # Clear the screen before displaying the menu

        if choice == '1':
            egy_run()
        elif choice == '2':
            euc_run()
        elif choice == '3':
            fib_run()
        elif choice == '4':
            gcd_lcd()
        elif choice == '5':
            mod_run()
        elif choice == '6':
            prime_run()
        elif choice == '7':
            print("[ Exited NUMBER THEORY MENU ]\n")
            break
        else:
            print("Invalid choice, please try again.")
            input("Press Enter to continue...")  # Pause for user to read the invalid message before clearing the screen


if __name__ == "__main__":
    num_theory_menu()
