#------------------------------------------------------
#----------- tuplas
#------------------------------------------------------
nombres = ("pepe", "rodrigo", "josé", "manuel")
print(nombres) # ("pepe", "rodrigo", "josé", "manuel")
print(nombres[0]) # pepe
print(nombres[1:3]) # ("rodrigo", "josé")
print(nombres[-1]) # manuel
print(nombres.count("josé")) # 1 (porque solo se repite 1 vez)



#------------------------------------------------------
#----------- listas
#------------------------------------------------------
nombres = ["pepe", "rodrigo", "josé", "manuel"]
nombres[1] = "algo"
print(nombres) # ["pepe", "algo", "josé", "manuel"]

# ELIMINAR valores
nombres.pop()
print(nombres) # ["pepe", "rodrigo", "josé"]
nombres.pop(1)
print(nombres)# ["pepe", "josé"]
nombres.remove("pepe")
print(nombres) # ["josé"]

#ORDENAR la lista
nombres.reverse()
print(nombres) # ["manuel", "josé", "rodrigo", "pepe"]
nombres.sort()
print(nombres) # ["josé", "manuel", "pepe", "rodrigo"]
nombresOrdenAlfabetico = sorted(nombres)
print(nombres) # ["josé", "manuel", "pepe", "rodrigo"]
nombres.sort(reverse = True)
print(nombres) # ["rodrigo", "pepe", "manuel", "josé"]
nombres.sort(key = len)
print(nombres) # ["pepe", "josé", "manuel", "rodrigo"]

#orden alfabetico
frutas = ['pera', 'Manzana', 'fresa']
frutas.sort(key = str.lower)
print(frutas) # ["fresa", "Manzana", "pera"]

#BUSQUEDA en una lista
nombres = ["pepe", "rodrigo", "josé", "manuel"]
print(nombres.count("pepe")) # Nos da 1, porque solo hay 1 elemento
print(nombres.index("josé")) # Nos da 2, porque es el indice de "josé"

#COMPRESION de lista
alumnos = ["Ana", "Luis", "Pedro", "Marta", "Nerea", "Pablo"]
iniciales = [alumno[0] for alumno in alumnos]
print(iniciales) # ["A", "L", "P", "M", "N", "P"]

#RECORRER LISTA a traves de los indices <<< sabemos los indices y los valores de esta forma >>>
alumnos = ["Ana", "Luis", "Pedro", "Marta", "Nerea", "Pablo"]
for indice in range(0, len(alumnos)):
    print(alumnos[indice], end="\t")
    # Ana Luis Pedro Marta Nerea Pablo

#RECORRER lista a traves de los VALORES << solo los valores >>
alumnos = ["Ana", "Luis", "Pedro", "Marta", "Nerea", "Pablo"]
for valor in alumnos:
    print(valor, end="\t")
    # Ana Luis Pedro Marta Nerea Pablo

#DICCIONARIOS <<<<<
diccionarioEs = { "hola": "hola", "adiós": "adiós" }
diccionarioEn = { "hola": "hi", "adiós": "bye" }
print(diccionarioEs['hola']) # hola
print(diccionarioEn['hola']) # hi
#ACTUALIZAR diccionarios
diccionarioEn.update( { "adiós": "good bye" } )
print(diccionarioEn)


#defino otra lista y le add con .append, se van poniendo en orden.
#para insertar en una posicion concreta, uso insert
lista = []
lista.append("cereza")
lista.append("manzana")
lista.append("pera")
lista.append("melon")
lista.insert(2, "MANDARINA") #voy a insertar en la posición 2 de la lista
print(lista)