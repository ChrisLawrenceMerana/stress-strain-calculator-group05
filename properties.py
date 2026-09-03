"""Contains data-oriented material properties and appropriate dataclasses."""

from dataclasses import asdict, dataclass
from typing import Any, Dict

@dataclass
class MaterialProperties:
    """Properties of a material."""

    density: float  # kg/m³
    yield_strength: float  # MPa
    typical_youngs_modulus: float  # GPa