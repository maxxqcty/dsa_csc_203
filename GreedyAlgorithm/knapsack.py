class Item:
    def __init__(self, profit, weight, index):
        self.profit = profit
        self.weight = weight
        self.index = index
        self.pw_ratio = profit / weight

def fractional_knapsack(capacity, items):
    # Sort items by profit-to-weight ratio in descending order
    items.sort(key=lambda x: x.pw_ratio, reverse=True)

    total_profit = 0.0
    fractions = [0] * len(items)

    for item in items:
        if capacity == 0:
            break  # No more capacity left in the knapsack

        # If the item can be fully accommodated
        if item.weight <= capacity:
            capacity -= item.weight
            total_profit += item.profit
            fractions[item.index] = 1.0  # Full item is taken
        else:
            # Take the fraction of the remaining item
            fraction = capacity / item.weight
            total_profit += item.profit * fraction
            fractions[item.index] = fraction  # Fraction of the item is taken
            capacity = 0  # Knapsack is now full

    return total_profit, fractions

# Driver code
def run_kp():
    capacity = float(input("Enter the maximum capacity of the knapsack: "))
    n = int(input("Enter the number of items: "))
    items = []

    for i in range(n):
        profit = float(input(f"Profit for item {i + 1}: "))
        weight = float(input(f"Weight for item {i + 1}: "))
        items.append(Item(profit, weight, i))

    # Display item data in table format
    print("\nItems:")
    print("+------+--------+--------+-------------+")
    print("| Item | Profit | Weight | P/W Ratio   |")
    print("+------+--------+--------+-------------+")
    for i in range(n):
        print(f"| {i + 1:<4} | {items[i].profit:<6} | {items[i].weight:<6} | {items[i].pw_ratio:<11.2f} |")
    print("+------+--------+--------+-------------+")

    max_profit, fractions = fractional_knapsack(capacity, items)

    print("\nFractions of items carried in the knapsack:")
    for i in range(n):
        print(f"Item {i + 1}: {fractions[i]:.2f}")  # Print all items, including those with 0.00

    print(f"\nMaximum Profit: {max_profit:.2f}")

if __name__ == "__main__":
    run_kp()
# -----------------------------------------------------------
# OUTPUT :


# Enter the number of items: 10
# Profit for item 1: 5
# Weight for item 1: 3
# Profit for item 2: 10
# Weight for item 2: 4
# Profit for item 3: 15
# Weight for item 3: 4
# Profit for item 4: 7
# Weight for item 4: 2
# Profit for item 5: 8
# Weight for item 5: 3
# Profit for item 6: 9
# Weight for item 6: 1
# Profit for item 7: 4
# Weight for item 7: 2
# Profit for item 8: 8
# Weight for item 8: 5
# Profit for item 9: 9
# Weight for item 9: 7
# Profit for item 10: 20
# Weight for item 10: 5

# Items:
# +------+--------+--------+-------------+
# | Item | Profit | Weight | P/W Ratio   |
# +------+--------+--------+-------------+
# | 1    | 5.0    | 3.0    | 1.67        |
# | 2    | 10.0   | 4.0    | 2.50        |
# | 3    | 15.0   | 4.0    | 3.75        |
# | 4    | 7.0    | 2.0    | 3.50        |
# | 5    | 8.0    | 3.0    | 2.67        |
# | 6    | 9.0    | 1.0    | 9.00        |
# | 7    | 4.0    | 2.0    | 2.00        |
# | 8    | 8.0    | 5.0    | 1.60        |
# | 9    | 9.0    | 7.0    | 1.29        |
# | 10   | 20.0   | 5.0    | 4.00        |
# +------+--------+--------+-------------+

# Fractions of items carried in the knapsack:
# Item 1: 1.00
# Item 2: 1.00
# Item 3: 1.00
# Item 4: 1.00
# Item 5: 1.00
# Item 6: 1.00
# Item 7: 1.00
# Item 8: 0.20
# Item 9: 0.00
# Item 10: 1.00

# Maximum Profit: 79.60

