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