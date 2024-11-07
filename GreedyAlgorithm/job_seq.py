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
def run_job():
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

if __name__ == "__main__":
    run_job()
# -----------------------------------------------------------
# OUTPUT :

# Enter the number of jobs: 7
# Deadline for J1: 3
# Profit for J1: 35
# Deadline for J2: 3
# Profit for J2: 30
# Deadline for J3: 4
# Profit for J3: 25
# Deadline for J4: 4
# Profit for J4: 20
# Deadline for J5: 3
# Profit for J5: 15
# Deadline for J6: 1
# Profit for J6: 12
# Deadline for J7: 2
# Profit for J7: 5

# Job Data:

# +-----------+-----------+-----------+
# | Job       | Deadline  | Profit    |
# +-----------+-----------+-----------+
# | J1        | 3         | 35        |
# | J2        | 3         | 30        |
# | J3        | 4         | 25        |
# | J4        | 4         | 20        |
# | J5        | 3         | 15        |
# | J6        | 1         | 12        |
# | J7        | 2         | 5         |
# +-----------+-----------+-----------+

# Job Sequence for Maximum Profit:
# +-----+-----+-----+-----+
# | J4  | J2  | J1  | J3  |
# +-----+-----+-----+-----+
# Maximum Profit: 110

