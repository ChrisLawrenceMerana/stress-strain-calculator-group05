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