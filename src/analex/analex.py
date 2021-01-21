import sys
sys.path.append('src/')

from syntax import syn

# Check correct usage
if(len(sys.argv) == 2):

  # Check if it is a '.mio' file
  if(sys.argv[1].split('.')[1] == 'mio'):
    fileLex = open('{}.lex'.format(sys.argv[1].split('.')[0]), 'w+')
    fileSim = open('{}.sim'.format(sys.argv[1].split('.')[0]), 'w+')

    print(syn['RES'])

  else:
    print('ERROR: Use a .mio file')

else:
  print('USAGE: analex <file.mio>')