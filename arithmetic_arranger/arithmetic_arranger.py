def arithmetic_arranger(problems, answer = False):
  if len(problems) > 5:
    return "Error: Too many problems."

  x_lst = []
  op_lst = []
  y_lst = []
  dash_lst = []
  x_sp = []
  y_sp = []
  sol_sp = []
  
  sp = ' '*4

  problems = [each.split() for each in problems]  
    
  for each in problems:
    maxLength = max(len(i) for i in each)
    if maxLength > 4:
      return "Error: Numbers cannot be more than four digits."
    else: 
      continue
  
  try:
    for each in problems:
      x_lst.append(int(each[0]))
      y_lst.append(int(each[2]))
  except:
    return "Error: Numbers must only contain digits."

  for each in problems:
      if each[1] == '+' or each[1] == '-':
        op_lst.append(each[1])
      else: return "Error: Operator must be '+' or '-'."

  if answer == True:
    op = {'+': (lambda x, y: x + y), '-': (lambda x, y: x - y)}
    sol_lst = []
    for x, y, p in zip(x_lst, y_lst, op_lst):
      sol = str(op[p] (x, y))
      dash = max(len(str(x)), len(str(y))) + 2
      sol_lst.append(' '*(dash - len(sol)) + sol)
      

  x_lst = [str(x) for x in x_lst]
  y_lst = [str(y) for y in y_lst]

  for x, y, p in zip(x_lst, y_lst, op_lst):
    dash = max(len(x), len(y)) + 2
    dash_lst.append('-'*dash)
    if len(x) > len(y):
      diff = len(x) - len(y)
      x_sp.append(' '*2 + x)
      y_sp.append(p + ' '*(diff +1) + y)
    elif len(x) < len(y):
      diff = len(y) - len(x)
      x_sp.append(' '*(diff + 2) + x)
      y_sp.append(p + ' ' + y)
    else: #equal length
      x_sp.append(' '*2 + x)
      y_sp.append(p + ' ' + y)

  

  num_one =  sp.join(x_sp)
  num_two =  sp.join(y_sp)
  dashes = sp.join(dash_lst)

  if answer == True:
    solutions = sp.join(sol_lst)
    arranged_problems = num_one + '\n' + num_two + '\n' + dashes + '\n' + solutions
  else:
    arranged_problems = num_one + '\n' + num_two + '\n' + dashes

  return arranged_problems
