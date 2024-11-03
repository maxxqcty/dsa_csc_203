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