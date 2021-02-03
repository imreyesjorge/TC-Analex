import sys

sys.path.append('src/')
from syntax import *

# Check correct usage
if(len(sys.argv) == 2):

  # Check if it is a '.mio' file
  if(sys.argv[1].split('.')[1] == 'mio'):
    file = open(sys.argv[1])
    fileLex = open('{}.lex'.format(sys.argv[1].split('.')[0]), 'w+')
    fileSim = open('{}.sim'.format(sys.argv[1].split('.')[0]), 'w+')

    pidArr = []
    pvalArr = []
    idArr = []
    txtArr = []
    valArr = []
    cID = 1
    cTXT = 1

    # Lee linea por linea
    for line in file:

      # Si la linea no es un comentario, entonces
      if(line[0] != "#"):

        # Convertimos la linea (string) a un array
        thisArr = toArr(line)  

        # Checa si todas las palaras en la linea son reservadas
        if(isLine(thisArr)):

          # Checa cada palabra de la linea
          for i in thisArr:
            flag = False

            # Checa si la palabra es reservada
            if(isDefault(i)):
              if(isARI(i)):
                fileLex.write('[op_ar]\n')
              else:
                fileLex.write(i + '\n')
              continue

            # Checa si la palabra es un ID
            elif(isID(i)):
              for this in idArr:
                if(i == this[0][0]):
                  flag = True
              if(flag):
                flag = False
              else:
                pidArr.append([[i],['ID{0:0=2d}'.format(cID)]])
              fileLex.write('[id] ID' + '{0:0=2d}'.format(cID) + '\n')
              cID += 1
              idArr.append([[i],['ID{0:0=2d}'.format(cID)]])

            # Checa si la palabra es texto
            elif(isText(i)):
              txtArr.append([[i],['TX{0:0=2d}'.format(cTXT)]])
              fileLex.write('[text] TX' + '{0:0=2d}'.format(cTXT) + '\n')
              cTXT += 1

            # Checa si la palabra es numerico
            elif(isNumeric(i)):
              for this in valArr:
                if(i == this[0][0]):
                  flag = True
              if(flag):
                flag = False
              else:
                pvalArr.append([[i],[octalToDecimal(i)]])
              fileLex.write('[val]' + '\n')
              valArr.append([[i],[octalToDecimal(i)]])
        else:
          print('ERROR')
          break

    # Write <file>.sim
    fileSim.write('IDS\n')
    for i in pidArr:
      fileSim.write('{}, {}\n'.format(i[0][0], i[1][0]))

    fileSim.write('\nTXT\n')
    for i in txtArr:
      fileSim.write('{}, {}\n'.format(i[0][0], i[1][0]))

    fileSim.write('\nVAL\n')
    for i in pvalArr:
      fileSim.write('{}, {}\n'.format(i[0][0], i[1][0]))

  else:
    print('ERROR: Use a .mio file')

else:
  print('USAGE: analex <file.mio>')