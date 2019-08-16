#invertir orden de string:
entrada = str(input("introduce una palabra: "))
entradaInvertida = entrada[::-1]
print(entrada,"\n------", entradaInvertida)
if entrada==entradaInvertida:
    print("Palindromo\n")
else:
    print("no es palindromo\n")

#-------------------------
length=int(len(entrada))
textoInvertido =""

iguales=True
x=int(0)
for letra in entrada:
    while iguales and (x<=length):
        if entrada[x]==entrada[length]:
            print(entrada[x], entrada[length])
            x+=1
            length-=1
        else:
            iguales=False

if iguales==False:
    print("no es palindromo")
else:
    print("SI")