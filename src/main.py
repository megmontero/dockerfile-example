import  os
from fibonacci import fibonacci


LENGTH = os.getenv('LENGTH')

if (not LENGTH):
    print("Debes especificar la longitud de la serie en la variable LENGTH")
    exit(-1)
print(f'La serie con longitud {LENGTH} es :')
print(fibonacci(length=int(LENGTH)))
