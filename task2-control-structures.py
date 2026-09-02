while True:
#Loop
    try:
        start=int(input("Welcome to the Stress and Strain Calculator! Press 1 to begin calculating, and 2 to exit the program! "))
        if start==1:
                pass
        elif start==2:
            break
        else:
            print("Invalid input. Please 1 to continue or 2 to exit.")
            continue

        applied=float(input("Enter Applied Force: "))
        cross=float(input("Enter Cross-Sectional Area: "))
        original=float(input("Enter Original Length: "))
        changed=float(input("Enter Changed Length: "))
        
#Input Validation
        if applied>0 and cross>0 and original>0 and changed>0: 
            print("All values valid! Calculating...")
            stress=(applied/cross)/1000000
            strain=original/changed
            print(f'Stress: {stress} MPa, Strain: {strain}')

#Error Handling
        else:
            print("Negative/Null Value detected. Please try again.")
            continue
    except ValueError:
        print("Incorrect Value type detected. Please try again.")
        continue

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
        print("[4] CUSTOM MATERIAL ")

        select=int(input("Enter a number corresponding to the desired material: "))

        if select==1:
            chosen="Steel"
        elif select==2:
            chosen="Aluminum"
        elif select==3:
            chosen="Titanium"
        elif select==4:
            chosen=input("Enter the material's name: ")
            customstrength=float(input("Enter the material's Yield Strength: "))
            custommodulus=float(input("Enter the material's Young's Modulus"))
            materials[chosen]={"yield_strength": customstrength, "youngs_modulus": custommodulus}
        else:
            raise KeyError

#Safety Analysis
        load=materials[chosen]["yield_strength"]-stress
        factor=materials[chosen]["yield_strength"]/stress
        if load>materials[chosen]["yield_strength"]*0.10:
            load='SAFE'
        elif load<=materials[chosen]["yield_strength"]*0.10:
            load='CAUTION'
        else:
            load='DANGER'
        print(f'{load} - FACTOR OF SAFETY: {factor}')
    except TypeError:
        print("Invalid")

    
    