def activitySelection(activities):
    # Sort activities by their end times
    activities.sort(key=lambda x: x[1])

    # Select the first activity
    selected_activities = [activities[0]]
    last_end_time = activities[0][1]

    # Iterate over the sorted activities and select if they don't overlap
    for i in range(1, len(activities)):
        if activities[i][0] >= last_end_time:
            selected_activities.append(activities[i])
            last_end_time = activities[i][1]

    # Display result
    print("\nSelected Activities for Maximum Number:")
    print("+-----------+-----------+-----------+")
    print("| Activity  | Start     | End       |")
    print("+-----------+-----------+-----------+")
    for i, activity in enumerate(selected_activities):
        print(f"| {i + 1:<9} | {activity[0]:<9} | {activity[1]:<9} |")
    print("+-----------+-----------+-----------+")

# Input data from user
def run_act():
    n = int(input("Enter the number of activities: "))
    activities = []
    
    for i in range(n):
        start = int(input(f"Start time for Activity {i + 1}: "))
        end = int(input(f"End time for Activity {i + 1}: "))
        activities.append((start, end))
    
    # Display activity data in table format
    print("\nActivity Data:\n")
    print("+-----------+-----------+-----------+")
    print("| Activity  | Start     | End       |")
    print("+-----------+-----------+-----------+")
    for i, activity in enumerate(activities):
        print(f"| {i + 1:<9} | {activity[0]:<9} | {activity[1]:<9} |")
    print("+-----------+-----------+-----------+")
    
    # Function Call
    activitySelection(activities)
    
if __name__ == "__main__":
    run_act()


# -----------------------------------------------------------
# OUTPUT : 

# Enter the number of activities: 12
# Start time for Activity 1: 1
# End time for Activity 1: 4
# Start time for Activity 2: 3
# End time for Activity 2: 5
# Start time for Activity 3: 1
# End time for Activity 3: 6
# Start time for Activity 4: 2
# End time for Activity 4: 7
# Start time for Activity 5: 3
# End time for Activity 5: 8
# Start time for Activity 6: 5
# End time for Activity 6: 9
# Start time for Activity 7: 6
# End time for Activity 7: 9
# Start time for Activity 8: 7
# End time for Activity 8: 10
# Start time for Activity 9: 8
# End time for Activity 9: 11
# Start time for Activity 10: 7
# End time for Activity 10: 12
# Start time for Activity 11: 12
# End time for Activity 11: 14
# Start time for Activity 12: 12
# End time for Activity 12: 16

# Activity Data:

# +-----------+-----------+-----------+
# | Activity  | Start     | End       |
# +-----------+-----------+-----------+
# | 1         | 1         | 4         |
# | 2         | 3         | 5         |
# | 3         | 1         | 6         |
# | 4         | 2         | 7         |
# | 5         | 3         | 8         |
# | 6         | 5         | 9         |
# | 7         | 6         | 9         |
# | 8         | 7         | 10        |
# | 9         | 8         | 11        |
# | 10        | 7         | 12        |
# | 11        | 12        | 14        |
# | 12        | 12        | 16        |
# +-----------+-----------+-----------+

# Selected Activities for Maximum Number:
# +-----------+-----------+-----------+
# | Activity  | Start     | End       |
# +-----------+-----------+-----------+
# | 1         | 1         | 4         |
# | 2         | 5         | 9         |
# | 3         | 12        | 14        |
# +-----------+-----------+-----------+

