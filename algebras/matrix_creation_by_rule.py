def get_rules(text):
   return text.split(",")
    
def get_conditions(rule):
    return rule.split("if")[1]

def get_values(rule):
    return rule.split("if")[0]

def create_matrix_by_rule(matrix, rule):
    '''construction rule is something like this:
    "1 if i == j, 0 if i != j"'''
    for i in range(1,len(matrix) +1):
      for j in range(1,len(matrix[0]) + 1):
         rules = get_rules(rule)
         for rule in rules:
            if eval(get_conditions(rule)): matrix[i -1][j-1] = eval(get_values(rule))
    return matrix