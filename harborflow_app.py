import calc_quote, weekly_report


# Task 1 - Menu
def menu():
    print("HARBORFLOW DISPATCH CONSOLE")
    print("1. Close console")
    print("2. Validate booking reference")
    print("3. Calculate delivery quote")
    print("4. Consolidate parcel labels")
    print("5. Check van capacity")
    print("6. Classify service performance")
    print("7. Produce weekly dispatch report")
    print("8. Compare service scenarios")

    # Make sure the choice is an integer between 1 and 8
    choice = input("Select service: ")
    while choice.isdigit() is False or int(choice) < 1 or int(choice) > 8:
        print("Error - Select a service from 1 to 8.")
        choice = input("Select service: ")

    return int(choice)


# Task 2 - Validate booking reference
def validate_reference(text):
    text = text.strip().upper()

    # Check the length and that the hyphens are in the correct places
    if len(text) != 12 or text[3] != "-" or text[7] != "-":
        return ""

    # Split the reference into its parts and check each one
    fixed = text[0:3]
    customer_code = text[4:7]
    shipment_number = text[8:12]
    if fixed != "HFL" or customer_code.isalpha() is False or shipment_number.isdigit() is False:
        return ""

    return text


def run_reference_check():
    # validate_reference returns an empty string if the reference is invalid
    reference = input("Booking reference: ")
    output = validate_reference(reference)
    if output == "":
        print("Invalid booking reference.")
    else:
        print(f"Valid reference: {output}")


# Task 3 - Calculate delivery quote
# (see calc_quote.py)

# Task 4 - Consolidate parcel labels
def consolidate_data(scanner_data):
    # Takes a comma separated string and prints each unique label on its own line
    str_list = []
    obj_count = 0

    print("Unique load list:")

    for item in scanner_data.split(","):
        str_temp = item.strip().upper()
        if str_temp in str_list:  # Skip labels that have already been scanned
            continue
        str_list.append(str_temp)
        obj_count += 1
        print(f"{obj_count}. {str_temp}")

    print(f"Total unique parcels: {obj_count}")


# Task 5 - Check van capacity
def check_van_cap():
    # Asks for the van capacity and parcel weights, then accepts or rejects each parcel
    tot_parc = 0
    acc_parc = 0
    loaded_weight = 0

    van_cap = float(input("Van capacity (kg):"))  # TODO: Add sanity checks
    remaining_cap = van_cap

    parcel_weights = input("Parcel weights (kg):")  # TODO: Add sanity checks

    for item in parcel_weights.split(","):
        tot_parc += 1
        float_temp = float(item.strip())

        if float_temp <= remaining_cap:
            acc_parc += 1
            loaded_weight += float_temp
            print(f"Parcel {tot_parc}: ACCEPTED")
            remaining_cap = van_cap - loaded_weight
        else:
            print(f"Parcel {tot_parc}: REJECTED")

    print(f"Accepted parcels: {acc_parc}")
    print(f"Loaded weight: {loaded_weight:.2f} kg")
    print(f"Remaining capacity: {remaining_cap:.2f} kg")


# Task 6 - Classify service performance
def delay_calculation():
    promised = int(input("Promised minutes: "))
    actual = int(input("Actual minutes: "))
    damaged_parcels = int(input("Amount of damaged parcels: "))
    delay = actual - promised

    if damaged_parcels > 0:
        service_status = "SERVICE FAILED"
    elif delay <= 0:
        service_status = "ON TIME"
    elif delay <= 15:
        service_status = "MINOR DELAY"
    else:
        service_status = "MAJOR DELAY"

    print(f"Delay: {delay} minutes")
    print(f"Service status: {service_status}")


# Task 7 - Produce weekly dispatch report (see weekly_report.py)


# Task 8 - Make the console resilient


# Task 9 - Compare delivery scenarios
def comparing_delivery_scenarios():
    # Reuses the input validation from task 3
    dist = calc_quote.ask_positive_number("Distance (km): ")
    wei = calc_quote.ask_positive_number("Weight (kg): ")

    # Prices for each delivery type, in the same order as service_codes
    all_options = [
        calc_quote.delivery_cost("S", distance=dist, weight=wei),
        calc_quote.delivery_cost("X", distance=dist, weight=wei),
        calc_quote.delivery_cost("P", distance=dist, weight=wei),
    ]
    service_codes = ["Standard", "Express", "Priority"]

    print()
    print("Service comparison")
    print(f"Standard: {all_options[0]:.2f} SEK")
    print(f"Express: {all_options[1]:.2f} SEK")
    print(f"Priority: {all_options[2]:.2f} SEK")

    # Find the cheapest and most expensive options
    cheapest = all_options[0]
    for n in all_options[1:]:
        if n < cheapest:
            cheapest = n
    expensive = all_options[0]
    for n in all_options[1:]:
        if n > expensive:
            expensive = n

    # Print the delivery type at the same index as the price
    print(f"Cheapest service: {service_codes[all_options.index(cheapest)]}")
    print(f"Most expensive service: {service_codes[all_options.index(expensive)]}")
    print()


def main():
    running = True
    while running:
        service = menu()
        match service:
            case 1:
                running = False
            case 2:
                run_reference_check()
            case 3:
                calc_quote.run_task3()
            case 4:
                consolidate_data(input("Scanned labels: "))
            case 5:
                check_van_cap()
            case 6:
                delay_calculation()
            case 7:
                weekly_report.run_weekly_report()
            case 8:
                comparing_delivery_scenarios()

    print("Console closed. Dispatch data remains safe.")


# Only start the console when this file is run directly
if __name__ == "__main__":
    main()
