#El método init/self, es un método constructor. Básicamente sirve para adjudicar valores. Normalmente tu le otrogas un valor a una variable, pero en el caso de que no lo hagas tomará el valor inicial que le de el __init__
#Para utilizar este método, primero crearemos una clase, y dentro definiremos varias funciones. En el caso de que denrto de dichas funciones añadamos variables, habrá que colocar el nombre de diccha variable al lado del self.

#Creamos una clase, ya que todas las funciones que se encuentran dentro de la clase texto, van a definir al texto en si.

class Texto:

    def __init__(self,texto):
        self.texto = texto


    def intro (self,lista,palabraapalabra,letra):
        lista = []
        for palabraapalabra in range ():
            letra = self.texto[palabraapalabra]
            if letra in texto =="#":
                %/
texto = "#mira como se mueve aquella banderola -dijo un monje#lo que se mueve es el viento -respondió otro monje#ni las banderolas ni el viento, lo que se mueve son vuestras mentes -dijo el maestro"