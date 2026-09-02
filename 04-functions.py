def get_positive_float(prompt):
    """
    Prompts the user for input and validates that it is a positive number.
    Replaces the basic float(input()) from Task 1 to prevent crashes.
    """
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                print("Error: Value must be greater than zero. Try again.")
            else:
                return value
        except ValueError:
            print("Error: Invalid input. Please enter a number.")

def calculate_stress(force, area):
    """Calculates the stress on a material."""
    return force / area

def calculate_strain(change_in_length, original_length):
    """Calculates the strain on a material."""
    return change_in_length / original_length

def calculate_youngs_modulus(stress, strain):
    """Calculates Young's Modulus, preventing division by zero."""
    if strain == 0:
        return 0.0
    return stress / strain

def calculate_factor_of_safety(yield_strength, stress):
    """Calculates the factor of safety."""
    if stress == 0:
        return 0.0
    return yield_strength / stress

def display_results(force, area, orig_len, change_len, stress, strain, modulus):
    """
    Formats and prints the test results.
    Takes the variables as parameters instead of relying on global variables.
    """
    print("\n" + "=" * 35)
    print("           TEST RESULTS           ")
    print("=" * 35)
    print(f"Applied Force            : {force:,.2f} N")
    print(f"Cross-Sectional Area     : {area:.6f} m²")
    print(f"Original Length          : {orig_len:.4f} m")
    print(f"Change in Length         : {change_len:.6f} m")
    print("-" * 35)
    print(f"Calculated Stress        : {stress:,.2f} Pa ({stress / 1e6:.2f} MPa)")
    print(f"Calculated Strain        : {strain:.6f} (or {strain * 100:.4f}%)")
    print(f"Young's Modulus          : {modulus:,.2f} Pa ({modulus / 1e9:.2f} GPa)")
    print("=" * 35)

def main():
    """Coordinates the inputs, calculations, and outputs."""
    print("Stress and Strain Calculator")

    applied_force = get_positive_float("Enter applied force in Newtons: ")
    cross_sectional_area = get_positive_float("Enter cross-sectional area in square meters: ")
    original_length = get_positive_float("Enter original length in meters: ")
    change_in_length = get_positive_float("Enter change in length in meters: ")

    stress = calculate_stress(applied_force, cross_sectional_area)
    strain = calculate_strain(change_in_length, original_length)
    youngs_modulus = calculate_youngs_modulus(stress, strain)
    
    display_results(
        applied_force, cross_sectional_area, original_length, 
        change_in_length, stress, strain, youngs_modulus
    )

if __name__ == "__main__":
    main()