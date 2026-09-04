"""Main stress-strain test program."""

import csv
from datetime import datetime
import json
from pathlib import Path
import random

import database
from material import Material
from properties import MaterialProperties
from tests import StressStrainTest
from utils import Loop, MatSelect, SafetyAna, pa_to_mpa

# Directory and file management via pathlib
BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"
JSON_FILE = DATA_DIR / "test_results.json"
CSV_FILE = DATA_DIR / "test_results.csv"

def generate_simulated_test_data() -> tuple[float, float, float, float]:
    """Generates realistic simulated mechanical tensile test parameters using random."""
    # Tensile loads commonly range from 10 kN to 150 kN
    force = round(random.uniform(10_000.0, 150_000.0), 2)

    # Cylindrical or flat specimen cross-section area (approx 50 mm² to 500 mm²)
    area = round(random.uniform(0.00005, 0.00050), 6)

    # Standard specimen gauge length (0.05 m to 0.50 m)
    orig_len = round(random.uniform(0.05, 0.50), 4)

    # Elastic-to-plastic elongation (0.05 mm to 4.0 mm)
    changed_len = round(random.uniform(0.00005, 0.00400), 6)

    print("\n--- SIMULATED TEST BENCH DATA GENERATED ---")
    print(f"  Simulated Force            : {force:,.2f} N")
    print(f"  Simulated Area             : {area:.6f} m²")
    print(f"  Simulated Original Length  : {orig_len:.4f} m")
    print(f"  Simulated Elongation       : {changed_len:.6f} m")
    return force, area, orig_len, changed_len

def save_results_to_json(results_data: list, file_path: Path = JSON_FILE) -> None:
    """Saves a list of test result dictionaries into a JSON file."""
    try:
        DATA_DIR.mkdir(parents=True, exist_ok=True)
        with file_path.open(mode="w", encoding="utf-8") as file:
            json.dump(results_data, file, indent=4)
        print(f"\nResults successfully saved to '{file_path.name}'.")
    except Exception as e:
        print(f"\nError saving results to JSON: {e}")

def save_results_to_csv(results_data: list, file_path: Path = CSV_FILE) -> None:
    """Saves a list of test result dictionaries into a CSV file."""
    try:
        DATA_DIR.mkdir(parents=True, exist_ok=True)
        with file_path.open(mode="w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)

            writer.writerow([
                "Material",
                "Force (N)",
                "Area (m²)",
                "Original Length (m)",
                "Change in Length (m)",
                "Stress (Pa)",
                "Strain",
                "Youngs Modulus (Pa)",
                "Safety Factor",
                "Failed",
                "Timestamp",
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
                    test["timestamp"],
                ])
        print(f"Results successfully saved to '{file_path.name}'.")
    except Exception as e:
        print(f"\nError saving results to CSV: {e}")

def load_results_from_json(file_path: Path = JSON_FILE) -> list:
    """Loads and returns test result data from a JSON file using pathlib."""
    if not file_path.exists():
        return []

    try:
        with file_path.open(mode="r", encoding="utf-8") as file:
            data = json.load(file)
        print(f"Previous results successfully loaded from '{file_path.name}'.\n")
        return data
    except (json.JSONDecodeError, OSError) as e:
        print(f"Warning: Could not read '{file_path.name}' ({e}). Starting fresh.\n")
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
    session_results = load_results_from_json()

    while True:
        material_name = MatSelect()
        if not material_name:
            break

        # Let user decide whether to input manually or generate simulated data
        print("\nInput Mode:")
        print("[1] Enter manual test parameters")
        print("[2] Generate simulated test data (Random)")
        mode = input("Select option (1/2): ").strip()

        if mode == "2":
            force, area, orig_len, changed_len = generate_simulated_test_data()
        else:
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

        # Completion timestamp
        completion_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Package test attributes into a dictionary for JSON/CSV storage
        test_record = {
            "material": test.material.name,
            "force_N": round(test.force, 2),
            "area_m2": round(test.area, 6),
            "original_length_m": round(test.original_length, 4),
            "change_in_length_m": round(test.change_in_length, 6),
            "stress_Pa": round(test.stress, 2),
            "strain": round(test.strain, 6),
            "youngs_modulus_Pa": round(test.youngs_modulus, 2),
            "safety_factor": round(getattr(test, "safety_factor", 0.0), 2),
            "failed": test.will_fail() if hasattr(test, "will_fail") else False,
            "timestamp": completion_time,
        }
        session_results.append(test_record)

        again = input("\nPerform another calculation? (y/n): ").strip().lower()
        if again != "y":
            print("Exiting calculator.")
            break

    if session_results:
        save_results_to_json(session_results)
        save_results_to_csv(session_results)

if __name__ == "__main__":
    main()