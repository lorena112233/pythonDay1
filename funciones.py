def getMin(lista):
    numeroMin = lista[0]

    for numero in lista:
        if numero < numeroMin:
            numeroMin = numero

    return numeroMin


print(getMin([22,1,56,7,2,6,18]))