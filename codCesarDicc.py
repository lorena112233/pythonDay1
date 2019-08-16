#diccAbecedario = { "a":,"b","c","d","e","f","g","h","i","j","k","l","m","n","ñ","o","p","q","r","s","t","u","v","w","x","y","z" }

desplazamiento = 6
alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ".lower()
abecedario = {}

for letra in alfabeto:
    posicion = alfabeto.index(letra)
    nuevaPosicion = posicion + desplazamiento

    if nuevaPosicion >= len(alfabeto):
        nuevaPosicion=abs(len(alfabeto)-nuevaPosicion)

    abecedario.update( { letra: alfabeto[nuevaPosicion] } )

entradaUsuario = input("introduce un texto: ").lower()
textoCifrado= ""

for letra in entradaUsuario:
    if letra in list(abecedario.keys()):
        textoCifrado += abecedario[letra]

    else: #Si pongo una coma, o un espacio, no traduce, lo respeta, porque no esta en el abecedario
        textoCifrado+=letra

print(textoCifrado)

