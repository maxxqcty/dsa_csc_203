import math

def find_primes_in_range(start, end):
    primes = []
    for num in range(start, end + 1):
        if num > 1:
            is_prime = True
            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0:
                    is_prime = False
                    break
            if is_prime:
                primes.append(num)
    return primes

def display_matrix(prime_numbers):
    n = len(prime_numbers)
    # Calculate the size of the matrix
    matrix_size = math.ceil(math.sqrt(n))
    
    # Fill in the matrix with prime numbers and placeholders for extra cells
    matrix = []
    index = 0
    for i in range(matrix_size):
        row = []
        for j in range(matrix_size):
            if index < n:
                row.append(prime_numbers[index])
                index += 1
            else:
                row.append(" ")  # Placeholder for extra cells
        matrix.append(row)
    
    # Display the matrix
    for row in matrix:
        print(" ".join(f"{num:3}" for num in row))


def prime_run():
# Example usage
    start_range = int(input("Enter the start of the range: "))
    end_range = int(input("Enter the end of the range: "))

    prime_numbers = find_primes_in_range(start_range, end_range)
    print("\n Prime numbers:")
    display_matrix(prime_numbers)

if __name__ == "__main__":
    prime_run()

# -----------------------------------------------------------
# OUTPUT :


# Enter the start of the range: 1 
# Enter the end of the range: 100

#  Prime numbers:
#   2   3   5   7  11
#  13  17  19  23  29
#  31  37  41  43  47
#  53  59  61  67  71
#  73  79  83  89  97

