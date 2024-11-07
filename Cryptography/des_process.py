
import sys

class DES:
    S0_table = [
        [1, 0, 3, 2],
        [3, 2, 0, 1],
        [0, 2, 1, 3],
        [2, 1, 0, 3]
    ]

    S1_table = [
        [0, 1, 2, 3],
        [2, 0, 1, 3],
        [3, 0, 1, 2],
        [2, 1, 0, 3]
    ]

    def hexToInt_single(self, hex_str):
        return int(hex_str, 16)

    def intToBinaryString_single(self, num, bits=2):
        return format(num, '0{}b'.format(bits))

    def binaryToHex_single(self, binary_str):
        return format(int(binary_str, 2), 'x')

    def hexToInt(self, hex_list):
        return [int(x, 16) for x in hex_list]

    def hexToBinaryString(self, hex_values, bits=8):
        return [format(int(x, 16), '0{}b'.format(bits)) for x in hex_values]

    def binaryToHex(self, binary_str):
        return format(int(binary_str, 2), 'x')

    def valid_input(self, label, size, limit):
        num = []
        print(f"\nEnter your {label} Values")
        for i in range(size):
            while True:
                val = int(input(f"\n{label}[{i + 1}] = "))
                if limit <= val <= size:
                    num.append(val)
                    break
                else:
                    print(f"Invalid input. Please enter a valid number between {limit} and {size}.")
        return num

    def valid_key_input(self, label, size, limit):
        num = []
        print(f"\nEnter your {label} Values")
        for i in range(size):
            while True:
                val = int(input(f"\n{label}[{i}] = "))
                if val in [0, 1]:
                    num.append(val)
                    break
                else:
                    print(f"Invalid input. Please enter 0 or 1.")
        return num

    def display_box(self, label, values, inputSize, outputSize):
        boxWidth = 10 + inputSize * 4

        if label == "KEY":
            print("\nKEY: ", "".join(map(str, values)))
        else:
            print('_' * boxWidth)
            print("|" + f"{label:<{boxWidth - 1}}|")
            print("|Input   |" + "".join([f"{i:<4}" for i in range(1, inputSize + 1)]) + "|")
            print('-' * boxWidth)
            print("|Output  |" + "".join([f"{x:<4}" for x in values]) + "|")
            print('-' * boxWidth)

    def permutate(self, permPattern, bits, size, message):
        print(f"permutate {message}: ", end='')
        storage = [bits[permPattern[i] - 1] for i in range(size)]
        print("".join(map(str, storage)))
        return storage

    def left_shift(self, bits, shifts):
        return bits[shifts:] + bits[:shifts]

    def binaryStringToVector(self, binary_str):
        return [int(bit) for bit in binary_str]

    def IP_EP_STEP(self, PT, IP, EP, P4, K1):
        Initial = self.permutate(IP, PT, 8, "IP")

        left_half = Initial[:4]
        right_half = Initial[4:]

        print("\nCurrent Plaintext: ", "".join(map(str, PT)))
        print("IP: ", "".join(map(str, Initial)))
        print("left_half: ", "".join(map(str, left_half)))
        print("right_half: ", "".join(map(str, right_half)))

        EP_bit = self.permutate(EP, right_half, 8, "EP")

        XOR_result = [EP_bit[i] ^ K1[i] for i in range(8)]

        print("EP: ", "".join(map(str, EP_bit)))
        print("XOR of EP and K1: ", "".join(map(str, XOR_result)))

        S0 = XOR_result[:4]
        S1 = XOR_result[4:]

        S0_row = int(f"{S0[0]}{S0[3]}", 2)
        S0_col = int(f"{S0[1]}{S0[2]}", 2)
        S1_row = int(f"{S1[0]}{S1[3]}", 2)
        S1_col = int(f"{S1[1]}{S1[2]}", 2)

        print(f"S0 row: {S0_row}, col: {S0_col}")
        print(f"S1 row: {S1_row}, col: {S1_col}")

        S0_answer = self.S0_table[S0_row][S0_col]
        S1_answer = self.S1_table[S1_row][S1_col]

        s0_binary = self.intToBinaryString_single(S0_answer, 2)
        s1_binary = self.intToBinaryString_single(S1_answer, 2)

        print("S0 Output (binary): ", s0_binary)
        print("S1 Output (binary): ", s1_binary)

        combined_binary = s0_binary + s1_binary
        combined_vector = self.binaryStringToVector(combined_binary)

        P4_bit = self.permutate(P4, combined_vector, 4, "P4")

        XOR_result2 = [P4_bit[i] ^ left_half[i] for i in range(4)]

        final_answer = XOR_result2 + right_half

        print("XOR of IP,SOS1 and P4: ", "".join(map(str, final_answer)))

        shifted_answer = right_half + XOR_result2

        print("final_answer: ", "".join(map(str, shifted_answer)))

        return shifted_answer

    def des_menu(self):
        print("\n\n| ----- DES ----- |\n\n")
        print("| ---- USER INPUT FOR KEYS ---- |\n\n")
        p10 = self.valid_input("P10", 10, 1)
        p8 = self.valid_input("P8", 8, 1)
        p4 = self.valid_input("P4", 4, 1)
        EP = self.valid_input("EP", 8, 1)
        IP = self.valid_input("IP", 8, 1)
        KEY_INPUT = self.valid_key_input("KEY", 10, 0)

        self.display_box("P10", p10, 10, 10)
        self.display_box("P8", p8, 8, 8)
        self.display_box("P4", p4, 4, 4)
        self.display_box("EP", EP, 8, 8)
        self.display_box("IP", IP, 8, 8)
        self.display_box("KEY", KEY_INPUT, 10, 10)

        print("\n\n| ----- SOLVING FOR KEY ----- |\n")
        print("\n| ----- Getting Permutation and Key ----- |\n")

        self.display_box("KEY", KEY_INPUT, 10, 10)

        permuted_key = self.permutate(p10, KEY_INPUT, 10, "P10")

        left_half = permuted_key[:5]
        right_half = permuted_key[5:]

        left_half = self.left_shift(left_half, 1)
        right_half = self.left_shift(right_half, 1)

        combined_key_for_K1 = left_half + right_half

        K1 = self.permutate(p8, combined_key_for_K1, 8, "P8")

        print("\nKey 1: ", "".join(map(str, K1)))

        left_half = self.left_shift(left_half, 2)
        right_half = self.left_shift(right_half, 2)

        combined_key_for_K2 = left_half + right_half
        K2 = self.permutate(p8, combined_key_for_K2, 8, "P8")

        print("\nKey 2: ", "".join(map(str, K2)))

        decision = input("\n\nSingle Hexa Combination or Plaintext? (H/P) \n\n").strip()

        if decision == 'H':
            PT = input("\nEnter your PlainText: ").strip()
            hex_values = [format(ord(ch), 'x') for ch in PT]
            Integer_hex = self.hexToInt(hex_values)
            hex_to_binaries = self.hexToBinaryString(hex_values, 8)

            print("\n\n| ---- Complete Hex to Binary Values From Letters ---- | \n\n")
            print("Hex to Integers: ")
            for i in range(len(hex_values)):
                print(f"{hex_values[i]} = {Integer_hex[i]}")

            print("\nHex to Binaries: ")
            for i in range(len(hex_to_binaries)):
                print(f"{hex_values[i]} = {hex_to_binaries[i]}")

            print("\n\n| ---- Complete Hex to Binary Values From Letters ---- | \n\n")
            print("\n\n| ----- Round 1 ----- |\n\n")
                    
            XorFirstRound = []

            for i in range(len(hex_to_binaries)):
                print(f"------> Letter being Solved ----->\n {hex_values[i]} to binary: {hex_to_binaries[i]}")

                first_round = self.IP_EP_STEP(hex_to_binaries, IP, EP, p4, K1)
                XorFirstRound.append(first_round)

            self.again()

    def again(self):
        choice = input("Would you like to encrypt again? (Y/N): ").strip().upper()
        while choice == 'Y':
            self.des_menu()
            choice = input("Would you like to encrypt again? (Y/N): ").strip().upper()
        print("Exiting DES program. Goodbye!")
        sys.exit()

    def des_run():
        # Instantiate DES and run the menu
        des = DES()
        des.des_menu()

