from fractions import Fraction

def egyptian_fraction(numerator, denominator):
    fraction = Fraction(numerator, denominator)
    result = []
    
    print(f"Starting with fraction: {fraction}")
    
    # Greedy algorithm for Egyptian Fraction
    step = 1
    while fraction.numerator != 1:
        # Calculate the smallest unit fraction greater than or equal to the fraction
        unit_denominator = (fraction.denominator // fraction.numerator) + 1
        unit_fraction = Fraction(1, unit_denominator)
        result.append(unit_fraction)
        
        # Show the step-by-step solution
        print(f"Step {step}: Choose unit fraction 1/{unit_denominator}")
        print(f"Subtracting {unit_fraction} from {fraction}")
        
        # Update the fraction by subtracting the unit fraction
        fraction -= unit_fraction
        
        print(f"Remaining fraction after step {step}: {fraction}\n")
        step += 1
    
    # Append the final fraction
    result.append(fraction)
    print(f"Final step: Choose unit fraction {fraction}")
    
    return result

# Get input from the user
numerator = int(input("Enter the numerator: "))
denominator = int(input("Enter the denominator: "))

# Call the function with user input
egyptian_fractions = egyptian_fraction(numerator, denominator)

# Display the result as a sum
print("\nEgyptian fraction representation:")
print(" + ".join(str(f) for f in egyptian_fractions))


# -----------------------------------------------------------
# OUTPUT :

# Enter the numerator: 13
# Enter the denominator: 89
# Starting with fraction: 13/89
# Step 1: Choose unit fraction 1/7
# Subtracting 1/7 from 13/89
# Remaining fraction after step 1: 2/623

# Step 2: Choose unit fraction 1/312
# Subtracting 1/312 from 2/623
# Remaining fraction after step 2: 1/194376

# Final step: Choose unit fraction 1/194376

# Egyptian fraction representation:
# 1/7 + 1/312 + 1/194376

