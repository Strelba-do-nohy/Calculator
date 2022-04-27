########################################################
# Project name: Testa for math library for calculator
# Package: Calculator
# File: tdd_library_test.py
# Date: 24.03.2022
# Last changes: 27.04.2022
# Author: Strelba do nohy (Kateryna Zdebska -- xzdebs00)
#########################################################
# @package Calculator
# @file tdd_library_test.py
# @author Strelba do nohy (Kateryna Zdebska -- xzdebs00)
##########################################################

import unittest
import calculator_library
global N_AFTER_DOT
N_AFTER_DOT = 7

## @class Testing math library
# @param unittest.TestCase request for separate testing
class TestCalc(unittest.TestCase):
    ## Test for plus function
    # @test Summing positive, negative, integer and none-integer numbers
    # @param self Pointer to class
    def test_plus(self):
        self.assertEqual(calculator_library.plus(10, 5), 15)
        self.assertEqual(calculator_library.plus(0, 1), 1)
        self.assertEqual(calculator_library.plus(1.55, -5), -3.45)
        self.assertEqual(calculator_library.plus(3.1415, 7.1717), 10.3132)
        self.assertEqual(calculator_library.plus(-335.7, -3.3), -339)

    ## Test for minus function
    # @test Difference of positive, negative, integer and none-integer numbers
    # @param self Pointer to class
    def test_minus(self):
        self.assertEqual(calculator_library.minus(10, 5), 5)
        self.assertEqual(calculator_library.minus(0, 1), -1)
        self.assertEqual(calculator_library.minus(1.55, -5), 6.55)
        self.assertEqual(calculator_library.minus(-786.455, 9.13), -795.585)
        self.assertEqual(calculator_library.minus(-335.7, -3.3), -332.4)

    ## Test for umnoz function
    # @test Multiplication zero, positive, negative, integer and none-integer numbers
    # @param self Pointer to class
    def test_umnoz(self):
        self.assertEqual(calculator_library.umnoz(10, 5), 50)
        self.assertEqual(calculator_library.umnoz(0, 110), 0)
        self.assertEqual(calculator_library.umnoz(1.55, -5), -7.75)
        self.assertEqual(calculator_library.umnoz(-786.455, -9.13), 7180.33415)

    ## Test for podeli function
    # @test Division positive, negative, integer and none-integer numbers
    # @test Raising error for division by zero
    # @param self Pointer to class
    def test_podeli(self):
        self.assertEqual(calculator_library.podeli(10, 5), 2)
        self.assertEqual(calculator_library.podeli(0, 110), 0)
        self.assertEqual(calculator_library.podeli(1.55, -5), -0.31)
        self.assertEqual(calculator_library.podeli(-21, -7), 3)

        self.assertAlmostEqual(calculator_library.podeli(-786.455, -9.13), 86.1396495, places = N_AFTER_DOT)
        
        self.assertRaises(ZeroDivisionError, calculator_library.podeli, 10, 0)

    ## Test for faktorial function
    # @test Factorial calculation for positive, integer numbers
    # @test Raising error for factorial calculation for negative, none-integer numbers 
    # @param self Pointer to class
    def test_faktorial(self):
        self.assertEqual(calculator_library.faktorial(5), 120)
        self.assertEqual(calculator_library.faktorial(2), 2)
        self.assertEqual(calculator_library.faktorial(1), 1)
        self.assertEqual(calculator_library.faktorial(0), 1)
        
        #self.assertRaises(TypeError, calculator_library.faktorial, -7)
        self.assertRaises(TypeError, calculator_library.faktorial, 3.33)

    ## Test for exponenta function
    # @test Exponentiation of positive, negative, integer and none-integer numbers
    # @test Raising error for negative, none-integer power 
    # @param self Pointer to class
    def test_exponenta(self):
        self.assertEqual(calculator_library.exponenta(5, 2), 25)
        self.assertEqual(calculator_library.exponenta(5, 0), 1)
        self.assertEqual(calculator_library.exponenta(0, 2), 0)
        self.assertEqual(calculator_library.exponenta(1, 111), 1)
        self.assertEqual(calculator_library.exponenta(1.25, 4), 2.4414062)
        self.assertEqual(calculator_library.exponenta(-7, 3), -343)
        self.assertEqual(calculator_library.exponenta(-2, 4), 16)

        self.assertAlmostEqual(calculator_library.exponenta(1.25, 4), 2.4414062, places = N_AFTER_DOT)

        #self.assertRaises(TypeError, calculator_library.exponenta, 5, 3.5)
        #self.assertRaises(TypeError, calculator_library.exponenta, 2, -3)

    ## Test for koren function
    # @test Calculating root of positive, negative, integer and none-integer numbers
    # @test Raising error for calculating an even root of a negative number
    # @test Raising error for zero, negative, none-integer root
    # @param self Pointer to class
    def test_koren(self):
        self.assertEqual(calculator_library.koren(4, 2), 2)
        self.assertEqual(calculator_library.koren(-8, 3), -2)
        self.assertEqual(calculator_library.koren(1, 111), 1)

        self.assertAlmostEqual(calculator_library.koren(1.25, 4), (1.25**(1/4)), places = N_AFTER_DOT)
        self.assertAlmostEqual(calculator_library.koren(-7, 3), (-7**(1/3)), places = N_AFTER_DOT)
        self.assertAlmostEqual(calculator_library.koren(5, 2), (5**(1/2)), places = N_AFTER_DOT)

        self.assertRaises(TypeError, calculator_library.koren, -5, 2)
        self.assertRaises(ZeroDivisionError, calculator_library.koren, 7, 0)
        #self.assertRaises(TypeError, calculator_library.koren, 7, 3.33)
        #self.assertRaises(TypeError, calculator_library.koren, 7, -3)
    
    ## Test for log function
    # @test Calculating logarithm to positive, integer, none-integer base of positive, integer and none-integer numbers 
    # @test Raising error for zero, one, negatives, none-integers in base
    # @test Raising error for logarithm calculation for negative, zero numbers 
    # @param self Pointer to class
    def test_log(self):
        self.assertEqual(calculator_library.log(2, 8), 3)
        self.assertEqual(calculator_library.log(2, 1), 0) 
        self.assertEqual(calculator_library.log(9, 3), 0.5)
        self.assertEqual(calculator_library.log(0.5, 2), -1)  
        
        self.assertAlmostEqual(calculator_library.log(10, 8), 0.90309, places = N_AFTER_DOT)
        self.assertAlmostEqual(calculator_library.log(0.5, 3), -1.5849625, places = N_AFTER_DOT)

        self.assertRaises(TypeError, calculator_library.log, -5, 2)
        self.assertRaises(TypeError, calculator_library.log, 1, 2)
        self.assertRaises(TypeError, calculator_library.log, 2, -2)
        self.assertRaises(TypeError, calculator_library.log, 0, 2)
        self.assertRaises(TypeError, calculator_library.log, 2, 0)

if __name__ == '__main__':
    unittest.main()