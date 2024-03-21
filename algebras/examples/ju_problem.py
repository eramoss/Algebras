import sys
sys.path.insert(0, '.')
from algebras.matrix_creation_by_rule import get_rules, get_conditions, get_values, create_matrix_by_rule
from algebras.matrix_rows_reductions import echelon_form, det_by_echelon_form
import numpy as np

rule = "2*i if i >= j, -j if j > i"
matrix_4_4 = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]



def print_matrix(matrix):
    print(np.array2string(matrix, separator=', ', formatter={'all': lambda x: "\t"+ str(x)}))

matrix = create_matrix_by_rule(matrix_4_4, rule)
print("Matrix by rule: ")
print_matrix(np.array(matrix))
print("\nEchelon form: ")
matrix = echelon_form(matrix)
print_matrix(np.array(matrix))
print("Determinant: ", det_by_echelon_form(matrix))