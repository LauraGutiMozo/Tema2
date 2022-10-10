# Tema2

Laura Gutiérrez mozo




Ejercicio 1


Ejercicio
Crea una clase llamada Punto con sus dos coordenadas X e Y.
Añade un método constructor para crear puntos fácilmente. Si no se reciben una coordenada, su valor será cero.
Sobreescribe el método string, para que al imprimir por pantalla un punto aparezca en formato (X,Y)
Añade un método llamado cuadrante que indique a qué cuadrante pertenece el punto, teniendo en cuenta que si X == 0 e Y != 0 se sitúa sobre el eje Y, si X != 0 e Y == 0 se sitúa sobre el eje X y si X == 0 e Y == 0 está sobre el origen.
Añade un método llamado vector, que tome otro punto y calcule el vector resultante entre los dos puntos.
(Optativo) Añade un método llamado distancia, que tome otro punto y calcule la distancia entre los dos puntos y la muestre por pantalla. La fórmula es la siguiente:

Nota
La función raíz cuadrada en Python sqrt() se debe importar del módulo math y utilizarla de la siguiente forma:
import math
math.sqrt(9)
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

Ejercicio 2
Utilizando todo lo que sabes sobre cadenas, listas, sus métodos internos... Transforma este texto:
un día que el viento soplaba con fuerza#mira como se mueve aquella banderola -dijo un monje#lo que se mueve es el viento -respondió otro monje#ni las banderolas ni el viento, lo que se mueve son vuestras mentes -dijo el maestro
En este otro:
Un día que el viento soplaba con fuerza...
- Mira como se mueve aquella banderola -dijo un monje.
- Lo que se mueve es el viento -respondió otro monje.
- Ni las banderolas ni el viento, lo que se mueve son vuestras mentes -dijo el maestro.
Lo único prohibido es modificar directamente el texto.

Ejercicio 3
Crea una función modificar() que a partir de una lista de números realice las siguientes tareas sin modificar la original:
Borrar los elementos duplicados.
Ordenar la lista de mayor a menor.
Eliminar todos los números impares.
Realizar una suma de todos los números que quedan.
Añadir como primer elemento de la lista la suma realizada.
Devolver la lista modificada.
Finalmente, después de ejecutar la función, comprueba que la suma de todos los números a partir del segundo, concuerda con el primer número de la lista, tal que así:
nueva_lista = modificar(lista)
print( nueva_lista[0] == sum(nueva_lista[1:]) )
True
Recordatorio
La función sum(lista) devuelve una suma de los elementos de una lista.