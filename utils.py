"""Module that contains reusable calculation and conversion utilities."""

materials = {
    "Steel": {"yield_strength": 250, "youngs_modulus": 200},
    "Aluminum": {"yield_strength": 95, "youngs_modulus": 69},
    "Titanium": {"yield_strength": 880, "youngs_modulus": 114},
}

# Unit Conversions
def pa_to_mpa(pressure_pa: float) -> float:
    """Converts pressure from Pascals (Pa) to Megapascals (MPa)."""
    return pressure_pa / 1e6

def mpa_to_pa(pressure_mpa: float) -> float:
    """Converts pressure from Megapascals (MPa) to Pascals (Pa)."""
    return pressure_mpa * 1e6

def pa_to_gpa(pressure_pa: float) -> float:
    """Converts pressure from Pascals (Pa) to Gigapascals (GPa)."""
    return pressure_pa / 1e9

def gpa_to_pa(pressure_gpa: float) -> float:
    """Converts pressure from Gigapascals (GPa) to Pascals (Pa)."""
    return pressure_gpa * 1e9

# Reusable Calculations
def calculate_stress(force: float, area: float) -> float:
    """Calculates stress in Pa."""
    if area <= 0:
        raise ValueError("Cross-sectional area must be greater than zero.")
    return force / area

def calculate_strain(change_in_length: float, original_length: float) -> float:
    """Calculates engineering strain."""
    if original_length <= 0:
        raise ValueError("Original length must be greater than zero.")
    return change_in_length / original_length

def calculate_youngs_modulus(stress_pa: float, strain: float) -> float:
    """Calculates Young's modulus in Pascals."""
    if strain == 0:
        return 0.0
    return stress_pa / strain

def evaluate_safety_margin(yield_strength_mpa: float, stress_mpa: float) -> tuple[float, str]:
    """Calculates safety factor and operational verdict."""
    if stress_mpa <= 0:
        return float("inf"), "SAFE"

    factor = yield_strength_mpa / stress_mpa
    load_margin = yield_strength_mpa - stress_mpa

    if stress_mpa > yield_strength_mpa:
        verdict = "UNSAFE (Yield Exceeded)"
    elif load_margin <= (yield_strength_mpa * 0.10):
        verdict = "CAUTION"
    else:
        verdict = "SAFE"

    return factor, verdict

# Interactive Handlers
def Loop():
    """Queries the user for test dimensions and loads, returning raw inputs and stress."""
    while True:
        try:
            start = int(
                input(
                    "\nPress 1 to begin calculating, or 2 to exit: "
                )
            )
            if start == 2:
                return None
            elif start != 1:
                print("Invalid input. Please enter 1 or 2.")
                continue

            applied = float(input("Enter Applied Force (N): "))
            cross = float(input("Enter Cross-Sectional Area (m²): "))
            original = float(input("Enter Original Length (m): "))
            changed = float(input("Enter Changed Length (m): "))

            if applied > 0 and cross > 0 and original > 0 and changed > 0:
                stress_pa = calculate_stress(applied, cross)
                stress_mpa = pa_to_mpa(stress_pa)
                strain = calculate_strain(changed, original)
                print(f"Stress: {stress_mpa:.2f} MPa, Strain: {strain:.6f}")
                return applied, cross, original, changed
            else:
                print("Negative/Null Value detected. Please try again.")
        except ValueError:
            print("Incorrect Value type detected. Please try again.")

def MatSelect():
    """Selects or creates a material in the local dictionary."""
    while True:
        try:
            print("\nSelection:")
            print("[1] Steel - Yield Strength ~250 MPa, Young's Modulus ~200 GPa")
            print("[2] Aluminum - Yield Strength ~95 MPa, Young's Modulus ~69 GPa")
            print("[3] Titanium - Yield Strength ~880 MPa, Young's Modulus ~114 GPa")
            print("[4] CUSTOM MATERIAL")

            select = int(input("Enter choice (1-4): "))
            if select == 1:
                return "Steel"
            elif select == 2:
                return "Aluminum"
            elif select == 3:
                return "Titanium"
            elif select == 4:
                chosen = input("Enter the material's name: ").strip().title()
                customstrength = float(input("Enter Yield Strength (MPa): "))
                custommodulus = float(input("Enter Young's Modulus (GPa): "))
                materials[chosen] = {
                    "yield_strength": customstrength,
                    "youngs_modulus": custommodulus,
                }
                return chosen
            else:
                print("Invalid selection. Must be 1 to 4.")
        except (TypeError, ValueError):
            print("Invalid input! Numbers required.")

def SafetyAna(chosen: str, stress_mpa: float):
    """Carries out safety analysis and prints status."""
    if chosen not in materials:
        print(f"Error: Material '{chosen}' not found.")
        return

    ys = materials[chosen]["yield_strength"]
    factor, verdict = evaluate_safety_margin(ys, stress_mpa)

    print("\n" + "=" * 35)
    print("         SAFETY ANALYSIS          ")
    print("=" * 35)
    print(f"Material                 : {chosen}")
    print(f"Applied Stress           : {stress_mpa:.2f} MPa")
    print(f"Yield Strength           : {ys:.2f} MPa")
    print(f"Factor of Safety         : {factor:.2f}")
    print(f"Verdict                  : {verdict}")
    print("=" * 35)