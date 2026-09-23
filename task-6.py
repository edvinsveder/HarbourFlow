#this task is used to know is the delivery was on time or delayed, and did anything go wrong with the parcel?



def delay_calculation():

    promised = int(input("Promised minutes: "))
    actual = int(input("Actual minutes: "))
    damaged_parcels = int(input("Amount of damaged parcels: "))
    delay = actual - promised      #time of arival

    if damaged_parcels > 0:
        service_status = "SERVICE FAILED"

    else: 
        if delay <= 0:
            service_status = "ON TIME"
        elif delay <= 15:
            service_status = "MINOR DELAY"
        else: service_status = "MAYJOR DELAY"

    print(f"Delay: {delay} minutes")
    print(f"Service status: {service_status}")

delay_calculation()
