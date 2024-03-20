import fractions

def inverse_multiplier(a,m):
    '''Returns the multiplier in Fraction that a*multiplier = -m'''
    return fractions.Fraction(-m,a)

def add_row(m1,m2):
    '''Returns the sum of two rows'''
    return [m1[i]+m2[i] for i in range(len(m1))]

def multiply_row(m1,multiplier):
    '''Returns the row multiplied by a multiplier'''
    return [m1[i]*multiplier for i in range(len(m1))]

def swap_rows(matrix,i,j):
    '''Swaps two rows in a matrix'''
    matrix[i],matrix[j] = matrix[j],matrix[i]
    return matrix

def echelon_form(matrix):
    for i in range(len(matrix)):
        for j in range(i+1,len(matrix)):
            '''i is the current row for pivot and j is the next row to be reduced'''

            pivot = matrix[i][i]
            if pivot == 0:
                '''If the pivot is zero, we need to swap the rows'''
                matrix = swap_rows(matrix,i,i+1)
                matrix[i] = multiply_row(matrix[i],-1)
                
                continue
            i_element_next_row = matrix[j][i]
            multiplier = inverse_multiplier(pivot,i_element_next_row)
            matrix[j] = add_row(matrix[j],multiply_row(matrix[i],multiplier))
    return matrix

def multuply_primary_diagonal(matrix):
    product = 1
    for i in range(len(matrix)):
        product *= matrix[i][i]
    return product

def det_by_echelon_form(matrix):
    '''Returns the determinant of a matrix by converting it to echelon form'''
    echelon_matrix = echelon_form(matrix)
    return multuply_primary_diagonal(echelon_matrix)


matrix = [[1,2,3],[4,0,6],[7,6,9]]
print(echelon_form(matrix))
print(det_by_echelon_form(matrix))