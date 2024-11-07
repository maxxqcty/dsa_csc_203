from MST.boruvka import run_boruvka
from MST.dial import run_dial
from MST.dijkstra import run_dijkstra
from MST.kruskal import run_kruskal
from MST.prim import run_prim

import webbrowser

import os

def clear_screen():
    # Clear the screen based on the operating system
    if os.name == 'nt':  # For Windows
        os.system('cls')
    else:  # For Unix/Linux/Mac
        os.system('clear')


def mst_menu():
    while True:
        print("=== MINIMUM SPANNING TREE ===\n")
        print("1. Boruvka's Algorithm")
        print("2. Dial's Algorithm")
        print("3. Dijkstra's Algorithm")
        print("4. Kruskal's Algorithm")
        print("5. Prim's Algorithm")
        print("6. MST Visualizer")
        print("7. Exit")

        choice = input("Enter your choice (1-6): ")
        clear_screen()  # Clear the screen before displaying the menu

        if choice == '1':
            run_boruvka()
        elif choice == '2':
            run_dial()
        elif choice == '3':
            run_dijkstra()
        elif choice == '4':
            run_kruskal()
        elif choice == '5':
            run_prim()
        elif choice == '6':
            # Path to your HTML file
            file_path = 'index.html'

            # Open the HTML file in the default browser
            webbrowser.open(f'file:///C:/Users/user/Downloads/dsa_csc_203/mst.html')
            break
        elif choice == '7':
            print("[ Exited MINIMUM SPANNING TREE MENU ]\n")
            break
        else:
            print("Invalid choice, please try again.")
            input("Press Enter to continue...")  # P

if __name__ == "__main__":
    mst_menu()
