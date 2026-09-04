"""Entry point demonstrating tests module integration."""

from tests import (
    StressStrainTest,
    calculate_factor_of_safety,
    calculate_strain,
    calculate_stress,
    calculate_youngs_modulus,
)


def run_tests_demo(material):
    """Executes and displays a stress-strain test using the tests module."""
    force = 50000.0  # N
    area = 0.00025  # m²
    orig_len = 2.0  # m
    change_len = 0.001  # m

    test = StressStrainTest(
        material=material,
        force=force,
        area=area,
        original_length=orig_len,
        change_in_length=change_len,
    )
    test.display_results()
    return test


from database import (
    units,
    add_material,
    get_material,
    list_materials,
)

def run_database_demo():
    """Executes and displays material management operations"""
    print("Database Module Demo:")

    #List the materials
    print(f"Initial Materials: {list_materials()}")
    #Add new material
    add_material("Copper", yield_strength=80000000.0, youngs_modulus=100000000000.0)
    print("Added 'Copper' to the database")

    #Display steel properties
    steel = get_material("Steel")
    if steel:
        print("\nSteel Properties:")
        print(f" - Yield Strength: {steel['yield_strength']:,.1f} {units[3]}")
        print(f" - Young's Modulus: {steel['youngs_modulus']:,.1f} {units[3]}")

    #Display updated material list
    print(f"Updated Materials: {list_materials()}")

run_database_demo()

from utils import (
    Loop,
    MatSelect,
    SafetyAna
)

def run_utils_demo():
    """Executes and displays reusable utilities"""

    #Asks for the material to be used
    final_material= MatSelect()
    print("Material selection confirmed!")

    #Queries the necessary values needed for calculation
    final_stress=Loop()
    print("Calculated!")

    #Makes safety analysis after necessary values and materials are found
    SafetyAna(final_material, final_stress)

run_utils_demo()