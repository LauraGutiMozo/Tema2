from audioop import add


class modificador:
    def __Init__ (self,lista):
        self.lista = lista

    def lista_sin_dupli (self):
        self.lista = list(set(self.lista)) #Borrar los elementos duplicados.
    #MÉTODO BURBUJA
    def lista_ordenada(self):
        for i in range (0, len(self.lista)-1):
            for j in range(0, len(self.lista) -i-1):
                if (self.lista[j]> self.lista[j+1]):
                    self.lista[j], self.lista[j+1]= self.lista[j+1], self.lista[j]
                    return self.lista
    #Eliminar todos los números impares.
    def eliminar (self):
        for elemento in self.lista_ordenada:
            self.lista_pares=[]
            if elemento % 2 == 0:
                self.lista_pares.append(elemento)
                return self.lista_pares
    #Realizar una suma de todos los números que quedan.
    def suma(self):
        for elemento in self.lista_pares:
            sumatorio = sum (self.lista_pares)
            return sumatorio
    #Añadir como primer elemento de la lista la suma realizada.
    def add (self):
        self.lista_pares.insert (0,self.suma)
        return self.lista_pares

#Finalmente, después de ejecutar la función, comprueba que la suma de todos los números a partir del segundo, concuerda con el primer número de la lista, tal que así:
    #def comprobador(self, lista_pares):
        #nueva_lista = modificador(self.lista_pares)
        #print( nueva_lista[0] == sum(nueva_lista[1:]) )
        #True