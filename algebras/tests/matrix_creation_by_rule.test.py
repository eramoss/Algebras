import unittest
import fractions
import sys
sys.path.insert(0, '.')
from algebras.matrix_creation_by_rule import get_rules, get_conditions, get_values, create_matrix_by_rule

class TestMatrixRowReductions(unittest.TestCase):
    default_rule = "2*i if i >= j, -j if j > i"
    def test_get_rules(self):
        self.assertEqual(get_rules(self.default_rule), ['2*i if i >= j', ' -j if j > i'])

    def test_get_conditions(self):
        self.assertEqual(get_conditions("2*i if i >= j"), ' i >= j')

    def test_get_values(self):
        self.assertEqual(get_values("2*i if i >= j"), '2*i ')
    
    def test_create_matrix_by_rule(self):
        default_matrix = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
        rules = get_rules(self.default_rule)
        matrix = create_matrix_by_rule(default_matrix, self.default_rule)
        for i in range(1,len(matrix) +1):
            for j in range(1,len(matrix[0]) + 1):
                for rule in rules:
                    if eval(get_conditions(rule)): self.assertEqual(matrix[i -1][j-1], eval(get_values(rule)))
        
       

if __name__ == '__main__':
    unittest.main()