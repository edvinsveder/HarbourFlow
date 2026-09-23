#task: calculate delivery cost depending on the distance, weight and typr of delivery
#types of diliveries: S = Standard, X = Express and P = Priority

#for trail the distance and weight have input
distance = float(input("Distance (km): "))
# Added conditions so that the distance and weight must be above 0
while distance <= 0:
    print("Error - Value must be greater than zero.")
    distance = float(input("Distance (km): "))
weight = float(input("Weight (kg): "))
while weight <= 0:
    print("Error - Value must be greater than zero.")
    weight = float(input("Weight (kg): "))
service_multiplier = 0


print("Type of delivery do you want?")
print("S. Standard  -  0% extra cost")
print("X. Express  -  25% extra cost")
print("P. Priority  -  60% extra cost")

service_code = input("Dilivery type (the letter before type): ")
# Added conditions so that the delivery type must be s, x or p
while service_code.upper() != "S" or service_code.upper() != "X" or service_code.upper() != "P":
    print("Error - Service code must be S, X or P.")
    service_code = input("Dilivery type (the letter before type): ")


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


#below is what i had at start when trying things out
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



def delivery_cost():

    service_multiplier = type_of_delivery(service_code)
        
    subtotal = 45.00 + distance*6.50 + weight*4.00 
    #the distance should be in km and the weight in kg

    quote = subtotal * service_multiplier 

    #printing the quote 

    print(f"Distance (km): {distance:.1f}")
    print(f"Weight (kg): {weight}")
    print(f"Service code: {service_code.upper()}")
    print(f"Delivery quote: {quote:.2f} SEK")

#this runs the functions
type_of_delivery(service_code)
delivery_cost()