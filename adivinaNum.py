import random

contadorIntentos = 3

#--- y el jugador 2 es la maquina, asi que genero el random
maquina = random.randint(0, 100)
print("_>>> Para comprobar que funciona...vemos el numero que se genera: ", maquina)
HasAcertado = False

def numeroCorrecto(respuesta):
    global contadorIntentos

    if respuesta == maquina:
        print("HAS ACERTADO :)")
        return True
    else:
        contadorIntentos-=1
        print("Los siento, intentalo de nuevo")
        return False


def comoDeCerca(quieresPista):
    if respuesta > maquina:
        print("debes introducir un numero menor")
    elif respuesta<maquina:
        print("debes introducir un numero mayor")

while HasAcertado == False and contadorIntentos>0:
    respuesta = int(input("Adivina el numero: "))
    HasAcertado = numeroCorrecto(respuesta)

#while HasAcertado == False and contadorIntentos>0:
    #respuesta = int(input("Adivina el numero: "))


    #if respuesta == maquina:
        #HasAcertado = True
        #print("HAS ACERTADO :)")
    #else:
        #contadorIntentos-=1
        #print("Los siento, intentalo de nuevo")
    
    #if contadorIntentos == 0:
        #print("---------------------------\nSe te han acabado los intentos")

