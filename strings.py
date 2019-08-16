# --- Cuenta el numero de veces que se repite cada letra en la cadena de texto que introducimos por teclado
entrada=input("Introduce una palabra: ")
 
diccionario={}
for letra in entrada:
     print(letra)
for letra in entrada:
    if letra in diccionario:
        diccionario[letra]=diccionario[letra]+1
    else:
        diccionario[letra]=1
 
print(diccionario)