from interpreter import *

import unittest

class Test(unittest.TestCase):

    def test_simple_define(self):
        actual = interpreta("(define x 1)")
        expected = "Void"
        self.assertEqual(actual, expected)

    def test_multiple_defines(self):
        actual = interpreta("(define x 1) (define y 1) (define z 1) (define w 1)")
        expected = "Void"
        self.assertEqual(actual, expected)

    def test_simple_expression(self):
        actual = interpreta("(+ (* 2 3) 5)")
        expected = 11
        self.assertEqual(actual, expected)

    def test_variable_expression(self):
        actual = interpreta("(define x 5) (  + (* 2 x) 7)")
        expected = 17
        self.assertEqual(actual, expected)

    def test_built_in_functions_expression(self):
        actual = interpreta("(define x 1) (define y 1) (if ( eq x y) (* (cos x) 10) (/ x 4))")
        expected = 5.403023058681398
        self.assertEqual(actual, expected)

    def test_variable_not_defined_variable(self):
        with self.assertRaises(ValueError):
            interpreta("(define x 1) (define y 1) (if ( eq x y) (* (cos zeta) 10) (/ x 4))")
    
    def test_wrong_definition_syntax(self):
        expr = "(define x 1) (define y 1) (define) z (if ( eq x y) (* (cos zeta) 10) (/ x 4))"
        with self.assertRaises(SyntaxError):
            interpreta(expr)

    def test_warning_unary_function_syntax(self):
        expr = "(define x 1) (define y 1) (define zeta 10) (if ( eq x y) (* (cos zeta x) 10) (/ x 4))"
        with self.assertWarns(Warning):
            interpreta(expr)

    def test_multiple_results(self):
        expr = "(define x (+ 2 3)) (* 2 x) (+ 5 6)"
        actual = interpreta(expr)
        expected = [10,11]
        self.assertEqual(actual,expected)

unittest.main(verbosity=2)