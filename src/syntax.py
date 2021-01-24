import re

file = open('debug.txt', 'w+')

syn = {
  'RES': ['PROGRAMA', 'FINPROG', 'SI', 'ENTONCES', 'SINO', 'FINSI', 'REPITE', 'VECES', 'FINREP', 'IMPRIME', 'LEE'],
  'REL': ['>', '<', '==', '='],
  'ARI': ['+', '-', '*', '/']
}

def toArr(str):
  arr = []
  currStr = '' 
  flag = False
  for i in str:
    if(i == '\n'):
      if(currStr != ''):
        arr.append(currStr)
    elif(i != ' ' and i != '"'):
      currStr = currStr + i
    else:
      if(flag):
        if(i != '"'):
          currStr = currStr + i
        else:
          flag = False
          currStr = currStr + i
          arr.append(currStr)
          currStr = ''
      else:
        if(i == ' '):
          if(currStr != ''):
            arr.append(currStr)
            currStr = ''
        else:
          flag = True
          currStr = currStr + i
  return arr

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

def isLine(arr):
  flag = True
  file.write(' '.join(arr) + '\n')
  for i in arr:
    # Check if it is any of the reserved words
    if(not(isAny(i))):
      flag = False
  return flag

def isDefault(word):
  flag = isRES(word) or isREL(word) or isARI(word)
  return flag

def isAny(word):
  flag = isRES(word) or isREL(word) or isARI(word) or word == '=' or isID(word) or isNumeric(word) or isText(word)
  return flag

def isID(word):
  pattern = '[A-Za-z][A-Za-z0-9]+'
  flag = re.match(pattern, word)  
  return flag

def isNumeric(word):  
  pattern = '[0-8]+'
  flag = re.match(pattern, word) 
  return flag

def isText(word):
  pattern = ('"[\sA-Za-z0-9]+"')
  flag = re.match(pattern, word)
  return flag

def octalToDecimal(octal):
  decimal = 0
  position = 0
  octal = octal[::-1]
  for digit in octal:
    value = int(digit)
    num = int(8 ** position)
    equivalence = int(num * value)
    decimal += equivalence
    position += 1
  return decimal
