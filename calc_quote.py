# Task 3: Calculate the delivery cost based on distance, weight and delivery type.
# Delivery types: S = Standard, X = Express, P = Priority


def run_task3():
    distance = ask_positive_number("Distance (km): ")
    weight = ask_positive_number("Weight (kg): ")

    print()
    print("Available delivery options:")
    print("S. Standard  -  No extra cost")
    print("X. Express   -  25% extra cost")
    print("P. Priority  -  60% extra cost")
    service_code = input("Option: ").upper()

    while service_code not in ("S", "X", "P"):
        print("Error - Service code must be S, X or P.")
        service_code = input("Option: ").upper()

    # Print the final result
    print()
    print(f"Distance (km): {distance:.1f}")
    print(f"Weight (kg): {weight:.1f}")
    print(f"Service code: {service_code}")
    print(f"Delivery quote: {delivery_cost(service_code, distance, weight):.2f} SEK")


def ask_positive_number(prompt):
    # Keeps asking until the user enters a number greater than zero
    while True:
        try:
            value = float(input(prompt))
        except ValueError:
            print("Error - Value must be a number.")
            continue
        if value <= 0:
            print("Error - Value must be greater than zero.")
            continue
        return value


def delivery_type(service_code):
    # Returns the price multiplier for the given delivery type
    if service_code == "S":
        return 1.00
    elif service_code == "X":
        return 1.25
    elif service_code == "P":
        return 1.60
    raise ValueError(f"Unknown service code: {service_code}")


def delivery_cost(service_code, distance, weight):
    # Distance is in km and weight is in kg
    service_multiplier = delivery_type(service_code)
    subtotal = 45.00 + distance * 6.50 + weight * 4.00
    return subtotal * service_multiplier
