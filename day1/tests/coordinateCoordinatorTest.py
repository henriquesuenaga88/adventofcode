import unittest
from ..src.coordinateCalculator import CoordinateCalculator

class TestDay1(unittest.TestCase):

    def test_calc_taxicab_geometry_from_R2_L3(self):
        calculator = CoordinateCalculator("R2, L3").calc_taxicab_geometry_from()
        self.assertEqual(calculator.total_distance, 5)
        self.assertEqual(calculator.first_location_visited_twice_distance, 0)

    def test_calc_taxicab_geometry_from_R2_R2_R2(self):
        calculator = CoordinateCalculator("R2, R2, R2").calc_taxicab_geometry_from()
        self.assertEqual(calculator.total_distance, 2)
        self.assertEqual(calculator.first_location_visited_twice_distance, 1)

    def test_calc_taxicab_geometry_from_R5_L5_R5_R3(self):
        calculator = CoordinateCalculator("R5, L5, R5, R3").calc_taxicab_geometry_from()
        self.assertEqual(calculator.total_distance, 12)
        self.assertEqual(calculator.first_location_visited_twice_distance, 0)

    def test_calc_taxicab_geometry_from_R8_R4_R4_R8(self):
        calculator = CoordinateCalculator("R8, R4, R4, R8").calc_taxicab_geometry_from()
        self.assertEqual(calculator.total_distance, 8)
        self.assertEqual(calculator.first_location_visited_twice_distance, 4)

if __name__ == '__main__':
    unittest.main()