if __name__ == "__main__":
        DES.des_run()

#  -----------------------------------------------------------
# OUTPUT: 


# | ----- DES ----- |


# | ---- USER INPUT FOR KEYS ---- |



# Enter your P10 Values

# P10[1] = 5

# P10[2] = 3

# P10[3] = 8

# P10[4] = 9

# P10[5] = 10

# P10[6] = 1

# P10[7] = 2

# P10[8] = 4

# P10[9] = 7

# P10[10] = 6

# Enter your P8 Values

# P8[1] = 4

# P8[2] = 5

# P8[3] = 2

# P8[4] = 1

# P8[5] = 6

# P8[6] = 7

# P8[7] = 8

# P8[8] = 3

# Enter your P4 Values

# P4[1] = 2

# P4[2] = 3

# P4[3] = 1

# P4[4] = 1

# Enter your EP Values

# EP[1] = 1

# EP[2] = 0
# Invalid input. Please enter a valid number between 1 and 8.

# EP[2] = Traceback (most recent call last):
#   File "c:\Users\user\Downloads\dsa_csc_203\Cryptography Codes\des_process.py", line 228, in <module>
#     des.des_menu()
#   File "c:\Users\user\Downloads\dsa_csc_203\Cryptography Codes\des_process.py", line 149, in des_menu
#     EP = self.valid_input("EP", 8, 1)
#   File "c:\Users\user\Downloads\dsa_csc_203\Cryptography Codes\des_process.py", line 42, in valid_input
#     val = int(input(f"\n{label}[{i + 1}] = "))
# KeyboardInterrupt
# PS C:\Users\user> & C:/msys64/ucrt64/bin/python.exe "c:/Users/user/Downloads/dsa_csc_203/Cryptography Codes/des_process.py"


