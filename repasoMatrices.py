import random 

lista2D = []
respuesta = int(input("Cuantas frutas quieres que haya?: "))

for j in range(0, 5): # la diferencia entre los dos numeros, indica la longitud de columna (cuantas filas van a aparecer)
    fila = []
    for i in range(0, 5): #el rango entre los dos numeros (la diferencia entre ellos) indica la longitud de fila (cuantos numeros entran en cada fila)
        fila.append('') # en este rango, indico los numeros con los que quiero que se rellene de forma random
    lista2D.append(fila)

# lista2D = [[random.randint(0, 9) for i in range(0, 6)] for j in range(0, 6)];

"""
lista2D = [ 
    [0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0]
];
"""

#lista2D = [[0] * 6] * 6;


#LAS IMPRIMO DE DIFERENTES MANERAS:
#------------------------------------
for fila in lista2D: # de esta manera, me saca la matriz en forma cuadrada, bien
    for valor in fila:
        print(valor, end = " ")
    print()
    print("---")


for i in range(0, len(lista2D)): #de esta manera, me imprime seguro un numero de ****, y pasa a otra fila
    for j in range(0, len(lista2D[i])):
        print(lista2D[i][j], end = " ")
        #print()
        print("****")
