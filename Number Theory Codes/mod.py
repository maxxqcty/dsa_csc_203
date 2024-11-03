def calculate_mod(expression, mod_value):
    try:
        # Evaluate the expression
        result = eval(expression)
        
        # Calculate the modulus
        mod_result = result % mod_value
        
        return mod_result
    except Exception as e:
        return f"Error: {str(e)}"

# Input from the user
user_expression = input("Enter an arithmetic expression: ")
mod_value = int(input("Enter the modulus value: "))

# Calculate the modulus of the expression
mod_result = calculate_mod(user_expression, mod_value)

# Output the result
print(f"The result of '{user_expression} mod {mod_value}' is: {mod_result}")