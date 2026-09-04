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
