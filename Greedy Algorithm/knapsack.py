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
if __name__ == '__main__':
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
