
materials={
            "Steel": {"yield_strength": 250, "youngs_modulus": 200},
            "Aluminum": {"yield_strength": 95, "youngs_modulus": 69},
            "Titanium": {"yield_strength": 880, "youngs_modulus": 114}
        }
#Material selection
def MatSelect():
    """Presents a selection of predetermined materials to select, with the option of creating a custom one if desired.

    Args:
        select: The number corresponding to a material shown in the selection.

    Returns:
        chosen: The final selected material to be used in other calculations
    
    """
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
            raise ValueError("Invalid input!")
        return materials[chosen]
    
    except TypeError, ValueError:
        print('Invalid Input!')
        return

