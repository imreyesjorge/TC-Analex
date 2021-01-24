import os
import sys

# Run 'analex.py'
os.system("python src/analex/analex.py {}".format(sys.argv[1]))
aux = sys.argv[1]
aux = aux[0:-4]
os.system("python src/anasin/anasin.py {}".format(aux))