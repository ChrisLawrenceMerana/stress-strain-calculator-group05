while True:
    try:
        applied=float(input("Enter Applied Force: "))
        cross=float(input("Enter Cross-Sectional Area: "))
        original=float(input("Enter Original Length: "))
        changed=float(input("Enter Changed Length: "))
        
#Input Validation
        if applied>0 and cross>0 and original>0 and changed>0: 
            print("All values valid! Calculating...")
            stress=applied/cross
            strain=original/changed
            print(f'Stress: {stress} Pa, Strain: {strain}')

#Error Handling
        else:
            print("Negative/Null Value detected. Please try again.")
    except ValueError:
        print("Incorrect Value type detected. Please try again.")

#Material Selection
    materials={
                "Steel": {"yield_strength": 250, "youngs_modulus": 200},
                "Aluminum": {"yield_strength": 95, "youngs_modulus": 69},
                "Titanium": {"yield_strength": 880, "youngs_modulus": 114}
            }
    try:
        print("Selection:")
        print("[1] Steel - Yield Strength ~250 MPa, Young's Modulus ~200 GPa")
        print("[2] Aluminum - Yield Strength ~95 Mpa, Young's Modulus ~69 GPa")
        print("[3] Titanium - Yield Strength ~880 MPa, Young's Modulus ~114 GPa")

        select=int(input("Enter a number corresponding to the desired material: "))

        if select==1:
            chosen="Steel"
        elif select==2:
            chosen="Aluminum"
        elif select==3:
            chosen="Titanium"
        else:
            raise KeyError

    except TypeError:
        print("Invalid ")
    