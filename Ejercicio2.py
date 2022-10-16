#Escribimos el if name ==main porque estamos importando la función intro de otro módulo

print("EJERCICIO 2")

import sys		
sys.path.append("C:\Users\LAURA\Documents\GitHub\Tema2\texto.py") 

from texto import Texto

if "__name__==__main__":
    texto = "#mira como se mueve aquella banderola -dijo un monje#lo que se mueve es el viento -respondió otro monje#ni las banderolas ni el viento, lo que se mueve son vuestras mentes -dijo el maestro"
    print (Texto.intro(texto))

