# stress-strain-calculator-group05
# Stress and Strain Analysis System

## Group Members

| Member | Assigned Task | GitHub Username | Task 6 Contribution |
| :--- | :--- | :--- | :--- |
| Cabalfin | Task 1 – Basic Stress and Strain Calculator | @AljurCabalfin | Created the tests module and integrated file and directory management using pathlib |
| Ello | Task 2 – Control Structures and Validation | @ClarenceJohnEllo | Created the utils module and integrated test timestamps using datetimes |
| Galleto | Task 3 – Data Structures and Test History | @SherylJaneGalleto | Created the tests module and integrated saving and loading results to json |
| Meraña | Task 4 – Functions and Modular Programming | @ChrisLawrenceMerana | Created the material and properties module, integrated random simulated data using random |
| Moises | Task 5 – Object-Oriented Stress and Strain System | @MacieMoises | Created the database module and integrated test data export to csv |

### Primary Responsibilities

| Member | Primary Responsibility |
| :--- | :--- |
| CABALFIN, Aljur S. | Task 1 – Basic Stress and Strain Calculator, tests module, and integration of file and directory management using pathlib |
| ELLO, Clarence John D. | Task 2 – Control Structures and Validation, utils module and integrated test timestamps using datetimes |
| GALLETO, Sheryl Jane E. | Task 4 – Functions and Modular Programming, tests module and integrated saving and loading results to json |
| MERAÑA, Chris Lawrence O. | Task 5 – Object-Oriented Stress and Strain System, material and properties module, integrated random simulated data using random |
| MOISES, Macie L. | Task 3 - Data Structures and Test History, database module and integrated test data export to csv |

> Modular Integration was completed collaboratively by all members.

## Project Description
The Stress and Strain Analysis System is an engineering application designed to calculate mechanical behavior: including tensile stress, strain, Young's modulus, and safety margins for various materials under applied loads. It evaluates structural integrity against material yield strengths and logs session records for reporting and verification.

## Program Features
* **Core Mechanical Calculations:** Computes engineering stress in Pascals (Pa) and Megapascals (MPa), strain, and experimental Young's modulus.
* **Safety Evaluation:** Assesses structural integrity against material yield strengths by calculating the factor of safety and determining operational verdicts (Safe, Caution, or Unsafe).
* **Testing Modes:** Supports manual test parameter entry with input validation, as well as an automated simulator that generates scenarios using random.
* **Material Registry Management:** Manages predefined material standards (Steel, Aluminum, Titanium) and supports real-time registration of custom materials.
* **Persistent Session Logging:** Automatically records session test history to structured JSON and tabular CSV files via pathlib for auditing and record-keeping.

## Installation / Requirements
* **Python Version:** Python 3.8 or newer
* **Required Libraries:** Standard library modules only (no external pip packages required):
  * `csv`
  * `json`
  * `pathlib`
  * `random`
  * `datetime`
  * `dataclasses`
  * `typing`

## How to Run the Program
Run the main entry script from your terminal:

```bash
python main.py

## Repository Structure
* **`main.py`**: The primary application that handles user interaction, test mode, data synchronization between modules, and file persistence (JSON/CSV) via pathlib[cite: 6].
* **`material.py`**: Contains the object-oriented material domain hierarchy, featuring the base Material class and specialized subclasses (`Metal`, `Plastic`, `Composite`)[cite: 7].
* **`properties.py`**: Defines the MaterialProperties dataclass responsible for storing and validating base physical attributes (density, yield strength, and Young's modulus)[cite: 1].
* **`database.py`**: Acts as the central registry for standard material instances, supporting material lookups and custom material additions[cite: 5].
* **`tests.py`**: Encapsulates tensile test logic within the StressStrainTest class to compute stress, strain, Young's modulus, factor of safety, and state[cite: 3].
* **`utils.py`**: Provides pure calculation functions, unit conversion helpers (Pa, MPa, GPa), evaluations, and prompts[cite: 4].
* **`README.md`**: Project documentation and repository overview[cite: 2].