# | ----- DES ----- |


# | ---- USER INPUT FOR KEYS ---- |



# Enter your P10 Values

# P10[1] = 5

# P10[2] = 3

# P10[3] = 8

# P10[4] = 9

# P10[5] = 10

# P10[6] = 1

# P10[7] = 2 

# P10[8] = 4

# P10[9] = 7

# P10[10] = 6

# Enter your P8 Values

# P8[1] = 4

# P8[2] = 5

# P8[3] = 2

# P8[4] = 1

# P8[5] = 6

# P8[6] = 7

# P8[7] = 8

# P8[8] = 3

# Enter your P4 Values

# P4[1] = 2

# P4[2] = 3

# P4[3] = 1

# P4[4] = 1

# Enter your EP Values

# EP[1] = 4

# EP[2] = 3

# EP[3] = 2

# EP[4] = 1

# EP[5] = 4

# EP[6] = 2

# EP[7] = 1

# EP[8] = 3

# Enter your IP Values

# IP[1] = 2

# IP[2] = 3

# IP[3] = 5

# IP[4] = 6

# IP[5] = 7

# IP[6] = 1

# IP[7] = 4

# IP[8] = 8

# Enter your KEY Values

# KEY[0] = 1

# KEY[1] = 1

# KEY[2] = 0

# KEY[3] = 0

# KEY[4] = 0

# KEY[5] = 1

# KEY[6] = 1

# KEY[7] = 1

# KEY[8] = 1

# KEY[9] = 0
# __________________________________________________
# |P10                                              |
# |Input   |1   2   3   4   5   6   7   8   9   10  |
# --------------------------------------------------
# |Output  |5   3   8   9   10  1   2   4   7   6   |
# --------------------------------------------------
# __________________________________________
# |P8                                       |
# |Input   |1   2   3   4   5   6   7   8   |
# ------------------------------------------
# |Output  |4   5   2   1   6   7   8   3   |
# ------------------------------------------
# __________________________
# |P4                       |
# |Input   |1   2   3   4   |
# --------------------------
# |Output  |2   3   1   1   |
# --------------------------
# __________________________________________
# |EP                                       |
# |Input   |1   2   3   4   5   6   7   8   |
# ------------------------------------------
# |Output  |4   3   2   1   4   2   1   3   |
# ------------------------------------------
# __________________________________________
# |IP                                       |
# |Input   |1   2   3   4   5   6   7   8   |
# ------------------------------------------
# |Output  |2   3   5   6   7   1   4   8   |
# ------------------------------------------

# KEY:  1100011110


# | ----- SOLVING FOR KEY ----- |


# | ----- Getting Permutation and Key ----- |


# KEY:  1100011110
# permutate P10: 0011011011
# permutate P8: 00101011

# Key 1:  00101011
# permutate P8: 01011110

# Key 2:  01011110


# Single Hexa Combination or Plaintext? (H/P)

# H

# Enter your PlainText: 11101101

# | ----- DES ----- |


# | ---- USER INPUT FOR KEYS ---- |



# Enter your P10 Values

# P10[1] = 5

# P10[2] = 3

# P10[3] = 8

# P10[4] = 9

