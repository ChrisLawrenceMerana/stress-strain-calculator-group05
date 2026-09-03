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

class Metal(Material):
    """Subclass for metal materials."""

    def __init__(
        self,
        name: str,
        properties: MaterialProperties,
        is_ferrous: bool = False,
        ductility_pct: float = 0.0,
    ):
        super().__init__(name,properties)
        if ductility_pct <0:
            raise ValueError("Ductility percentage must be non-negative")
        self.is_ferrous = is_ferrous
        self.ductility_pct = ductility_pct

    def __str__(self) -> str:
        ferrous_text = "Ferrous" if self.is_ferrous else "Non-ferrous"
        return(
            f"{self.name}({ferrous_text} metal, "
            f"Density: {self.properties.density}kg/m³, "
            f"Ductility: {self.ductility_pct}%)"
        )

    def to_dict(self) -> Dict[str, Any]:
        data = super().to_dict()
        data.update({"is_ferrous": self.is_ferrous, "ductility_pct": self.ductility_pct})
        return data

    #test