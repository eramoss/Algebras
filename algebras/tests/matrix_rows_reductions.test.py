import unittest
import fractions
import sys
sys.path.insert(0, '.')
from algebras.matrix_rows_reductions import inverse_multiplier, add_row, multiply_row, swap_rows, echelon_form, multiply_primary_diagonal, det_by_echelon_form

class TestMatrixRowReductions(unittest.TestCase):

    def test_inverse_multiplier(self):
        self.assertEqual(inverse_multiplier(2, 4), fractions.Fraction(-2, 1))
        self.assertEqual(inverse_multiplier(5, 10), fractions.Fraction(-2, 1))

    def test_add_row(self):
        self.assertEqual(add_row([1, 2, 3], [4, 5, 6]), [5, 7, 9])
        self.assertEqual(add_row([0, 0, 0], [1, 1, 1]), [1, 1, 1])

    def test_multiply_row(self):
        self.assertEqual(multiply_row([1, 2, 3], 2), [2, 4, 6])
        self.assertEqual(multiply_row([4, 5, 6], 0), [0, 0, 0])

    def test_swap_rows(self):
        self.assertEqual(swap_rows([[1, 2, 3], [4, 5, 6]], 0, 1), [[4, 5, 6], [1, 2, 3]])

    def test_echelon_form(self):
        self.assertEqual(echelon_form([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), [[1, 2, 3], [0, -3, -6], [0, 0, 0]])

    def test_echelon_form_with_first_zero(self):
        self.assertEqual(echelon_form([[0, 2, 3], [4, 5, 6], [7, 8, 9]]), [[-4, -5, -6], [0, 2, 3], [0, 0, -3/8]])

    def test_multiply_primary_diagonal(self):
        self.assertEqual(multiply_primary_diagonal([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), 45)

    def test_det_by_echelon_form(self):
        self.assertEqual(det_by_echelon_form([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), 0)

if __name__ == '__main__':
    unittest.main()