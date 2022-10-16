from math import sqrt

class punto:
    def __init__ (self,x,y):
        self.x = x
        self.y = y
    def __str__ (self):
        coordenadasA = f"({self.x},{self.y})"
        return coordenadasA
    def cuadrante (self):
        cuadrante = None
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
        elif self.x != 0 and self.y == 0:
            cuadrante = "Sobre el ejer x"
        elif self.x == 0 and self.y != 0:
            cuadrante = "Sobre el ejer y"
        return cuadrante

    def vector(self):
        c = int(input("Introduce la coordenada X del vector B"))
        d = int(input("Introduce la coordenada Y del vector B"))
        #El nuevo vector será la resta del vector A (que es el original) y el vector B

        self.vector_x= c - self.x
        self.vector_y = d -self.y
    def __str__ (self):
        coordenadasBA = f"({self.vector_x},{self.vector_y})"
        return coordenadasBA

    def distancia (self):
        distanciaAB = math.sqrt(((self.vector_x**2) + (self.vector_y**2)))
        return distanciaAB
