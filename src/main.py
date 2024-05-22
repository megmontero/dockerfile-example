import sys 
from fibonacci import fibonacci


if (len(sys.argv) != 2):
    print("Debes especificar un único argumento con la longitud de la serie")
    exit(-1)
print(f'La serie con longitud {sys.argv[1]} es :')
print(fibonacci(length=int(sys.argv[1])))