# P10[5] = 10

# P10[6] = 1

# P10[7] = 2

# P10[8] = 4

# P10[9] = 7

# P10[10] = 6

# Enter your P8 Values

# P8[1] = 4

# P8[2] = 5

# P8[3] = 2

# P8[4] = 1

# P8[5] = 6

# P8[6] = 7

# P8[7] = 8

# P8[8] = 3

# Enter your P4 Values

# P4[1] = 2

# P4[2] = 3

# P4[3] = 1

# P4[4] = 1

# Enter your EP Values

# EP[1] = 1

# EP[2] = 0
# Invalid input. Please enter a valid number between 1 and 8.

# EP[2] = Traceback (most recent call last):
#   File "c:\Users\user\Downloads\dsa_csc_203\Cryptography Codes\des_process.py", line 228, in <module>
#     des.des_menu()
#   File "c:\Users\user\Downloads\dsa_csc_203\Cryptography Codes\des_process.py", line 149, in des_menu
#     EP = self.valid_input("EP", 8, 1)
#   File "c:\Users\user\Downloads\dsa_csc_203\Cryptography Codes\des_process.py", line 42, in valid_input
#     val = int(input(f"\n{label}[{i + 1}] = "))
# KeyboardInterrupt
# PS C:\Users\user> & C:/msys64/ucrt64/bin/python.exe "c:/Users/user/Downloads/dsa_csc_203/Cryptography Codes/des_process.py"


# | ----- DES ----- |


# | ---- USER INPUT FOR KEYS ---- |



# Enter your P10 Values

# P10[1] = 5

# P10[2] = 3

# P10[3] = 8

# P10[4] = 9

# P10[5] = 10

# P10[6] = 1

# P10[7] = 2 

# P10[8] = 4

# P10[9] = 7

# P10[10] = 6

# Enter your P8 Values

# P8[1] = 4

# P8[2] = 5

# P8[3] = 2

# P8[4] = 1

# P8[5] = 6

# P8[6] = 7

# P8[7] = 8

# P8[8] = 3

# Enter your P4 Values

# P4[1] = 2

# P4[2] = 3

# P4[3] = 1

# P4[4] = 1

# Enter your EP Values

# EP[1] = 4

# EP[2] = 3

# EP[3] = 2

# EP[4] = 1

# EP[5] = 4

# EP[6] = 2

# EP[7] = 1

# EP[8] = 3

# Enter your IP Values

# IP[1] = 2

# IP[2] = 3

# IP[3] = 5

# IP[4] = 6

# IP[5] = 7

# IP[6] = 1

# IP[7] = 4

# IP[8] = 8

# Enter your KEY Values

# KEY[0] = 1

# KEY[1] = 1

# KEY[2] = 0

# KEY[3] = 0

# KEY[4] = 0

# KEY[5] = 1

# KEY[6] = 1

# KEY[7] = 1

# KEY[8] = 1

# KEY[9] = 0
# __________________________________________________
# |P10                                              |
# |Input   |1   2   3   4   5   6   7   8   9   10  |
# --------------------------------------------------
# |Output  |5   3   8   9   10  1   2   4   7   6   |
# --------------------------------------------------
# __________________________________________
# |P8                                       |
# |Input   |1   2   3   4   5   6   7   8   |
# ------------------------------------------
# |Output  |4   5   2   1   6   7   8   3   |
# ------------------------------------------
# __________________________
# |P4                       |
# |Input   |1   2   3   4   |
# --------------------------
# |Output  |2   3   1   1   |
# --------------------------
# __________________________________________
# |EP                                       |
# |Input   |1   2   3   4   5   6   7   8   |
# ------------------------------------------
# |Output  |4   3   2   1   4   2   1   3   |
# ------------------------------------------
# __________________________________________
# |IP                                       |
# |Input   |1   2   3   4   5   6   7   8   |
# ------------------------------------------
# |Output  |2   3   5   6   7   1   4   8   |
# ------------------------------------------

# KEY:  1100011110


# | ----- SOLVING FOR KEY ----- |


# | ----- Getting Permutation and Key ----- |


# KEY:  1100011110
# permutate P10: 0011011011
# permutate P8: 00101011

# Key 1:  00101011
# permutate P8: 01011110

# Key 2:  01011110


# Single Hexa Combination or Plaintext? (H/P)

# H

# Enter your PlainText: 11101101


# ENCRYPTED TEXT: 01011000
# HEX = 58