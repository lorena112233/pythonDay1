import string

# tipo de dato:
numero = 3
print("El tipo es: " + str(type(numero)))

# tamaño del dato
print(len("es un texto")) # 11
print(len("345345")) # 6
print(len([34, 564, 23])) # 3

#string
nombre = "marianito"
print(nombre[0]) # p
print(nombre[1:3]) # ep
print(nombre[-1]) # e

#recorrer string 1
#nombre2 = "pepe";
#for i in range(0, len(nombre2)):
#print(nombre2[i]);

#recorrer string 2
#nombre3 = "pepe";
#for letra3 in nombre3:
#print(letra3);

#modificar strings
"texto".capitalize() # Texto
"TEXTO".lower() # texto
"texto".upper() # TEXTO
"Texto".swapcase() # tEXTO

#completar un string # Mi nombre es Pepe y tengo 90 años.
print ("Mi nombre es %s y tengo %i años." % ("Pepe", 90))

# Hola Pepe
texto = "Hola {0}"
print(texto.format("Pepe"))

# Especificamos un hueco, pero sin decir de que tipo ni la posicion, se deja ahi vacio y se rellena con lo del final
"Esto es un texto {} y un numero {}".format("asd", 2)

# Obtenemos un 2 del total de letras t que hay
"texto".count("t", 0, -1)

# Obtenemos un 0 que es el indice de la primera t
"texto".find("t", 0, -1) #EL -1 es el ultimo siempre

# Recorremos el string desde el INICIO y si encontramos un t obtenemos un True / Boolean
"texto".startswith("t", 0, -1)

# Recorremos el string desde el FINAL y si encontramos un t obtenemos un True / Boolean
"texto".endswith("t", 0, -1)

#COMPROBACION
"texto".isalnum() # True si el contenido cadena es alfanúmerica
#"texto".Isalpha() # True si el contenido cadena es alfabético
#"texto".Isdigit() # True si el contenido cadena es númerico

#REEMPLAZAR
"Esto es una prueba".replace("e", "A") # Esto as una pruAba

#UNIR
# Manzana - Pera - Plátano
simbolo = " - "
secuenciaTexto = ("Manzana", "Pera", "Plátano")
print(simbolo.join(secuenciaTexto))

#SEPARAR
print("Esto es un texto con espacios".split(" "))
["Esto", "es", "un", "texto", "con", "espacios"]





