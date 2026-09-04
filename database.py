"""Module for managing predefined materials and their physical properties"""

materials_database = {
    "Steel": {"yield_strength": 250000000.0, "youngs_modulus": 200000000000.0},
    "Aluminum": {"yield_strength": 95000000.0, "youngs_modulus": 69000000000.0},
    "Titanium": {"yield_strength": 880000000.0, "youngs_modulus": 114000000000.0}
}

units = ("N", "m²", "m", "Pa")

def get_material(material):
    """Retrieve properties for a material"""
    material = material.title()
    return materials_database.get(material)

def add_material(material, yield_strength, youngs_modulus):
    """Adds a new material with its yield strength and Young's modulus to the database"""
    materials_database[material.title()] = {
        "yield_strength": yield_strength,
        "youngs_modulus": youngs_modulus
    }

def list_materials():
    """Returns a list of all available material names"""
    return list(materials_database.keys())
