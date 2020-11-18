class Category:
  def __init__(self, name):
    self.name = name.title()
    self.ledger = []
    self.total = 0

  def __str__(self):
    half_ast = int((30 - len(self.name))/2)
    dspl_lst = [f"{'*' * half_ast}{self.name}{'*' * half_ast}"]

    for i in range(len(self.ledger)):
      entry = []
      for v in self.ledger[i].values():
        if type(v) is str:
          entry.append(v[:23])
        else:
          v = float(v)
          entry.append(f'{v:.2f}')
      sp = ' ' * (30 - (len(entry[0]) + len(entry[1])))
      dspl_lst.append(sp.join(entry))

    dspl_lst.append(f'Total: {self.total:.2f}')

    dspl = '\n'
    dspl = dspl.join(dspl_lst)
    return dspl

  def deposit(self, amount, description = ''):
    self.ledger.append({'description': description, 'amount': amount })
    self.total += amount

  def withdraw(self, amount, description = ''):
    if self.check_funds(amount):
      amount = 0 - amount
      self.ledger.append({'description': description, 'amount': amount })
      self.total += amount
      return True
    else:
      return False
    
  def get_balance(self):
    return self.total

  def transfer(self, amount, destination):
    if self.check_funds(amount):
      destination.ledger.append({'description': f'Transfer from {self.name}', 'amount': amount })
      destination.total += amount

      amount = 0 - amount
      self.ledger.append({'description': f'Transfer to {destination.name}', 'amount': amount })
      self.total += amount
      return True
    else:
      return False

  def check_funds(self, amount):
    if amount > self.total:
      return False
    else: return True


def create_spend_chart(categories):
  total = 0
  cat_total = {}

  for category in categories:
    cat_withdraw = 0
    for i in category.ledger:
      # if i['description'].startswith('Transfer'): continue
      # else:
      if i['amount'] < 0:
        amount = abs(i['amount'])
        cat_withdraw += amount
        total += amount
    cat_total[category.name] = cat_withdraw

  cat_names = []
  cat_perc = []

  for k,v in cat_total.items():
    cat_names.append(k)
    cat_perc.append(int(v / total * 10) * 10)
  
  final_lst = ['Percentage spent by category']

  for perc in range(100, -10 , -10):
    percent = []
    percent.append(f'{perc:3}|')
    for num in cat_perc:
      if num >= perc:
        percent.append(' o ')
      else:
        percent.append('   ')
    percent.append(' ')
    sp = ''
    final_lst.append(sp.join(percent))
  
  final_lst.append('    ' + '-' * (len(cat_names) * 3 + 1))

  longest_cat = max(cat_names, key = len)

  for i in range(len(longest_cat)):
    names = ['    ']
    for name in cat_names:
      try:
        names.append(f' {name[i]} ')
      except:
        names.append('   ')
    names.append(' ')
    sp = ''
    final_lst.append(sp.join(names))

  sp = '\n'

  final_str = sp.join(final_lst)

  return final_str
