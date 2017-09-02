import unittest
from ..src.coordinateCalculator import CoordinateCalculator

class TestDay1(unittest.TestCase):

    def test_calcTaxiCabGeometryFromR2L3(self):
        calculator = CoordinateCalculator("R2, L3")
        calculator.calcTaxiCabGeometryFrom()
        self.assertEqual(calculator.total_distance, 5)
        self.assertEqual(calculator.firstLocationVisitedTwiceDistance, 0)

    def test_calcTaxiCabGeometryFromR2R2R2(self):
        calculator = CoordinateCalculator("R2, R2, R2").calcTaxiCabGeometryFrom()
        self.assertEqual(calculator.total_distance, 2)
        self.assertEqual(calculator.firstLocationVisitedTwiceDistance, 1)

    def test_calcTaxiCabGeometryFromR5L5R5R3(self):
        calculator = CoordinateCalculator("R5, L5, R5, R3").calcTaxiCabGeometryFrom()
        self.assertEqual(calculator.total_distance, 12)
        self.assertEqual(calculator.firstLocationVisitedTwiceDistance, 0)

    def test_calcTaxiCabGeometryFromR8R4R4R8(self):
        calculator = CoordinateCalculator("R8, R4, R4, R8").calcTaxiCabGeometryFrom()
        self.assertEqual(calculator.total_distance, 8)
        self.assertEqual(calculator.firstLocationVisitedTwiceDistance, 4)

if __name__ == '__main__':
    unittest.main()