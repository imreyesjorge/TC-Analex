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

#Checar siguiente linea
def checkNextLine(line):
  next = initialStack.index(line)+1  
  if '[id]' in initialStack[next] or 'SI' in initialStack[next] or 'REPITE' in initialStack[next] or 'IMPRIME' in initialStack[next] or 'LEE' in initialStack[next]:
    push('SENTS')

  
flagPROG=False
flagID=False
flagSI=False
flagREP=False
flagIMP=False
flagLEE=False
flagError=False
flagOP_AR=False
flagOP_REL=False

for line in file:
  print(line, end = '')
  line = line.split()
  initialStack.append(line)
print()

cont=0
for line in initialStack:
  cont+= 1
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
  #Comprobamos que no haya error para continuar
  if not(flagPROG) and isEmpty():
    print('ERROR DE INICIO DE PROGRAMA')
    flagError=True
    break
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
  #Variable SENTS
  if inspect()=='SENTS':
    pop()
    push('SENT')    #Metemos variable     

  #Variable COMPARA
  if (inspect()=='COMPARA' and flagSI) or flagOP_REL:
    if '[id]' in line:      
      pop()
      flagOP_REL=True
      push('[op_rel]')
      continue
    elif inspect()=='[op_rel]' and '<' in line and flagSI and flagOP_REL:    
      flagOP_REL=False
      pop()
      push('ELEM')      
    else:
      print('ERROR DE COMPARA')
      flagError=True
      break

  #Controlador de op_ar
  elif flagOP_AR and '[op_ar]' in line and flagREP and flagPROG:
    push('ELEM')
    continue

  #Variable ELEM
  elif inspect()=='ELEM':
    if '[val]' in line or '[id]' in line:
      pop()
      if not(flagSI):
        checkNextLine(line)
      next = cont        
      if '[op_ar]' in initialStack[next] and flagPROG:   
        flagOP_AR=True
        continue
      else:
        flagID=False
        continue
    else:
      print('ERROR DE ELEM')
      flagError=True
      break

  #Variable SENT 
  elif inspect()=='SENT' or flagID or flagSI or flagREP or flagIMP or flagLEE:
    print(line)
    if ('=' in line and inspect()=='=' and flagID and flagPROG) or flagID and inspect()=='SENT' and not(flagIMP):
      pop()      
      flagID=False

    elif ('[id]' in line and inspect()=='SENT') and not(flagIMP):
      flagID=True
      pop()      
      push('ELEM')
      push('=')
      continue

    elif 'SI' in line or flagSI and not(flagIMP) and not('IMPRIME' in line) and not('LEE' in line) and not('REPITE' in line):      
      #Colocamos la estructura del SI #Estructruta de SI ENTONCES SINO FINSI
      if 'SI' in line and flagPROG and inspect()=='SENT':
        pop()
        flagSI=True
        push('FINSI')
        push('SENTS')     #Metemos variable
        push('ENTONCES')
        push('COMPARA')   #Metemos variable
        continue
      if inspect()=='ENTONCES' and flagSI and flagPROG:
        if 'ENTONCES' in line:          
          pop()
          continue
        else:
          print('ERROR DE COMPILACION')
      if 'SINO' in line and flagSI and flagPROG:    
        push('SENTS')     #Metemos variable 
        continue
      if flagSI and inspect()=='FINSI' and flagPROG:
        if 'FINSI' in line:
          pop()
          checkNextLine(line)
          if not('FINSI' in actualStack):
            flagSI=False
            continue
          else:
            continue
        else:
          print('ERROR DE COMPILACION')

    elif 'REPITE' in line or flagREP and not(flagIMP) and not('IMPRIME' in line) and not('LEE' in line): 
      #Colocamos la estructura del REPITE #Estructura de REPITE VECES FINREP
      if 'REPITE' in line and flagPROG and inspect()=='SENT':
        pop()
        flagREP=True
        push('FINREP')
        push('SENTS')     #Metemos variable
        push('VECES')  
        push('ELEM')      #Metemos variable
        continue 
      if inspect()=='VECES' and flagREP and flagPROG:
        if 'VECES' in line:          
          pop()
          continue
        else:
          print('ERROR DE COMPILACION')
      if inspect()=='FINREP' and flagREP and flagPROG:
        if 'FINREP' in line:
          pop()
          checkNextLine(line)
          if not('FINREP' in actualStack):
            flagREP=False
            continue
          else:
            continue
        else:
          print('ERROR DE COMPILACION AQUI')
          break

    elif 'IMPRIME' in line or flagIMP:
      #Colocamos la estructura del IMPRIME #Estructura de IMPRIME
      if 'IMPRIME' in line and flagPROG and inspect()=='SENT':
        pop()
        flagIMP=True
        push('IMPRIME')
        continue
      if inspect()=='IMPRIME' and flagIMP:
        if '[text]' in line:
          flagIMP=False
          pop()
          checkNextLine(line)
          continue
        elif '[id]' in line or '[val]' in line:
          pop()
          push('ELEM')    #Metemos variable 
          flagIMP=False
          pop()
          checkNextLine(line)
        else:
          print('ERROR DE COMPILACION')
          flagError=True
          break

    elif 'LEE' in line or flagLEE: 
      #Colocamos la estructura del LEE #Estructura de LEE
      if 'LEE' in line and flagPROG and inspect()=='SENT':        
        pop()   
        flagLEE=True
        push('LEE')
        continue
      if inspect()=='LEE' and flagLEE:
        if '[id]' in line:              
          pop()
          flagLEE=False                 
          checkNextLine(line)
          continue
        else:
          print('Error de compilacion')
          flagError=True
          break

    else:
      print(line)
      print(inspect())
      print('ERROR DE COMPILACION en SENT')      
      break  

  else:
    print('ERROR DE COMPILACION')
    break  

if isEmpty() and not(flagError):
  print('Compilación exitosa')
else:
  print('Compilacion erronea')
