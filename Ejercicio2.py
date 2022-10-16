#Escribimos el if anme ==main porque estamos importando la función intro de otro módulo

print("EJERCICIO 2")

import sys		
sys.path.append("C:\Users\LAURA\Documents\GitHub\Tema2\texto.py") 

from texto import Texto

if "__name__==__main__":
    print (Texto)

