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
if __name__ == '__main__':
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
