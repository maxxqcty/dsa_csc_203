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


def euc_run():
    # Ask the user for input
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))

    show_solution(a, b)

if __name__ == "__main__":
    euc_run()
# -----------------------------------------------------------
# OUTPUT : 

# Enter the first number: 1124
# Enter the second number: 238

# Euclidean Algorithm:
# 1124 = 238 * 4 + 172
# 238 = 172 * 1 + 66
# 172 = 66 * 2 + 40
# 66 = 40 * 1 + 26
# 40 = 26 * 1 + 14
# 26 = 14 * 1 + 12
# 14 = 12 * 1 + 2
# 12 = 2 * 6 + 0

# GCD of 1124 and 238 is: 2

