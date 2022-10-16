from unicodedata import numeric
import math

Añade un método llamado vector, que tome otro punto y calcule el vector resultante entre los dos puntos.
(Optativo) Añade un método llamado distancia, que tome otro punto y calcule la distancia entre los dos puntos y la muestre por pantalla. La fórmula es la siguiente:

Crea una clase llamada Rectangulo con dos puntos (inicial y final) que formarán la diagonal del rectángulo.
Añade un método constructor para crear ambos puntos fácilmente, si no se envían se crearán dos puntos en el origen por defecto.
Añade al rectángulo un método llamado base que muestre la base.
Añade al rectángulo un método llamado altura que muestre la altura.
Añade al rectángulo un método llamado area que muestre el area.
Sugerencia
Puedes identificar fácilmente estos valores si intentas dibujar el cuadrado a partir de su diagonal. Si andas perdido, prueba de dibujarlo en un papel, ¡seguro que lo verás mucho más claro! Además recuerda que puedes utilizar la función abs() para saber el valor absolute de un número.
Experimentación
Crea los puntos A(2, 3), B(5,5), C(-3, -1) y D(0,0) e imprimelos por pantalla.
Consulta a que cuadrante pertenecen el punto A, C y D.
Consulta los vectores AB y BA.
(Optativo) Consulta la distancia entre los puntos 'A y B' y 'B y A'.
(Optativo) Determina cual de los 3 puntos A, B o C, se encuentra más lejos del origen, punto (0,0).
Crea un rectángulo utilizando los puntos A y B.
Consulta la base, altura y área del rectángulo.


class punto(numeric):
    def __init__ (self,x,y):
        self.x = x
        self.y = y
    def __str__ (self):
        coordenadasA = f"({self.x},{self.y})"
        return coordenadasA
    def cuadrante (self):
        if self.x == 0 or self.x > 0  and self.y > 0:
            cuadrante = "CUADRANTE 1" 
        elif self.x ==0 or self.x < 0 and self.y > 0 :
            cuadrante ="CUADRANTE 2" 
        elif self.x !=0 or self.x > 0 and self.y ==0 or self.y < 0 :
            cuadrante ="CUADRANTE 3"
        elif self.x !=0 or self.x > 0 and self.y ==0 or self.y < 0 :
            cuadrante ="CUADRANTE 4" 
        elif self.x == 0 and self.y == 0:
            cuadrante ="LAS CORDENADAS SE ENCUENTRAN EN EL ORIGEN" 
        return cuadrante

    def vector(self):
        def __init__ (self,x,y):
            self.x = x
            self.y = y
        def __str__ (self):
            coordenadasB = f"({self.x},{self.y})"
            return coordenadasB

    def distancia (self):