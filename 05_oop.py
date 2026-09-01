from dataclasses import dataclass
from typing import Optional, List

# 1. Base Materials Class and Properties

@dataclass
class MaterialProperties:
    """Properties of a material."""

    density: float  # kg/m³
    yield_strength: float  # MPa
    typical_youngs_modulus: float  # GPa

    def __post_init__(self):
        """Validate properties."""
        if self.density <= 0:
            raise ValueError("Density must be positive")
        if self.yield_strength <= 0:
            raise ValueError("Yield strength must be positive")
        if self.typical_youngs_modulus <= 0:
            raise ValueError("Young's modulus must be positive")


class Material:
    """Base class for all materials."""

    def __init__(self, name: str, properties: MaterialProperties):
        self.name = name
        self.properties = properties

    def __str__(self) -> str:
        return f"{self.name} (Density: {self.properties.density} kg/m³)"

    def can_withstand_stress(self, stress: float) -> bool:
        """Check if the material can withstand the given stress."""
        # Convert GPa to MPa for comparison
        return stress < self.properties.yield_strength

# 2. Specialized Material Subclasses

class Metal(Material):
    """Subclass for metal materials."""
    def __init__(
        self,
        name: str,
        properties: MaterialProperties,
        is_ferrous: bool = False,
        ductility_pct: float = 0.0,
    ):
        super().__init__(name, properties)
        if ductility_pct < 0:
            raise ValueError("Ductility percentage must be non-negative")
        self.is_ferrous = is_ferrous
        self.ductility_pct = ductility_pct

    def __str__(self) -> str:
        """Extends string format to display ferrous status and ductility."""
        ferrous_text = "Ferrous" if self.is_ferrous else "Non-ferrous"
        return (
            f"{self.name} ({ferrous_text} metal, "
            f"Density: {self.properties.density} kg/m³, "
            f"Ductility: {self.ductility_pct}%)"
        )

class Plastic(Material):
    """Subclass for plastic materials."""
    def __init__(
        self,
        name: str,
        properties: MaterialProperties,
        glass_transition_temp: Optional[float] = None, #Temperature (°C) where polymer becomes rubbery.
    ):
        super().__init__(name, properties)
        self.glass_transition_temp = glass_transition_temp

    def __str__(self) -> str:
        """Extends string format to display glass transition temperature."""
        return f"{self.name} (Polymer, Tg: {self.glass_transition_temp}°C, Density: {self.properties.density} kg/m³)"

class Composite(Material):
    """Subclass for composite materials."""

    def __init__(
        self,
        name: str,
        properties: MaterialProperties,
        reinforcement_type: str, #Type of reinforcement (e.g., Carbon Fiber, Woven Glass, etc.)
    ):
        super().__init__ ( name, properties)
        self.reinforcement_type = reinforcement_type

    def __str__ (self) -> str:
        """Extends string format to display reinforcement type."""
        return f"{self.name} (Composite [{self.reinforcement_type}], Density: {self.properties.density} kg/m³)"

#3. Stress-Strain Test Class

class StressStrainTest:
    """A single stress-strain test."""

    def __init__(
        self,
        material: Material,
        force: float,
        area: float,
        original_length: float,
        change_in_length: float,
    ):

        # Validate inputs
        if force <= 0:
            raise ValueError("Force must be positive")
        if area <= 0:
            raise ValueError("Area must be positive")
        if original_length <= 0:
            raise ValueError("Original length must be positive")
        # Change in length can be negative (compression)

        self.material = material
        self._force = force
        self._area = area
        self._original_length = original_length
        self._change_in_length = change_in_length

    @property
    def stress(self) -> float:
        """Calculate stress in MPa."""
        return self._force / self._area

    @property
    def strain(self) -> float:
        """Calculate strain (dimensionless)."""
        return self._change_in_length / self._original_length

    @property
    def youngs_modulus(self) -> float:
        """Calculate Young's modulus in GPa."""
        # Convert to GPa from MPa
        return (self.stress / self.strain) / 1000

    @property
    def safety_factor(self) -> float:
        """Calculate the safety factor."""
        return self.material.properties.yield_strength / self.stress

    def will_fail(self) -> bool:
        """Determine if the material is likely to fail under this test."""
        return not self.material.can_withstand_stress(self.stress)

    def modulus_deviation_pct(self) -> float:
        """Calculate the relative discrepancy (%) between the theoretical and measured stiffness."""
        expected = self.material.properties.typical_youngs_modulus
        return abs(self.youngs_modulus - expected) / expected * 100

    def __str__(self) -> str:
        return (
            f"Test on {self.material.name}: "
            f"Stress={self.stress:.2f} MPa, "
            f"Strain={self.strain:.6f}, "
            f"Young's Modulus={self.youngs_modulus:.2f} GPa"
        )

# 4. Material Analysis and Table

class MaterialAnalysisSystem:
    """Combines multiple test records to analyze material performance."""

    def __init__ (self, tests: Optional[List[StressStrainTest]] = None):
        self.tests: List[StressStrainTest] = tests or []

    def add_test(self, test: StressStrainTest) -> None:
        self.tests.append(test)

    def generate_summary_report(self) -> str: 
        if not self.tests:
            return "No test records found."

        headers = [
            "Materal Name",
            "Class",
            "Stress (MPa)",
            "Strain",
            "Test E (GPa)",
            "Nom. E (GPa)",
            "Safety Factor",
            "Status",
        ]

        row_fmt = "{:<16} {:<12} {:<13.2f} {:<10.4f} {:<13.2f} {:<13.2f} {:<14.2f} {:<8}"
        width = 100

        lines = [
            "=" * width,
            "Material Analysis Summary Report".center(width),
            "=" * width,
            "{:<16}{:<12}{:<13}{:<10}{:<13}{:<13}{:<14}{:<8}".format(*headers),
            "-" * width,
        ]

        for t in self.tests:
            status = "FAIL" if t.will_fail() else "PASS"
            lines.append(
                row_fmt.format(
                    t.material.name,
                    t.material.__class__.__name__,
                    t.stress,
                    t.strain,
                    t.youngs_modulus,
                    t.material.properties.typical_youngs_modulus,
                    t.safety_factor,
                    status
                )
            )

        lines.append("=" * width)
        return "\n".join(lines)

#Demonstration

if __name__ == "__main__":
    steel_props = MaterialProperties(7850, 250, 200)
    abs_props = MaterialProperties(1040, 40, 2.3)
    cfrp_props = MaterialProperties(1600, 600, 135)

    steel = Metal('Steel', steel_props, True, 22.0)
    plastic = Plastic('Plastic', abs_props, 105.0)
    composite = Composite('Carbon Fiber', cfrp_props, 'Carbon Fiber')

    test_steel = StressStrainTest(steel, 5000, 25, 100, 0.10)
    test_plastic = StressStrainTest(plastic, 1200, 25, 100, 2.08)
    test_composite = StressStrainTest(composite, 10000, 25, 100, 0.30)

    analyzer = MaterialAnalysisSystem([test_steel, test_plastic, test_composite])
    print(analyzer.generate_summary_report())
