"""Main stress-strain test program."""

import database
from material import Material
from properties import MaterialProperties
from tests import StressStrainTest
from utils import Loop, MatSelect, SafetyAna, pa_to_mpa

def sync_to_material_object(name: str) -> Material:
    """Wraps dictionary/database entries into a Material instance for tests.py."""
    import utils

    mat_info = utils.materials[name]
    props = MaterialProperties(
        density=7850.0,
        yield_strength=float(mat_info["yield_strength"]),
        typical_youngs_modulus=float(mat_info["youngs_modulus"]),
    )
    return Material(name=name, properties=props)

def main():
    while True:
        material_name = MatSelect()
        if not material_name:
            break

        measurements = Loop()
        if measurements is None:
            print("Exiting calculator.")
            break

        force, area, orig_len, changed_len = measurements

        # Build class instance for tests.py
        material_obj = sync_to_material_object(material_name)

        # Execute tests.py verification
        test = StressStrainTest(
            material=material_obj,
            force=force,
            area=area,
            original_length=orig_len,
            change_in_length=changed_len,
        )
        test.display_results()

        # Run safety evaluation through utils.py
        SafetyAna(material_name, test.stress)

        # Query user to continue or exit after completing the run
        again = input("\nPerform another calculation? (y/n): ").strip().lower()
        if again != "y":
            print("Exiting calculator.")
            break

if __name__ == "__main__":
    main()