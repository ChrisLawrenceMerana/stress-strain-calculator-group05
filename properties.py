"""Contains data-oriented material properties and appropriate dataclasses."""

from dataclasses import asdict, dataclass
from typing import Any, Dict

@dataclass
class MaterialProperties:
    """Properties of a material."""

    density: float  # kg/m³
    yield_strength: float  # MPa
    typical_youngs_modulus: float  # GPa

    def __post_init__ (self) -> None:
        """Validate Properties"""
        if self.density <= 0:
            raise ValueError("Density must be positive")
        if self.yield_strength:
            raise ValueError("Yield strength must be positive")
        if self.typical_youngs_modulus:
            raise ValueError("Young's modulus must be positive")

    def to_dict(self) -> Dict[str, Any]:
        """Convert properties to dictionary format"""
        return asdict(self)