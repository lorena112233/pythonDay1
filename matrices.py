import random 

lista2D = []

for j in range(0, 6):
    fila = []
    for i in range(0, 6):
        fila.append(random.randint(0, 9))
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


for fila in lista2D:
    for valor in fila:
        print(valor, end = " ")
    print()

"""
for i in range(0, len(lista2D)):
    for j in range(0, len(lista2D[i])):
        print(lista2D[i][j], end = " ");
    print();
"""