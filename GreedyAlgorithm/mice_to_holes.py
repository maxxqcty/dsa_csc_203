from prettytable import PrettyTable

def mice_to_holes(mice, holes):
    # Sort both the mice and holes lists to minimize the maximum distance traveled
    mice.sort()
    holes.sort()
    
    # Create a table for displaying the results
    table = PrettyTable()
    table.field_names = ["Mouse Position", "Hole Position", "Distance Traveled"]
    
    # Calculate the distance each mouse has to travel and fill the table
    max_distance = 0
    for i in range(len(mice)):
        distance = abs(mice[i] - holes[i])
        table.add_row([mice[i], holes[i], distance])
        max_distance = max(max_distance, distance)
    
    # Display the table
    print(table)
    
    return max_distance

# Main function to interact with the user
def run_mh():
    # Ask the user for the number of mice and holes
    n = int(input("Enter the number of mice and holes: "))
    
    # Ask the user to input the positions of the mice
    mice_input = input(f"Enter the positions of {n} mice (comma-separated): ")
    mice = list(map(int, mice_input.split(',')))  # Convert input string into a list of integers
    
    # Ask the user to input the positions of the holes
    holes_input = input(f"Enter the positions of {n} holes (comma-separated): ")
    holes = list(map(int, holes_input.split(',')))  # Convert input string into a list of integers
    
    # Call the function to solve the problem
    result = mice_to_holes(mice, holes)
    
    # Display the result
    print(f"The minimum maximum distance any mouse has to travel is: {result}")

# Run the program
if __name__ == "__main__":
    run_mh()




# -----------------------------------------------------------
# OUTPUT: 

# Enter the number of mice and holes: 5     
# Enter the positions of 5 mice (comma-separated): 10,34,23,45,21
# Enter the positions of 5 holes (comma-separated): 78,98,45,32,34
# +----------------+---------------+-------------------+
# | Mouse Position | Hole Position | Distance Traveled |
# +----------------+---------------+-------------------+
# |       10       |       32      |         22        |
# |       21       |       34      |         13        |
# |       23       |       45      |         22        |
# |       34       |       78      |         44        |
# |       45       |       98      |         53        |
# +----------------+---------------+-------------------+
# The minimum maximum distance any mouse has to travel is: 53