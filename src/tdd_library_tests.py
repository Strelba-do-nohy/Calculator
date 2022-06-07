"""!
* Project Name : Calculator                                               
* File : tdd_library_test.py                                                    
* Date : 24.03.2022                                                        
* Last change : 27.04.2022                                                 
* Author : Strelba do nohy (Kateryna Zdebska -- xzdebs00)                                                                                                                
* Description : Tests for math library for calculator                                                                                 
"""
"""!
 @file tdd_library_test.py                                                                                                                  
 @brief Tests for math library for calculator                                                   
 @author Strelba do nohy (Kateryna Zdebska -- xzdebs00)
"""

import unittest
import matematicka_knihovna
global N_AFTER_DOT
## max number of characters after dot
N_AFTER_DOT = 7

class TestCalc(unittest.TestCase):
    """!
        @brief class for testing math library
        @param unittest.TestCase request for separate testing
        """
    def test_plus(self):
        """!
        @brief Test for plus function
        @test Summing positive, negative, integer and none-integer numbers
        @param self Pointer to class
        """
        self.assertEqual(matematicka_knihovna.plus(10, 5), 15)
        self.assertEqual(matematicka_knihovna.plus(0, 1), 1)
        self.assertEqual(matematicka_knihovna.plus(1.55, -5), -3.45)
        self.assertEqual(matematicka_knihovna.plus(3.1415, 7.1717), 10.3132)
        self.assertEqual(matematicka_knihovna.plus(-335.7, -3.3), -339)

    def test_minus(self):
        """!
        @brief Test for minus function
        @test Difference of positive, negative, integer and none-integer numbers
        @param self Pointer to class
        """
        self.assertEqual(matematicka_knihovna.minus(10, 5), 5)
        self.assertEqual(matematicka_knihovna.minus(0, 1), -1)
        self.assertEqual(matematicka_knihovna.minus(1.55, -5), 6.55)
        self.assertEqual(matematicka_knihovna.minus(-786.455, 9.13), -795.585)
        self.assertEqual(matematicka_knihovna.minus(-335.7, -3.3), -332.4)

    def test_umnoz(self):
        """!
        @brief Test for umnoz function
        @test Multiplication zero, positive, negative, integer and none-integer numbers
        @param self Pointer to class
        """
        self.assertEqual(matematicka_knihovna.umnoz(10, 5), 50)
        self.assertEqual(matematicka_knihovna.umnoz(0, 110), 0)
        self.assertEqual(matematicka_knihovna.umnoz(1.55, -5), -7.75)
        self.assertEqual(matematicka_knihovna.umnoz(-786.455, -9.13), 7180.33415)

    def test_podeli(self):
        """!
        @brief Test for podeli function
        @test Division positive, negative, integer and none-integer numbers
        @test Raising error for division by zero
        @param self Pointer to class
        """
        self.assertEqual(matematicka_knihovna.podeli(10, 5), 2)
        self.assertEqual(matematicka_knihovna.podeli(0, 110), 0)
        self.assertEqual(matematicka_knihovna.podeli(1.55, -5), -0.31)
        self.assertEqual(matematicka_knihovna.podeli(-21, -7), 3)

        self.assertAlmostEqual(matematicka_knihovna.podeli(-786.455, -9.13), 86.1396495, places = N_AFTER_DOT)
        
        self.assertRaises(ZeroDivisionError, matematicka_knihovna.podeli, 10, 0)

    def test_faktorial(self):
        """!
        @brief Test for faktorial function
        @test Factorial calculation for positive, integer numbers
        @test Raising error for factorial calculation for negative, none-integer numbers 
        @param self Pointer to class
        """
        self.assertEqual(matematicka_knihovna.faktorial(5), 120)
        self.assertEqual(matematicka_knihovna.faktorial(2), 2)
        self.assertEqual(matematicka_knihovna.faktorial(1), 1)
        self.assertEqual(matematicka_knihovna.faktorial(0), 1)
        
        #self.assertRaises(TypeError, matematicka_knihovna.faktorial, -7)
        self.assertRaises(TypeError, matematicka_knihovna.faktorial, 3.33)

    def test_exponenta(self):
        """!
        @brief Test for exponenta function
        @test Exponentiation of positive, negative, integer and none-integer numbers
        @test Raising error for none-integer power 
        @param self Pointer to class
        """
        self.assertEqual(matematicka_knihovna.exponenta(5, 2), 25)
        self.assertEqual(matematicka_knihovna.exponenta(5, 0), 1)
        self.assertEqual(matematicka_knihovna.exponenta(0, 2), 0)
        self.assertEqual(matematicka_knihovna.exponenta(1, 111), 1)
        self.assertEqual(matematicka_knihovna.exponenta(1.25, 4), 2.4414062)
        self.assertEqual(matematicka_knihovna.exponenta(-7, 3), -343)
        self.assertEqual(matematicka_knihovna.exponenta(-2, 4), 16)

        self.assertAlmostEqual(matematicka_knihovna.exponenta(1.25, 4), 2.4414062, places = N_AFTER_DOT)

        self.assertRaises(TypeError, matematicka_knihovna.exponenta, 5, 3.5)

    def test_koren(self):
        """!
        @brief Test for koren function
        @test Calculating root of positive, negative, integer and none-integer numbers
        @test Raising error for calculating an even root of a negative number
        @test Raising error for zero, negative, none-integer root
        @param self Pointer to class
        """
        self.assertEqual(matematicka_knihovna.koren(4, 2), 2)
        self.assertEqual(matematicka_knihovna.koren(-8, 3), -2)
        self.assertEqual(matematicka_knihovna.koren(1, 111), 1)

        self.assertAlmostEqual(matematicka_knihovna.koren(1.25, 4), (1.25**(1/4)), places = N_AFTER_DOT)
        self.assertAlmostEqual(matematicka_knihovna.koren(-7, 3), (-7**(1/3)), places = N_AFTER_DOT)
        self.assertAlmostEqual(matematicka_knihovna.koren(5, 2), (5**(1/2)), places = N_AFTER_DOT)

        self.assertRaises(TypeError, matematicka_knihovna.koren, -5, 2)
        self.assertRaises(ZeroDivisionError, matematicka_knihovna.koren, 7, 0)
        self.assertRaises(TypeError, matematicka_knihovna.koren, 7, 3.33)
        self.assertRaises(TypeError, matematicka_knihovna.koren, 7, -3)
    
    def test_log(self):
        """!
        @brief Test for log function
        @test Calculating logarithm to positive, integer, none-integer base of positive, integer and none-integer numbers 
        @test Raising error for zero, one, negatives, none-integers in base
        @test Raising error for logarithm calculation for negative, zero numbers 
        @param self Pointer to class
        """
        self.assertEqual(matematicka_knihovna.log(2, 8), 3)
        self.assertEqual(matematicka_knihovna.log(2, 1), 0) 
        self.assertEqual(matematicka_knihovna.log(9, 3), 0.5)
        self.assertEqual(matematicka_knihovna.log(0.5, 2), -1)  
        
        self.assertAlmostEqual(matematicka_knihovna.log(10, 8), 0.90309, places = N_AFTER_DOT)
        self.assertAlmostEqual(matematicka_knihovna.log(0.5, 3), -1.5849625, places = N_AFTER_DOT)

        self.assertRaises(TypeError, matematicka_knihovna.log, -5, 2)
        self.assertRaises(TypeError, matematicka_knihovna.log, 1, 2)
        self.assertRaises(TypeError, matematicka_knihovna.log, 2, -2)
        self.assertRaises(TypeError, matematicka_knihovna.log, 0, 2)
        self.assertRaises(TypeError, matematicka_knihovna.log, 2, 0)

if __name__ == '__main__':
    unittest.main()
