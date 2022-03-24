import unittest
import calculator_library
global N_AFTER_DOT
N_AFTER_DOT = 7

class TestCalc(unittest.TestCase):

    def test_add(self):
        self.assertEqual(calculator_library.add(10, 5), 15)
        self.assertEqual(calculator_library.add(0, 1), 1)
        self.assertEqual(calculator_library.add(1.55, -5), -3.45)
        self.assertEqual(calculator_library.add(3.1415, 7.1717), 10.3132)
        self.assertEqual(calculator_library.add(-335.7, -3.3), 339)

    def test_substract(self):
        self.assertEqual(calculator_library.substract(10, 5), 5)
        self.assertEqual(calculator_library.substract(0, 1), -1)
        self.assertEqual(calculator_library.substract(1.55, -5), 6.55)
        self.assertEqual(calculator_library.substract(-786.455, 9.13), 795.585)
        self.assertEqual(calculator_library.substract(-335.7, -3.3), -332.4)

    def test_multiply(self):
        self.assertEqual(calculator_library.multiply(10, 5), 50)
        self.assertEqual(calculator_library.multiply(0, 110), 0)
        self.assertEqual(calculator_library.multiply(1.55, -5), -7.75)
        self.assertEqual(calculator_library.multiply(-786.455, -9.13), 7180.33415)

    def test_division(self):
        self.assertEqual(calculator_library.division(10, 5), 2)
        self.assertEqual(calculator_library.division(0, 110), 0)
        self.assertEqual(calculator_library.division(1.55, -5), -0.31)
        self.assertEqual(calculator_library.division(-21, -7), 3)

        self.assertAlmostEqual(calculator_library.division(-786.455, -9.13), 86.1396495, places = N_AFTER_DOT)
        
        self.assertRaises(ValueError, calculator_library.division, 10, 0)

    def test_factorial(self):
        self.assertEqual(calculator_library.factorial(5), 120)
        self.assertEqual(calculator_library.factorial(2), 2)
        self.assertEqual(calculator_library.factorial(1), 1)

        self.assertRaises(ValueError, calculator_library.factorial, 0)
        self.assertRaises(ValueError, calculator_library.factorial, -7)
        self.assertRaises(ValueError, calculator_library.factorial, 3.33)

    def test_degree(self):
        self.assertEqual(calculator_library.degree(5, 2), 25)
        self.assertEqual(calculator_library.degree(5, 0), 1)
        self.assertEqual(calculator_library.degree(0, 2), 0)
        self.assertEqual(calculator_library.degree(1, 111), 1)
        self.assertEqual(calculator_library.degree(1.25, 4), 2.44140625)
        self.assertEqual(calculator_library.degree(-7, 3), -343)
        self.assertEqual(calculator_library.degree(-2, 4), 16)

        #self.assertAlmostEqual(calculator_library.division(1.25, 4), 2.4414062, places = N_AFTER_DOT)

        self.assertRaises(ValueError, calculator_library.degree, 5, 3.5)
        self.assertRaises(ValueError, calculator_library.degree, 2, -3)

    def test_root(self):
        self.assertEqual(calculator_library.root(4, 2), 2)
        self.assertEqual(calculator_library.root(-8, 3), -2)
        self.assertEqual(calculator_library.root(1, 111), 1)

        self.assertAlmostEqual(calculator_library.division(1.25, 4), 1.0573712, places = N_AFTER_DOT)
        self.assertAlmostEqual(calculator_library.division(-7, 3), -1.9129311, places = N_AFTER_DOT)
        self.assertAlmostEqual(calculator_library.division(5, 2), 2.2360679, places = N_AFTER_DOT)

        self.assertRaises(ValueError, calculator_library.root, -5, 2)
        self.assertRaises(ValueError, calculator_library.root, 7, 0)
        self.assertRaises(ValueError, calculator_library.root, 7, 3.33)
        self.assertRaises(ValueError, calculator_library.root, 7, -3)
    
    def test_logarithm(self):
        self.assertEqual(calculator_library.logarithm(2, 8), 3)
        self.assertEqual(calculator_library.logarithm(2, 1), 0) 
        self.assertEqual(calculator_library.logarithm(9, 3), 0.5)
        self.assertEqual(calculator_library.logarithm(0.5, 2), -1)  
        
        self.assertAlmostEqual(calculator_library.logarithm(10, 8), 0.9030899, places = N_AFTER_DOT)
        self.assertAlmostEqual(calculator_library.logarithm(0.5, 3), -1.5849625, places = N_AFTER_DOT)

        self.assertRaises(ValueError, calculator_library.logarithm, -5, 2)
        self.assertRaises(ValueError, calculator_library.logarithm, 1, 2)
        self.assertRaises(ValueError, calculator_library.logarithm, 2, -2)
        self.assertRaises(ValueError, calculator_library.logarithm, 0, 2)
        self.assertRaises(ValueError, calculator_library.logarithm, 2, 0)

if __name__ == '__main__':
    unittest.main()