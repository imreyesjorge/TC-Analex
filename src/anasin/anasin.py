import sys
sys.path.append('src/')

from syntax import syn

file = open('{}.lex'.format(sys.argv[1]))


initialStack = []
actualStack=['#']
def isEmpty():
  return actualStack==['#']
def push(item):
  actualStack.append(item)
def pop():
  return actualStack.pop()
def inspect():
  return actualStack[len(actualStack)-1]
def size():
  return len(actualStack)
  
flagPROG=False
flagID=False
flagSI=False
flagREP=False
flagIMP=False
flagLEE=False
flagError=False

for line in file:
  print(line, end = '')
  line = line.split()
  initialStack.append(line)
print()

for line in initialStack:
  print(line)
  print(actualStack)
  print()
  #-------------------------------------------------------------------
  #Estructura de PROGRAMA 
  if 'PROGRAMA' in line and not(flagPROG) and isEmpty():
    flagPROG=True
    push('FINPROG')  
    push('SENTS')
    push('[id]')
    continue
  if '[id]' in line and inspect()=='[id]' and flagPROG:
    if not(flagError):
      pop()
      continue
    else:
      print('ERROR NO INICIO DE PROGRAMA')
      flagError=True
      break
  if 'FINPROG' in line and flagPROG and inspect()=='FINPROG':
    flagPROG=False
    pop()
    continue  
    
  #-------------------------------------------------------------------
  #VARIABLES DEL PROGRAMA
  #Variable ELEM
  if inspect()=='ELEM':
    if ('[val]' in line or '[id]' in line):
      pop()
      continue
    else:
      print('ERROR DE ELEM')
      flagError=True
      break

  #Variable COMPARA
  if inspect()=='COMPARA' and flagSI:
    if '[id]' in line:
      push('[op_rel]')
      continue
    else:
      print('ERROR DE COMPARA ID')
      flagError=True
      break
    if inspect()=='[op_rel]' and flagSI:
      pop()
      pop()
      continue
    else:
      print('ERROR DE COMPARA OPREL')
      flagError=True
      break

  #Variable SENTS
  if inspect()=='SENTS':
    pop()
    push('SENT')    #Metemos variable 
    continue
    #Agrego un SENT y depsues puedo agregar un SENTS pero no es neceario 

  #Variable SENT 
  if inspect()=='SENT' or flagID or flagSI or flagREP or flagIMP or flagLEE:
    if '[id]' in line and flagID:
      pop()      
      push('ELEM')
      push('=')
      continue
    if ('=' in line and inspect()=='=' and flagID and flagPROG) or flagID:
      pop()      
      next = initialStack.index(line)+2
      if initialStack[next]=='[op_ar]' and flagID and flagPROG:
        push('ELEM')
        flagID=False
        continue
      else:
        flagID=False
        continue

    if 'SI' in line or flagSI:
      pop()
      #Colocamos la estructura del SI #Estructruta de SI ENTONCES SINO FINSI 
      if 'SI' in line and flagPROG:
        flagSI=True
        push('FINSI')
        push('SENTS')     #Metemos variable
        push('ENTONCES')
        push('COMPARA')   #Metemos variable
        continue
      if 'ENTONCES' in line and inspect()=='ENTONCES' and flagSI and flagPROG:
        pop()
        continue
      if 'SINO' in line and flagSI and flagPROG:    
        push('SENTS')     #Metemos variable 
        continue
      if 'FINSI' in line and flagSI and inspect()=='FINSI' and flagPROG:
        pop()
        if not('FINSI' in actualStack):
          flagSI=False
          continue
        else:
          continue

    elif 'REPITE' in line or flagREP:
      pop()
      #Colocamos la estructura del REPITE #Estructura de REPITE VECES FINREP
      if 'REPITE' in line and flagPROG:
        flagREP=True
        push('FINREP')
        push('SENTS')     #Metemos variable
        push('VECES')  
        push('ELEM')      #Metemos variable
        continue 
      if 'VECES' in line and inspect()=='VECES' and flagREP and flagPROG:
        pop()
        push('SENTS')     #Metemos variable 
        continue
      if 'FINREP' in line and inspect()=='FINREP' and flagREP and flagPROG:
        pop()
        if not('FINSI' in actualStack):
          flagREP=False
          continue
        else:
          continue

    elif 'IMPRIME' in line or flagIMP:
      pop()
      #Colocamos la estructura del IMPRIME #Estructura de IMPRIME
      if 'IMPRIME' in line and flagPROG:
        flagIMP=True
        push('IMPRIME')
        continue
      if inspect()=='IMPRIME' and flagIMP:
        if '[text]' in line:
          flagIMP=False
          pop()
          continue
        else:
          pop()
          push('ELEM')    #Metemos variable 
          continue

    elif 'LEE' in line or flagLEE:
      pop()
      #Colocamos la estructura del LEE #Estructura de LEE
      if 'LEE' in line and flagPROG:
        flagLEE=True
        push('LEE')
        continue
      if inspect()=='LEE':
        if '[id]' in line:      
          pop()
          flagLEE=False
          continue
        else:
          print('Error de compilacion')
          flagError=True
          break


if isEmpty() and not(flagError):
  print('Compilación exitosa')





