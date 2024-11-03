from bit_conversion import convert_to_decimal
from bit_conversion import convert_from_decimal

def convert_to_decimal(num, base):
    if base == 1:  # Binary
        return int(num, 2)
    elif base == 2:  # Decimal
        return float(num)
    elif base == 3:  # Octal
        return int(num, 8)
    elif base == 4:  # Hexadecimal
        return int(num, 16)
    else:
        raise ValueError("Invalid choice.")

def convert_from_decimal(num, base):
    if base == 1:  # Binary
        return bin(int(num))[2:]  # Remove '0b' prefix
    elif base == 2:  # Decimal
        return str(num)
    elif base == 3:  # Octal
        return oct(int(num))[2:]  # Remove '0o' prefix
    elif base == 4:  # Hexadecimal
        return hex(int(num))[2:]  # Remove '0x' prefix
    else:
        raise ValueError("Invalid choice.")

def perform_calculation(num1, num2, op, base):
    num1_dec = convert_to_decimal(num1, base)
    num2_dec = convert_to_decimal(num2, base)

    if op == '+':
        return num1_dec + num2_dec
    elif op == '-':
        return num1_dec - num2_dec
    elif op == '*':
        return num1_dec * num2_dec
    elif op == '/':
        if num2_dec == 0:
            raise ZeroDivisionError("Division by zero.")
        return num1_dec / num2_dec
    else:
        raise ValueError("Invalid operation.")

def execute_calculator(num1, num2, op, base):
    try:
        result = perform_calculation(num1, num2, op, base)
        print(f"\tResult: {convert_from_decimal(result, base)}")
    except Exception as e:
        print(f"\tError: {e}")

# Main execution block
if __name__ == "__main__":
    # Prompting user for input
    num1 = input("Enter the first number: ")
    num2 = input("Enter the second number: ")
    operation = input("Enter the operation (+, -, *, /): ")
    
    # Prompt for base
    print("Select base:")
    print("1. Binary")
    print("2. Decimal")
    print("3. Octal")
    print("4. Hexadecimal")
    
    base_choice = input("Enter your choice (1-4): ")
    
    # Convert base choice to integer
    base = int(base_choice)
    
    execute_calculator(num1, num2, operation, base)
