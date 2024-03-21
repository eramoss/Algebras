def get_rules(text):
   return text.split(",")
    
def get_conditions(rule):
    return rule.split("if")[1]

def get_values(rule):
    return rule.split("if")[0]

def create_matrix_by_rule(matrix, construct_rule):
    '''construct_rule is a string that contains the rules to create the matrix.
    The rules are separated by commas. Each rule is a condition followed by the value to be assigned to the matrix element.
    The condition is after the word "if" and the value is before the word "if".
    
    The variables to represent the row and column are i and j, respectively.
    In programming we represent the rows and the columns starting from 0, but in math we start from 1.
    
    Example:
    rule = "5 * i - j  if i == j, 2*i  if i > j, -j if j > i"'''
    for i in range(1,len(matrix) +1):
      for j in range(1,len(matrix[0]) + 1):
         rules = get_rules(construct_rule)
         for rule in rules:
            if eval(get_conditions(rule)): matrix[i -1][j-1] = eval(get_values(rule))
    return matrix