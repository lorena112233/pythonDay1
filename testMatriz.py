import random
 
def generarMapa(numeroFrutas, dimension):
    mapa = []

    for i in range(0, dimension):
        fila = []
        for j in range(0, dimension):
            fila.append(" ")
        mapa.append(fila)
    for i in range(0, numeroFrutas):
        posX = random.randint(0, dimension -1)
        posY = random.randint(0, dimension-1)
        while mapa[posY][posX]== "*":
            posX = random.randint(0, dimension -1)
            posY = random.randint(0, dimension-1)

        mapa[posY][posX]

        