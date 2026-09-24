# Put global test variables here:
consolidate_data_testing = "gb-104, GB-220, gb-104, se-011, GB-220"
import task3
#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


# Task 1, menu
def menu():  # To chose which of the services
    # Print looks bad when run, will fix
    print('''HARBORFLOW DISPATCH CONSOLE
    1. Close console
    2. Validate booking reference
    3. Calculate delivery quote
    4. Consolidate parcel labels
    5. Check van capacity
    6. Classify service performance
    7. Produce weekly dispatch report
    8. Compare service scenarios''')

    choice = input("Select service: ")
    while choice.isdigit() is False or int(choice) < 1 or int(choice) > 8:  # To make sure the choice is always an integer and within 1-7
        choice = input("Invalid input, please chooise between 1-8: ")

    return int(choice)


# Task 2, validate reference
def validate_reference(text):
    text = text.strip().upper()  # Normalizing the text
    if len(text) != 12 or text[3] != "-" or text[7] != "-": # Checking its the right length and has hyphens in correct spot
        return ""

    # Dividing the text up in parts and checking to make sure those are correct
    fixed = text[0:3]
    customer_code = text[4:7]
    shipment_number = text[8:12]
    # Hope we're allowed to use isalpha and isdigit
    if fixed != "HFL" or customer_code.isalpha() is False or shipment_number.isdigit() is False:
        return ""

    return text


# Task 4, consolidate data
def consolidate_data(scanner_data):  # Takes a comma separated string and parses its contents.
    str_list = []  # Consolidated in list for ease of export
    obj_count = 0

    print(f"Scanned labels: {scanner_data}")
    print("Unique load list:")

    for item in scanner_data.split(","):  # Separate by comma, strip whitespace, add content to list of obj
        str_temp = item.strip().upper()
        str_list.append(str_temp)
        obj_count += 1
        print(f"{obj_count}. {str_temp}")

    print(f"Total unique parcels: {obj_count}")
    return


# Task 5, checking van capacity
def check_van_cap():  # Prompts user for load limtit and individual parcel weight. Calculates max load & prints wheter a parcel is accepted or rejected.
    tot_parc = 0
    acc_parc = 0
    loaded_weight = 0

    van_cap = input("Van capacity (kg):") # TODO WARNING - Lacks any sanity checks. 
    van_cap = float(van_cap)
    remaining_cap = van_cap

    parcel_weights = input("Parcel weights (kg):") # TODO WARNING - Lacks any sanity checks

    for item in parcel_weights.split(","):  # Separate by comma, strip whitespace, add content to list of obj
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
    return


# Task 9, Comparing delivery scenarios
def comparing_delivery_scenarios():

    dist = float(input("Distance (km): "))
    wei = float(input("Weight (kg): "))

    from task3 import delivery_cost # Imports function from task3 that calculates prices.

    print()
    print("Service comparison")
    print(f"Standard: {delivery_cost("S", distance = dist, weight = wei)}") # Calculates price for Standard delivery
    print(f"Express: {delivery_cost("X", distance = dist, weight = wei)}") # Calculates price for Express delivery
    print(f"Priority: {delivery_cost("P", distance = dist, weight = wei)}") # Calculates price for Priority delivery

    # The set of prices for each delivery type
    all_options = [delivery_cost("S", distance = dist, weight = wei), delivery_cost("X", distance = dist, weight = wei), delivery_cost("P", distance = dist, weight = wei)]
    service_codes = ["Standard", "Express", "Priority"]

    # Calculates cheapest and most expensive options
    cheapest = all_options[0]
    for n in all_options[1:]:
        if n < cheapest:
            cheapest = n
    expensive = all_options[0]
    for n in all_options[1:]:
        if n > expensive:
            expensive = n

    print(f"Cheapest service: {service_codes[all_options.index(cheapest)]}") # Finds the index for cheapest price in all_options and prints corresponding delivery type at that same index
    print(f"Most expensive service: {service_codes[all_options.index(expensive)]}") # - II -
    print()
    return


def main():
    while True:
        service = menu()

        # Calls on the function of the service choice, breaks loop if 1 is chosen
        # Unsure if we said not to use break or not, can do something else if thats the case
        if service == 1:
            break
        elif service == 2:
            reference = input("Booking reference: ")
            output = validate_reference(reference)

            # I know this is stupid but assignment said to return as empty string if invalid
            if output == "":
                print("Invalid reference")
            else:
                print(f"Valid reference: {output}")
        elif service == 3:
            task3.run_task3() # Runs task 3
            # Function for task 3
        elif service == 4:
            pass
            # consolidate_data(consolidate_data_testing) # Test - May be removed 
            # Function for task 4
        elif service == 5:
            pass
            # check_van_cap() # Test - May be removed
            # Function for task 5
        elif service == 6:
            pass
            # Function for task 6
        elif service == 7:
            import weekly_report # Test - May be changed or removed.
            # Function for task 7
        else:
            comparing_delivery_scenarios() # - Test, may be removed or changed
            # Function for task 9, menu option 8

    print("Console closed. Dispatch data remains safe.")


if __name__ == "__main__":  # Namespace func - do not touch!
    main()
