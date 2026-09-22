# Put global test variables here:
consolidate_data_testing = "gb-104, GB-220, gb-104, se-011, GB-220"

#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

def consolidate_data(scanner_data): # Takes a comma separated string and parses its contents.
    str_list = [] # Consolidated in list for ease of export
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

def check_van_cap(): # Prompts user for load limtit and individual parcel weight. Calculates max load & prints wheter a parcel is accepted or rejected.
    tot_parc = 0
    acc_parc = 0
    loaded_weight = 0

    van_cap = input("Van capacity (kg):") # TODO WARNING - Lacks any sanity checks. User data may not be
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

def main():
    consolidate_data(consolidate_data_testing) # Test - May be removed 
    check_van_cap() # Test - May be removed

if __name__ == "__main__": # Namespace func - do not touch!
    main()
