def display_results(force, area, orig_len, change_len, stress, strain, youngs_mod):
    """Formats and displays the engineering test parameters and computed results."""
    print("\n" + "=" * 35)
    print("           TEST RESULTS           ")
    print("=" * 35)
    print(f"Applied Force        : {force:,.2f} N")
    print(f"Cross-Sectional Area : {area:.4f} m²")
    print(f"Original Length      : {orig_len:.2f} m")
    print(f"Change in Length     : {change_len:.4f} m")
    print("-" * 35)
    print(f"Calculated Stress    : {stress:,.2f} Pa ({stress / 1e6:.2f} MPa)")
    print(f"Calculated Strain    : {strain:.4f} (or {strain * 100:.2f}%)")
    print(f"Young's Modulus      : {youngs_mod:,.2f} Pa ({youngs_mod / 1e9:.2f} GPa)")
    print("=" * 35)

print("Stress and Strain Calculator")
applied_force = float(input("Enter applied force in Newtons: "))
cross_sectional_area = float(input("Enter cross-sectional area in square meters: "))
original_length = float(input("Enter original length in meters: "))
change_in_length = float(input("Enter change in length in meters: "))

stress = applied_force / cross_sectional_area
strain = change_in_length / original_length
youngs_modulus = stress / strain

display_results(
    applied_force,
    cross_sectional_area,
    original_length,
    change_in_length,
    stress,
    strain,
    youngs_modulus,
)