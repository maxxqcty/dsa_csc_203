def prime_factors(n):
    factors = []
    # Divide by 2 until n becomes odd
    while n % 2 == 0:
        factors.append(2)
        n //= 2
    # Check for odd factors from 3 to sqrt(n)
    for i in range(3, int(n**0.5) + 1, 2):
        while n % i == 0:
            factors.append(i)
            n //= i
    # If n is prime and greater than 2
    if n > 2:
        factors.append(n)
    return factors

def gcd(a, b):
    factors_a = prime_factors(a)
    factors_b = prime_factors(b)
    common_factors = set(factors_a) & set(factors_b)
    gcd_value = 1
    for factor in common_factors:
        gcd_value *= factor
    return gcd_value

def lcd(a, b):
    factors_a = prime_factors(a)
    factors_b = prime_factors(b)
    all_factors = set(factors_a + factors_b)
    lcd_value = 1
    for factor in all_factors:
        count_a = factors_a.count(factor)
        count_b = factors_b.count(factor)
        lcd_value *= factor ** max(count_a, count_b)
    return lcd_value

def display_prime_factorization(a, b):
    print(f"Prime factorization of {a}: {prime_factors(a)}")
    print(f"Prime factorization of {b}: {prime_factors(b)}")

# Main function to calculate GCD, LCD and show factorization
def main():
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    
    display_prime_factorization(a, b)
    
    print(f"GCD of {a} and {b}: {gcd(a, b)}")
    print(f"LCD of {a} and {b}: {lcd(a, b)}")

# Run the program
if __name__ == "__main__":
    main()

# -----------------------------------------------------------
#     OUTPUT: 

# Enter the first number: 95
# Enter the second number: 1045
# Prime factorization of 95: [5, 19]
# Prime factorization of 1045: [5, 11, 19]
# GCD of 95 and 1045: 95
# LCD of 95 and 1045: 1045
