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

    for line in file:
      if(line[0] != "#"):
        if(isLine(line.split())):
          print(line, end = '')
        else:
          print('ERROR')
          break

  else:
    print('ERROR: Use a .mio file')

else:
  print('USAGE: analex <file.mio>')