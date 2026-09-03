"""Material class hierarchy"""

from typing import Any, Dict, Optional
from properties import MaterialProperties

class Material:
    """Base class for all materials."""

    def __init__ (self, name: str, properties: MaterialProperties):
        self.name = name
        self.properties = properties

    def __str__(self) -> str:
        return f"{self.name} (Density: {self.properties.density} kg/m³)"

    def can_withstand_stress (self, stress: float) -> bool:
        """Check if the material can withstand the given stress."""
        return stress < self.properties.yield_strength

    def to_dict(self) -> Dict[str, Any]:
        return{
            "name": self.name,
            "type": self._class__.__name__,
            "properties": self.properties.to_dict()
        }