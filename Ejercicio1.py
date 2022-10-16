#Crea los puntos A(2, 3), B(5,5), C(-3, -1) y D(0,0) e imprimelos por pantalla.
#Consulta a que cuadrante pertenecen el punto A, C y D.
#Consulta los vectores AB y BA.
#Optativo) Consulta la distancia entre los puntos 'A y B' y 'B y A'.
#(Optativo) Determina cual de los 3 puntos A, B o C, se encuentra más lejos del origen, punto (0,0).
#Crea un rectángulo utilizando los puntos A y B.
#Consulta la base, altura y área del rectángulo.

print("EJERCICIO 1" )

import sys

from numpy import vectorize		
sys.path.append("C:\Users\LAURA\Documents\GitHub\Tema2\Punto.py")
sys.path.append("C:\Users\LAURA\Documents\GitHub\Tema2\rectangulo.py")

from Punto import punto

if "__name__==__main__":
    print(punto())
    print (punto.cuadrante())
    print(punto.vector())
    print(punto.distancia())

from rectangulo import rectangulo
if "__name__==__main__":
    print (rectangulo.base())
    print (rectangulo.altura())
    print(rectangulo.area())