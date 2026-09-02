print("Stress and Strain Calculator")
applied_force = float(input("Enter applied force in Newtons: "))
cross_sectional_area = float(input("Enter cross-sectional area in square meters: "))
original_length = float(input("Enter original length in meters: "))
change_in_length = float(input("Enter change in length in meters: "))

stress = applied_force / cross_sectional_area
strain = change_in_length / original_length
youngs_modulus = stress / strain