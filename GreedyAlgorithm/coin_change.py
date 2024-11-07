def coin_change(coins, amount):
    # Initialize dp array with a large number (greater than the maximum possible number of coins)
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0  # Base case: 0 amount requires 0 coins
    
    # Iterate over each coin
    for coin in coins:
        # Update the dp array for amounts that can be reached by adding this coin
        for i in range(coin, amount + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)
    
    # If dp[amount] is still infinity, it means no solution exists
    if dp[amount] == float('inf'):
        return -1
    return dp[amount]

# Main function to interact with the user
def run_coin():
    # Ask the user to input the coin denominations
    coins_input = input("Enter coin denominations (comma-separated): ")
    coins = list(map(int, coins_input.split(',')))  # Convert input string into a list of integers
    
    # Ask the user to input the amount
    amount = int(input("Enter the amount to make change for: "))
    
    # Call the function to solve the problem
    result = coin_change(coins, amount)
    
    # Display the result
    if result == -1:
        print(f"It's not possible to make {amount} with the given coins.")
    else:
        print(f"Minimum coins needed to make {amount}: {result}")

# Run the program
if __name__ == "__main__":
         run_coin()



# -----------------------------------------------------------
# OUTPUT : 

# Enter coin denominations (comma-separated): 1,5,10,20   
# Enter the amount to make change for: 100
# Minimum coins needed to make 100: 5