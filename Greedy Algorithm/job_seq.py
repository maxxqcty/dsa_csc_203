def printJobScheduling(arr, t):
    n = len(arr)
    
    # Sort all jobs by profit in descending order
    arr.sort(key=lambda x: x[2], reverse=True)

    # Track free time slots
    result = [False] * t
    job_sequence = ['-'] * t
    total_profit = 0

    # Schedule jobs for max profit
    for i in range(len(arr)):
        for j in range(min(t - 1, arr[i][1] - 1), -1, -1):
            if not result[j]:  # Check for free slot
                result[j] = True
                job_sequence[j] = arr[i][0]
                total_profit += arr[i][2]  # Add profit of scheduled job
                break

    # Display job sequence and maximum profit
    print("\nJob Sequence for Maximum Profit:")
    print("+-----+-----+-----+")
    print("| " + "   ".join(job_sequence) + "  |")
    print("+-----+-----+-----+")
    print(f"Maximum Profit: {total_profit}")


# Input data from user
if __name__ == '__main__':
    n = int(input("Enter the number of jobs: "))
    jobs = []
    
    for i in range(n):
        deadline = int(input(f"Deadline for J{i + 1}: "))
        profit = int(input(f"Profit for J{i + 1}: "))
        jobs.append([f"J{i + 1}", deadline, profit])
    
    # Display job data in table format
    print("\nJob Data:\n")
    print("+-----------+-----------+-----------+")
    print("| Job       | Deadline  | Profit    |")
    print("+-----------+-----------+-----------+")
    for job in jobs:
        print(f"| {job[0]:<9} | {job[1]:<9} | {job[2]:<9} |")
    print("+-----------+-----------+-----------+")
    
    # Define max time slots as maximum deadline
    max_time_slots = max(job[1] for job in jobs)

    # Function Call
    printJobScheduling(jobs, max_time_slots)