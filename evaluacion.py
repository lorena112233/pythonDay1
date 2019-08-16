respuesta = 1

def MasNotas():
    #respuesta = int(input("Deseas introducir otra nota?\n1-SI\n2-NO"))
    if respuesta == 1:
        return True
    else:
        return False
#-------------------

def notaMediaClase(notasClase):
    suma = 0
    contadorDeEjerciciosEntregados = 0

    for i in notasClase:
        suma = suma + i
        contadorDeEjerciciosEntregados += 1
    return (suma/contadorDeEjerciciosEntregados)
    #return suma/len(notasClase)
#-------------------

def mostrarResultado():
    
    print("Segun las ",len(notasClase), " notas obtenidas en clase: ", notasClase ,"\n\tte queda una media de: ", notaMedia ,"\nJunto con la nota obtenida en el proyecto final: ",notaProyecto, "\nLa nota media de final de curso es = ",notaMediaFinal)
#-------------------



#__Calculo la media de los ejercicios de clase (70% de la nota final)
    #_____Creo un array para almacenar todas las notas
notasClase = []

    #_____En el bucle voy pidiendo por consola
while MasNotas():
    nota = int(input("Introduce la nota: "))
    notasClase.append(nota) #(.append) ==> en el bucle voy add cada nota que introduce el usuario por consola
    respuesta = int(input("Deseas introducir otra nota?\n1-SI\n2-NO"))
    MasNotas()
    #print(notasClase)
    #_____le paso el array de las notas a la funcion "notamediaClase()"
notaMedia = notaMediaClase(notasClase)

#__Pido la nota del proyecto (30% de la nota final)
notaProyecto = int(input("Introduce la nota del proyecto: "))

#__Calculo la nota final
notaMediaFinal = 0.3*(notaProyecto)+0.7*(notaMedia)



#__Muestro resultado
mostrarResultado()