listAbecedario = [ "a","b","c","d","e","f","g","h","i","j","k","l","m","n","ñ","o","p","q","r","s","t","u","v","w","x","y","z" ]

desplazamiento = 60

respuesta = str(input("Que quieres traducir?: "))
textoCifrado = ""

for letra in respuesta:
    if letra in listAbecedario:
        posicion = listAbecedario.index(letra)
        nuevaPosicion = posicion + desplazamiento

        #aqui defino lo que pasa cuando la posicion es mayor que la length del abecedario, que vuelva a empezar
        while nuevaPosicion >= len(listAbecedario):
            nuevaPosicion = abs(len(listAbecedario)-nuevaPosicion)


        textoCifrado+=listAbecedario[nuevaPosicion]
    else: #Si pongo una coma, o un espacio, no traduce, lo respeta, porque no esta en el abecedario
        textoCifrado+=letra

print(textoCifrado)

#----------------------------------------------------------------------