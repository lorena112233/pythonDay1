respuesta = 1
#-------------------
def evaluacionPassed():
    if notaMedia < 5:
        print("___SUSPENSO, tendras que repetir el examen") 
    elif notaMedia>=5 and notaMedia <7:
        print("___BIEN")
    elif notaMedia>=7 and notaMedia <9:
        print("___NOTABLE")
    elif notaMedia>=9 and notaMedia <10:
        print("___SOBRESALIENTE")
    elif notaMedia==10:
        print("___MATRICULA DE HONOR")
    else:
        print("alguno de los valores introducidos no es valido. Recuerda separar los decimales por un punto (.) en lugar de una coma")
#-------------------

def calculoNotaFinal():
    notaFinal = 0.3*(notaProyecto)+0.7*(notaMedia)
    return notaFinal
#-------------------

def todoCorrecto():
    correcto = int(input("Todo correcto?\n1-SI\n2-NO"))
    if correcto == 1:
        return True
    else:
        return False
#-------------------

def MasNotas():
    respuesta = int(input("Deseas introducir otra nota?\n1-SI\n2-NO"))
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
    
    print("\nSegun las notas obtenidas en clase: ", notasClase ,"\n\tte queda una media de: ", notaMedia ,"\nJunto con la nota obtenida en el proyecto final: ",notaProyecto, "\nLa NOTA  FINAL es = ",notaFinal)
#-------------------
#-------------------

# le pregunto cuantas notas voy a tener que guardar, para no repetirle la pregunta todo el rato
numDeEjerciciosParaNota = int(input("Cuantos ejercicios has realizado?: "))

#_____Creo un array para almacenar todas las notas
notasClase = []

for i in range (0,numDeEjerciciosParaNota):
    nota = int(input("Introduce la nota: "))
    notasClase.append(nota)
print("Ha introducido las siguientes notas: ",notasClase)

if todoCorrecto():
    #__calculo la notaMediaClase()
    notaMedia = notaMediaClase(notasClase)

    notaProyecto = int(input("Introduce la nota del proyecto final: "))
    
    #__Calculo la nota final
    notaFinal = calculoNotaFinal()

else:
    while todoCorrecto()==False:
        print(notasClase)
        cambio = int(input("Que nota desea cambiar? "))
        for n, i in enumerate(notasClase):
            if i==cambio:
                #print(n) #para ver la posicion del valor que voy a cambiar
                notasClase[n]=int(input("Cual es la nota correcta?: "))
        print("Tras la correccion, las notas introducidas son las siguientes:\t", notasClase)
        
        if todoCorrecto():

            notaMedia = notaMediaClase(notasClase)
            print(notasClase, "***")

            notaProyecto = int(input("Introduce la nota del proyecto final: "))
            
            #__calculo la notaMediaClase()
            notaMedia = notaMediaClase(notasClase)
                    
            #__Calculo la nota final
            notaFinal = calculoNotaFinal()
            print(notaFinal, "####")

            
#__Muestro resultado
mostrarResultado()





