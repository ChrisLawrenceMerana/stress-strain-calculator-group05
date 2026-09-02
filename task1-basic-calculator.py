print("Stress and Strain Calculator")
applied_force = float(input("Enter applied force in Newtons: "))
cross_sectional_area = float(input("Enter cross-sectional area in square meters: "))
original_length = float(input("Enter original length in meters: "))
change_in_length = float(input("Enter change in length in meters: "))

stress = applied_force / cross_sectional_area
strain = change_in_length / original_length
youngs_modulus = stress / strain

print("\n" + "=" * 35)
print("           TEST RESULTS           ")
print("=" * 35)
print(f"Applied Force            : {applied_force:,.2f} N")
print(f"Cross-Sectional Area     : {cross_sectional_area:.6f} m²")
print(f"Original Length          : {original_length:.4f} m")
print(f"Change in Length         : {change_in_length:.6f} m")
print("-" * 35)
print(f"Calculated Stress        : {stress:,.2f} Pa ({stress / 1e6:.2f} MPa)")
print(f"Calculated Strain        : {strain:.6f} (or {strain * 100:.4f}%)")
print(f"Young's Modulus          : {youngs_modulus:,.2f} Pa ({youngs_modulus / 1e9:.2f} GPa)")
print("=" * 35)