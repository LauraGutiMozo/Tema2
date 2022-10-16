def modificador(lista):
    lista_sin_dupli = list(set(lista)) #Borrar los elementos duplicados.
    lista_ordenada = lista_sin_dupli.sort()#Ordenar la lista de mayor a menor.
    #Eliminar todos los números impares.
    for elemento in lista_ordenada:
        lista_pares=[]
        if elemento % 2 == 0:
            lista_pares.append(elemento)
            print(lista_pares)
    #Realizar una suma de todos los números que quedan.
    for elemento in lista_pares:
        sumatorio = sum(lista_pares)
        print(sumatorio)
    #Añadir como primer elemento de la lista la suma realizada.
    lista_pares.insert (0,sumatorio)
    #Devolver la lista modificada.
    return lista
    print(lista_pares)

#Finalmente, después de ejecutar la función, comprueba que la suma de todos los números a partir del segundo, concuerda con el primer número de la lista, tal que así:
def comprobador():
    nueva_lista = modificador(lista)
    print( nueva_lista[0] == sum(nueva_lista[1:]) )
    True