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


class StressStrainTest:
    """Represents a single stress-strain test execution."""

    def __init__(
        self,
        material: Material,
        force: float,
        area: float,
        original_length: float,
        change_in_length: float,
    ):
        if force <= 0 or area <= 0 or original_length <= 0:
            raise ValueError(
                "Force, area, and original length must be greater than zero."
            )

        self.material = material
        self.force = force
        self.area = area
        self.original_length = original_length
        self.change_in_length = change_in_length

        self.stress = calculate_stress(self.force, self.area)
        self.strain = calculate_strain(
            self.change_in_length, self.original_length
        )
        self.youngs_modulus = calculate_youngs_modulus(self.stress, self.strain)
        self.safety_factor = calculate_factor_of_safety(
            self.material.properties.yield_strength * 1e6, self.stress
        )

    def will_fail(self) -> bool:
        """Determines if test stress exceeds material yield strength."""
        return not self.material.can_withstand_stress(self.stress / 1e6)

    def display_results(self) -> None:
        """Prints formatted test output."""
        print("\n" + "=" * 35)
        print("           TEST RESULTS           ")
        print("=" * 35)
        print(f"Material                 : {self.material.name}")
        print(f"Applied Force            : {self.force:,.2f} N")
        print(f"Cross-Sectional Area     : {self.area:.6f} m²")
        print(f"Original Length          : {self.original_length:.4f} m")
        print(f"Change in Length         : {self.change_in_length:.6f} m")
        print("-" * 35)
        print(
            f"Calculated Stress        : {self.stress:,.2f} Pa ({self.stress / 1e6:.2f} MPa)"
        )
        print(
            f"Calculated Strain        : {self.strain:.6f} (or {self.strain * 100:.4f}%)"
        )
        print(
            f"Young's Modulus          : {self.youngs_modulus:,.2f} Pa ({self.youngs_modulus / 1e9:.2f} GPa)"
        )
        print(f"Safety Factor            : {self.safety_factor:.2f}")
        print("=" * 35)