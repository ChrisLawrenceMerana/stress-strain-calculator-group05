from typing import List, Optional
from material import Material

def calculate_stress(force: float, area: float) -> float:
    """Calculates engineering stress in Pascals (Pa)."""
    return force / area

def calculate_strain(change_in_length: float, original_length: float) -> float:
    """Calculates engineering strain (dimensionless)."""
    return change_in_length / original_length


def calculate_youngs_modulus(stress: float, strain: float) -> float:
    """Calculates Young's Modulus in Pascals (Pa), avoiding division by zero."""
    if strain == 0:
        return 0.0
    return stress / strain


def calculate_factor_of_safety(yield_strength: float, stress: float) -> float:
    """Calculates Factor of Safety against yield strength."""
    if stress == 0:
        return 0.0
    return yield_strength / stress
