def get_rules(text):
   return text.split(",")
    
def get_conditions(rule):
    return rule.split("if")[1]

def get_values(rule):
    return rule.split("if")[0]

def create_matrix_by_rule(matrix, construct_rule):
    for i in range(1,len(matrix) +1):
      for j in range(1,len(matrix[0]) + 1):
         rules = get_rules(construct_rule)
         for rule in rules:
            if eval(get_conditions(rule)): matrix[i -1][j-1] = eval(get_values(rule))
    return matrix