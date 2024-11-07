def fibonacci(n, memo={}):
    if n <= 0:
        return "Input should be a positive integer."
    elif n in memo:
        return memo[n]
    elif n == 1 or n == 2:
        memo[n] = 1
        return 1
    else:
        result = fibonacci(n-1, memo) + fibonacci(n-2, memo)
        memo[n] = result
        print(f"fib({n}) = fib({n-1}) + fib({n-2}) = {result}")
        return result



def fib_run():
    # Test the function
    n = int(input("Enter a positive integer for n: "))
    result = fibonacci(n)
    print(f"fib({n}) =", result)

if __name__ == "__main__":
    fib_run()
# -----------------------------------------------------------
# OUTPUT :

# Enter a positive integer for n: 20
# fib(3) = fib(2) + fib(1) = 2
# fib(4) = fib(3) + fib(2) = 3
# fib(5) = fib(4) + fib(3) = 5
# fib(6) = fib(5) + fib(4) = 8
# fib(7) = fib(6) + fib(5) = 13
# fib(8) = fib(7) + fib(6) = 21
# fib(9) = fib(8) + fib(7) = 34
# fib(10) = fib(9) + fib(8) = 55
# fib(11) = fib(10) + fib(9) = 89
# fib(12) = fib(11) + fib(10) = 144
# fib(13) = fib(12) + fib(11) = 233
# fib(14) = fib(13) + fib(12) = 377
# fib(15) = fib(14) + fib(13) = 610
# fib(16) = fib(15) + fib(14) = 987
# fib(17) = fib(16) + fib(15) = 1597
# fib(18) = fib(17) + fib(16) = 2584
# fib(19) = fib(18) + fib(17) = 4181
# fib(20) = fib(19) + fib(18) = 6765
# fib(20) = 6765

