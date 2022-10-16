from cmath import sqrt
from unicodedata import numeric
import math





class punto(numeric):
    def __init__ (self,x,y):
        self.x = x
        self.y = y
    def __str__ (self):
        coordenadasA = f"({self.x},{self.y})"
        return coordenadasA
    def cuadrante (self):
        if self.x > 0  and self.y > 0:
            cuadrante = "CUADRANTE 1" 
        elif self.x > 0 and self.y < 0 :
            cuadrante ="CUADRANTE 2" 
        elif self.x < 0 and self.y > 0 :
            cuadrante ="CUADRANTE 3"
        elif self.x < 0 and self.y < 0 :
            cuadrante ="CUADRANTE 4" 
        elif self.x == 0 and self.y == 0:
            cuadrante ="LAS CORDENADAS SE ENCUENTRAN EN EL ORIGEN" 
        elif self.x != 0 and sel.y == 0:
            cuadrante = "Sobre el ejer x"
        elif self.x == 0 and sel.y != 0:
            cuadrante = "Sobre el ejer y"
        return cuadrante

    def vector(self):
        c = int(input("Introduce la coordenada X del vector B"))
        d = int(input("Introduce la coordenada Y del vector B"))
        #El nuevo vector será la resta del vector A (que es el original) y el vector B

        vector_x= c - self.x
        vector_y = d -self.y
    def __str__ (self,vector_x, vector_y):
        coordenadasBA = f"({vector_x},{vector_y})"
        return coordenadasBA

    def distancia (self, vector_x, vector_y):
        distanciaAB = sqrt((vector_x**2) + (vector_y**2))
        return distanciaAB
