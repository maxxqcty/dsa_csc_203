from Cryptography.aes import run_aes
from Cryptography.des_process import DES
from Cryptography.diffie_helman import run_dh
from Cryptography.caesar_cipher import run_cc
from Cryptography.rsa import run_rsa

import os

def clear_screen():
    # Clear the screen based on the operating system
    if os.name == 'nt':  # For Windows
        os.system('cls')
    else:  # For Unix/Linux/Mac
        os.system('clear')


def crypto_menu():
    while True:
        print("=== CRYPTOGRAPHY ===\n")
        print("1. Advance Encryption Standard")
        print("2. Caesar Cipher")
        print("3. Data Encryption Standard")
        print("4. Diffie-Helman Key Exchange")
        print("5. Rivest-Shamir-Adleman Algorithm")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")
        clear_screen();

        if choice == '1':
            run_aes()
        elif choice == '2':
            run_cc()
        elif choice == '3':
            DES.des_run()
        elif choice == '4':
            run_dh()
        elif choice == '5':
            run_rsa()
        elif choice == '6':
            print("[ Exited CRYPTOGRAPHY MENU ]\n")
            break
        else:
            print("Invalid choice, please try again.")
            input("Press Enter to continue...")  # P

if __name__ == "__main__":
    crypto_menu()
