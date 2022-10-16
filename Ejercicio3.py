print("EJERCICIO 3")

import sys		
sys.path.append("C:\Users\LAURA\Documents\GitHub\Tema2\modificar.py") 

from modificar import modificador
#from modificar import comprobador 

if "__name__==__main__":
    lista=[4,5,8,9,7,6]
    mod = modificador(lista)
    print(mod.lista_sin_dupli())
    print(mod.lista_ordenada())
    print(mod.eliminar())
    print(mod.suma())
    print (mod.add())

    #lista_pares = mod.add
    #comp = comprobador(lista_pares)
    #print(comp.nueva_lista())