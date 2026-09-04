"""Main stress-strain test program with JSON persistence."""

import csv
import json
import datetime
import database
from material import Material
from properties import MaterialProperties
from tests import StressStrainTest
from utils import Loop, MatSelect, SafetyAna, pa_to_mpa


def save_results_to_json(results_data: list, filename: str = "test_results.json") -> None:
    """Saves a list of test result dictionaries into a JSON file."""
    try:
        with open(filename, "w") as file:
            json.dump(results_data, file, indent=4)
        print(f"\nResults successfully saved to '{filename}'.")
    except Exception as e:
        print(f"\nError saving results: {e}")

def save_results_to_csv(results_data: list, filename: str = "test_results.csv") -> None:
    """Saves a list of test result dictionaries into a CSV file."""
    try:
        with open(filename, "w", newline="") as file:
            writer = csv.writer(file)
            
            writer.writerow([
                "Material", "Force (N)", "Area (m²)", "Original Length (m)", 
                "Change in Length (m)", "Stress (Pa)", "Strain", 
                "Youngs Modulus (Pa)", "Safety Factor", "Failed", "Timestamp"
            ])
            
            for test in results_data:
                writer.writerow([
                    test["material"],
                    test["force_N"],
                    test["area_m2"],
                    test["original_length_m"],
                    test["change_in_length_m"],
                    test["stress_Pa"],
                    test["strain"],
                    test["youngs_modulus_Pa"],
                    test["safety_factor"],
                    test["failed"],
                    test["timestamp"]
                ])
        print(f"Results successfully saved to '{filename}'.")
    except Exception as e:
        print(f"\nError saving results to CSV: {e}")

def load_results_from_json(filename: str = "test_results.json") -> list:
    """Loads and returns test result data from a JSON file."""
    try:
        with open(filename, "r") as file:
            data = json.load(file)
        print(f"Previous results successfully loaded from '{filename}'.\n")
        return data
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print(f"Error: Failed to parse '{filename}'. File may be corrupted.\n")
        return []


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
    # Load previous session history if available
    session_results = load_results_from_json()

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

        # Marks time of completion through the datetime module
        completiontime= datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Package test attributes into a dictionary for JSON storage
        test_record = {
            "material": test.material.name,
            "force_N": test.force,
            "area_m2": test.area,
            "original_length_m": test.original_length,
            "change_in_length_m": test.change_in_length,
            "stress_Pa": test.stress,
            "strain": test.strain,
            "youngs_modulus_Pa": test.youngs_modulus,
            "safety_factor": getattr(test, "safety_factor", 0.0),
            "failed": test.will_fail() if hasattr(test, "will_fail") else False,
            "timestamp": completiontime,
        }
        session_results.append(test_record)

        # Query user to continue or exit after completing the run
        again = input("\nPerform another calculation? (y/n): ").strip().lower()
        if again != "y":
            print("Exiting calculator.")
            break

    # Save all test records to JSON and csv upon exiting
    if session_results:
        save_results_to_json(session_results)
        save_results_to_csv(session_results)


if __name__ == "__main__":
    main()
