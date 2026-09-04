"""Module for managing predefined materials and their physical properties"""

from material import Metal, Material
from properties import MaterialProperties

# Pre-populated using domain classes with units: density (kg/m³), yield_strength (MPa), youngs_modulus (GPa)
materials_database = {
    "Steel": Metal("Steel", MaterialProperties(7850.0, 250.0, 200.0), is_ferrous=True, ductility_pct=18.0),
    "Aluminum": Metal("Aluminum", MaterialProperties(2700.0, 95.0, 69.0), is_ferrous=False, ductility_pct=12.0),
    "Titanium": Metal("Titanium", MaterialProperties(4500.0, 880.0, 114.0), is_ferrous=False, ductility_pct=10.0),
}

units = ("N", "m²", "m", "Pa")

def get_material(material: str):
    """Retrieve properties for a material case-insensitively."""
    if material in materials_database:
        return materials_database[material]
    
    titled = material.strip().title()
    if titled in materials_database:
        return materials_database[titled]

    for name, mat_obj in materials_database.items():
        if name.lower() == material.strip().lower():
            return mat_obj
            
    return None

def add_material(material: str, yield_strength: float, youngs_modulus: float, density: float = 5000.0):
    """Adds a new material with its yield strength (MPa) and Young's modulus (GPa) to the database"""
    props = MaterialProperties(
        density=density,
        yield_strength=yield_strength,
        typical_youngs_modulus=youngs_modulus,
    )
    name = material.strip().title()
    materials_database[name] = Material(name, props)

def list_materials():
    """Returns a list of all available material names"""
    return list(materials_database.keys())