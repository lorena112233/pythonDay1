#invertir orden de string:
entrada = str(input("introduce una palabra: "))[::-1]
print(entrada,"\n------")

#-----------
desplazamiento=len(entrada)
textoInvertido =""
list=[]
for letra in entrada:
    list.append(letra)
    posicion = entrada.index(letra)
    print("\t",len(entrada))
    print(posicion)
    nuevaPosicion = posicion + desplazamiento
    #aqui defino lo que pasa cuando la posicion es mayor que la length del abecedario, que vuelva a empezar
    while nuevaPosicion >= len(entrada):
        nuevaPosicion = abs(len(entrada)-nuevaPosicion)


        textoInvertido+=entrada[nuevaPosicion]
    else: #Si pongo una coma, o un espacio, no traduce, lo respeta, porque no esta en el abecedario
        textoInvertido+=letra

print(textoInvertido)
#-------------------------------------
iguales=True
x=0
for letra in entrada:
    while True and (x<=desplazamiento):
        if entrada[x]==entrada[-1]:
            print(entrada[x], entrada[-1])
            x+=1
        else:
            iguales=False

if iguales==False:
    print("no es palindromo")
else:
    print("SI")