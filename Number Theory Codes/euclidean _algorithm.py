def euclidean_algorithm(a, b):
    steps = []
    while b != 0:
        quotient = a // b
        remainder = a % b
        steps.append(f"{a} = {b} * {quotient} + {remainder}")
        a, b = b, remainder
    return a, steps

def show_solution(a, b):
    gcd, steps = euclidean_algorithm(a, b)
    print("\nEuclidean Algorithm:")
    for step in steps:
        print(step)
    print(f"\nGCD of {a} and {b} is: {gcd}")

# Ask the user for input
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

show_solution(a, b)