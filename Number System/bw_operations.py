def total(binary):
    decimal_value = 0
    for i in range(len(binary)):
        bit = int(binary[len(binary) - 1 - i])
        decimal_value += bit * (2 ** i)
    return decimal_value

def perform_bitwise_operations(x, y):
    if len(x) != len(y):
        raise ValueError("Binary strings must be of the same length.")

    result_and = ""
    result_or = ""
    result_xor = ""
    result_not_x = ""
    result_not_y = ""

    for i in range(len(x)):
        bit_a = int(x[i])
        bit_b = int(y[i])
        result_and += str(bit_a & bit_b)
        result_or += str(bit_a | bit_b)
        result_xor += str(bit_a ^ bit_b)
        result_not_x += str(1 - bit_a)
        result_not_y += str(1 - bit_b)

    spc = 8
    print("+-----+-----+-----+-----+-----+-----+-----+")
    print("|  X  |  Y  | AND | OR  | XOR | ~X  | ~Y  |")
    print("+-----+-----+-----+-----+-----+-----+-----+")
    
    for i in range(len(x)):
        print(f"| {x[i]:<3} | {y[i]:<3} | {result_and[i]:<3} | {result_or[i]:<3} | {result_xor[i]:<3} | {result_not_x[i]:<3} | {result_not_y[i]:<3} |")
    
    print("+-----+-----+-----+-----+-----+-----+-----+")
    print(f"| {total(x):<3} | {total(y):<3} | {total(result_and):<3} | {total(result_or):<3} | {total(result_xor):<3} | {total(result_not_x):<3} | {total(result_not_y):<3} |")
    print("+-----+-----+-----+-----+-----+-----+-----+")

def main_bitwise_operations():
    x = input("Enter Binary X: ")
    y = input("Enter Binary Y: ")
    
    try:
        perform_bitwise_operations(x, y)
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main_bitwise_operations()
