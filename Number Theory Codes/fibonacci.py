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

# Test the function
n = int(input("Enter a positive integer for n: "))
result = fibonacci(n)
print(f"fib({n}) =", result)