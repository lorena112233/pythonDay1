import random
 
matriz=[]

for j in range(0,6):
    fila=[]
    for i in range(0,6):
        fila.append(random.randint(0,9))
    matriz.append(fila)
    print(matriz) #imprimo las filas en fila
    print()

for fila in matriz: 
    for valor in fila:
        print(valor, end = " ")
    print()
