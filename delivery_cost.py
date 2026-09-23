# Task: calculate delivery cost depending on the distance, weight and type of delivery
# Types of deliveries: S = Standard, X = Express and P = Priority

# Global vars
distance = float(input("Distance (km): "))
weight = float(input("Weight (kg): "))
service_multiplier = 0

# Run at module start
print("What type of delivery do you want?")
print("S. Standard  -  no extra cost")
print("X. Express   -  25% extra cost")
print("P. Priority  -  60% extra cost")

service_code = input("Select delivery type: ")


def type_of_delivery(service_code):
    
    service_code = service_code.upper()
    if service_code == "S" or service_code == "STANDARD":
        return 1.00
    elif service_code == "X" or service_code == "EXPRESS":
        return 1.25
    elif service_code == "P" or service_code == "PRIORITY":
        return 1.60
    else:
        print("Invalid delivery type - Try Again")
        new_service_code = input("Delivery type (the letter before type): ")
        return type_of_delivery(new_service_code)

def delivery_cost():

    service_multiplier = type_of_delivery(service_code)

    # Distance should be in km and weight in kg.
    subtotal = 45.00 + distance*6.50 + weight*4.00 
    quote = subtotal * service_multiplier 

    # Printing quote 
    print(f"Distance (km): {distance:.1f}")
    print(f"Weight (kg): {weight}")
    print(f"Service code: {service_code.upper()}")
    print(f"Delivery quote: {quote:.2f} SEK")

# This runs the functions:
type_of_delivery(service_code)
delivery_cost()


# Legacy code from development
"""
    if service_code == "S" or "STANDARD":
        service_multiplier = 1.00
    elif service_code == "X" or "EXPRESS":
        service_multiplier = 1.25
    elif service_code == "P" or "PRIORITY":
        service_multiplier = 1.60
    else:
        print("Invalid deliverty type  -  Try Again")
        service_code = input("Dilivery type (the letter before type): ")
        type_of_delivery(service_code)
"""

