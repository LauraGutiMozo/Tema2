Crea los puntos A(2, 3), B(5,5), C(-3, -1) y D(0,0) e imprimelos por pantalla.
Consulta a que cuadrante pertenecen el punto A, C y D.
Consulta los vectores AB y BA.
(Optativo) Consulta la distancia entre los puntos 'A y B' y 'B y A'.
(Optativo) Determina cual de los 3 puntos A, B o C, se encuentra más lejos del origen, punto (0,0).
Crea un rectángulo utilizando los puntos A y B.
Consulta la base, altura y área del rectángulo.

#El método constructor, es un metodo especial para crear e inicializar un objeto creado a partir de una clase
#ASÍ QUE SIEMPRE QUE TE DIGAN DE UTILIZAR EL MÉTODO CONSTRUCTOR, ES CREAR UNA CLASE, Y DENTRO DE ESTA UN INIT
class rectangulo:
    def __init__(self, inicialx, inicialy, finalx, finaly):
        self.inicialx = inicialx
        self.inicialy = inicialy
        self.finalx = finalx
        self.finaly = finaly
    def __str__ (self):
        puntoinicial = f"({self.inicialx} , {self.inicialy})"
        puntofinal = f"({self.finalx} , {self.finaly})"
        return puntoinicial, puntofinal

    def base(self):
        base = self.finalx - self.inicialx
        return base

    def altura (self):
        altura = self.finaly - self.fianlx
        return altura

    def area (self):
        area = self.base * self.altura
        return area



