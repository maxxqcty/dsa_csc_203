from bit_conversion import convert_to_decimal
from bit_conversion import convert_from_decimal

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


# -----------------------------------------------------------
# OUTPUT :

# Enter the first number: 7456.465
# Enter the second number: 5632.565
# Enter the operation (+, -, *, /): +
# Select base:
# 1. Binary
# 2. Decimal
# 3. Octal
# 4. Hexadecimal
# Enter your choice (1-4): 3
# Result: 15311.252

