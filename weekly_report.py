def weekly_dispatch_report():

    total_deliveries = 0 # Accumulator for the "total deliveries" part of the branch.
    met_target = 0 # Accumulator for the "days meeting target" part of the branch.
    weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"] 


    completed_deliveries_input = input("Completed deliveries: ") # User-input in the form "x, y, z"
    completed_deliveries_str = completed_deliveries_input.split(", ") # Converts the user-input into a set of strings, cuts out the comma and spaces
    while len(completed_deliveries_str) != 7:
        print("Error - Weekly report requires 7 delivery counts.")
        completed_deliveries_input = input("Completed deliveries: ")
        completed_deliveries_str = completed_deliveries_input.split(", ")
    completed_deliveries = [int(x) for x in completed_deliveries_str] # Converts the strings in the set into integers

    # Checking to make sure all delivery values are greater than 0
    for x in completed_deliveries:
        if x < 0:
            return True

# Calculates the day of which the highest recorded delivery was made
    highest_day = completed_deliveries[0]
    for n in completed_deliveries[1:]:
        if n > highest_day:
            highest_day = n

# Calculates the day of which the lowest recorded delivery was made
    lowest_day = completed_deliveries[0]
    for n in completed_deliveries[1:]:
        if n < lowest_day:
            lowest_day = n

# Calculates the total deliveries
    for n in completed_deliveries[0:]:
        total_deliveries += n

# Calculates wether or not each specific day met the daily target and saves it in variable
    for n in completed_deliveries[0:]:
        if n >= 50:
            met_target += 1

# Calculates the average deliveries per day
    average = total_deliveries / 7


    print()
    print("Daily target: 50")
    print("Weekly dispatch report")
    print(f"Total deliveries: {total_deliveries}")
    print(f"Average per day: {average:.2f}")

    # Index not allowed? Will re-visit
    print(f"Highest day: {weekdays[completed_deliveries.index(highest_day)]} ({highest_day})")
    print(f"Lowest day: {weekdays[completed_deliveries.index(lowest_day)]} ({lowest_day})")
    print(f"Days meeting target: {met_target}")
    print()

while weekly_dispatch_report():
    print("Error - Weekly report values cannot be negative.")