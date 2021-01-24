import sys
sys.path.append('src/')

from syntax import syn

file = open('{}.lex'.format(sys.argv[1]))

for line in file:
  print(line, end = '')