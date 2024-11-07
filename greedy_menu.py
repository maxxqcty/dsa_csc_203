from GreedyAlgorithm.act_select import run_act
from GreedyAlgorithm.coin_change import run_coin
from GreedyAlgorithm.huffman import run_huff
from GreedyAlgorithm.job_seq import run_job
from GreedyAlgorithm.knapsack import run_kp
from GreedyAlgorithm.mice_to_holes import run_mh



import os
import webbrowser

def clear_screen():
    # Clear the screen based on the operating system
    if os.name == 'nt':  # For Windows
        os.system('cls')
    else:  # For Unix/Linux/Mac
        os.system('clear')


def greedy_menu():
    while True:
        print("=== GREEDY ALGORITHMS ===\n")
        print("1. Activity Selection")
        print("2. Coin Change")
        print("3. Huffman Coding")
        print("4. Huffman Tree Visualizer")
        print("5. Job Sequencing")
        print("6. Knapsack Problem")
        print("7. Mice To Holes")
        print("8. Exit")

        choice = input("Enter your choice (1-8): ")
        clear_screen()
        if choice == '1':
            run_act()
        elif choice == '2':
            run_coin()
        elif choice == '3':
            run_huff()
        elif choice == '4':
          # Path to your HTML file
            file_path = 'huffman.html'

            # Open the HTML file in the default browser
            webbrowser.open(f'file:///C:/Users/user/Downloads/dsa_csc_203/huffman.html')
        elif choice == '5':
            run_job()
        elif choice == '6':
            run_kp()
        elif choice == '7':
            run_mh()
        elif choice == '8':
            print("[ Exited GREEDY ALGORITHMS MENU ]\n")
            break
        else:
            print("Invalid choice, please try again.")
            input("Press Enter to continue...")  # P

if __name__ == "__main__":
    greedy_menu()
