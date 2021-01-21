syn = {
  'RES': ['PROGRAMA', 'FINPROG', 'SI', 'ENTONCES', 'SINO', 'FINSI', 'REPITE', 'VECES', 'FINREP', 'IMPRIME', 'LEE'],
  'REL': ['>', '<', '=='],
  'ARI': ['+', '-', '*', '/']
}

def isRES(word):
  flag = False
  for i in syn['RES']:
    if(word == i):
      flag = True
  return flag

def isREL(word):
  flag = False
  for i in syn['REL']:
    if(word == i):
      flag = True
  return flag

def isARI(word):
  flag = False
  for i in syn['ARI']:
    if(word == i):
      flag = True
  return flag

def isAny(word):
  flag = isRES(word) or isREL(word) or isARI(word) or (word == '=') or (word[0] == '"' and word[-1] == '"')
  return flag

def isLine(arr):
  flag = True
  for i in arr:
    # Check if it is any of the reserved words
    if(not(isAny(i))):
      flag = False
  return flag
