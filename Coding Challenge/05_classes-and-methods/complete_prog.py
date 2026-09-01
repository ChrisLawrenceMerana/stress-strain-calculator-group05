from dataclasses import dataclass
from typing import Optional, List


# Material Data and Base Hierarchy

@dataclass
class MaterialProperties:
    """Data-centric container storing fundamental physical constants 
    and baseline mechanical limits for a material."""

    density: float                  # Mass density in kg/m³
    yield_strength: float           # Yield limit in MPa (stress threshold before plastic deformation)
    typical_youngs_modulus: float   # Nominal stiffness (Elastic Modulus) in GPa

    def __post_init__(self):
        """Validate properties if all physical properties are positive"""
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
    """Subclass for metallic alloys, with specific metallurgical attributes."""
    def __init__(
        self,
        name: str,
        properties: MaterialProperties,
        is_ferrous: bool = False,           # True for iron-based metals (steel), False for non-ferrous (aluminum)
        ductility_pct: float = 0.0,         # Percentage elongation before fracture   
    ):
        super().__init__(name, properties)
        if ductility_pct < 0:
            raise ValueError("Ductility percentage must be non-negative")
        self.is_ferrous = is_ferrous
        self.ductility_pct = ductility_pct

    def __str__(self) -> str:
        """Extends string formatting to display ferrous classfication and ductility."""
        ferrous_text = "Ferrous" if self.is_ferrous else "Non-ferrous"
        return (
            f"{self.name} ({ferrous_text} Metal, "
            f"Density: {self.properties.density} kg/m³, "
            f"Ductility: {self.ductility_pct}%)"
        )

class Plastic(Material):
    """
    Subclass for polymer materials, tracking thermal transition thresholds.
    """
    def __init__(
        self,
        name: str,
        properties: MaterialProperties,
        glass_transition_temp: float, #Temperature (C) where polumer transitions from rigid to rubbery
      ):
        super().__init__(name, properties)
        self.glass_transition_temp = glass_transition_temp

    def __str__(self) -> str:
        """
        Extends string formatting to display glass transition temperature.
        """
        return (
            f"{self.name} (Plastic, "
            f"Density: {self.properties.density} kg/m³, "
            f"Glass Transition Temp: {self.glass_transition_temp}°C)"
        )

class Composite(Material):
    """
    Subclass for reinforced matrix materials (carbon fiber, fiberglass)
    """
    def __init__(
        self,
        name: str,
        properties: MaterialProperties,
        reinforcement_type: str, # "Carbon Fiber", "Fiberglass", etc.
    ):
        super().__init__(name, properties)
        self.reinforcement_type = reinforcement_type

    def __str__(self) -> str:
        '''
        Extends string formatting to display reinforcement type.
        '''
        return (
            f"{self.name} (Composite [{self.reinforcement_type}], "
            f"Density: {self.properties.density} kg/m³)"
        )


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
        self.material = material
        self._force = force
        self._area = area
        self._original_length = original_length
        self._change_in_length = change_in_length

        # Validate inputs
        if force <= 0:
            raise ValueError("Force must be positive")
        if area <= 0:
            raise ValueError("Area must be positive")
        if original_length <= 0:
            raise ValueError("Original length must be positive")
        # Change in length can be negative (compression)

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

    def will_fail(self) -> bool:
        """Determine if the material is likely to fail under this test."""
        return not self.material.can_withstand_stress(self.stress)

    def __str__(self) -> str:
        return (
            f"Test on {self.material.name}: "
            f"Stress={self.stress:.2f} MPa, "
            f"Strain={self.strain:.6f}, "
            f"Young's Modulus={self.youngs_modulus:.2f} GPa"
        )


# Example material subclass
class Metal(Material):
    """A metal material."""

    def __init__(
        self, name: str, properties: MaterialProperties, is_ferrous: bool = False
    ):
        super().__init__(name, properties)
        self.is_ferrous = is_ferrous

    def __str__(self) -> str:
        ferrous_text = "Ferrous" if self.is_ferrous else "Non-ferrous"
        return f"{self.name} ({ferrous_text} metal, Density: {self.properties.density} kg/m³)"


# Example usage
steel_properties = MaterialProperties(
    density=7850, yield_strength=250, typical_youngs_modulus=200  # MPa  # GPa
)

steel = Metal("Steel", steel_properties, is_ferrous=True)
test = StressStrainTest(
    steel, force=5000, area=25, original_length=100, change_in_length=0.5
)

print(steel)
print(test)
print(f"Will the material fail? {'Yes' if test.will_fail() else 'No'}")
print(f"Calculated Young's modulus: {test.youngs_modulus:.2f} GPa")
print(f"Typical Young's modulus: {steel.properties.typical_youngs_modulus:.2f} GPa")
