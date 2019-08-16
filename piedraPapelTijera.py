import random
from random import randint
import locale

# --- defino el array
juego = ['piedra', 'papel', 'tijera']


#--- defino contadores para cada jugador
contJugador1 = 0
contJugador2 = 0
repetir=True
nJuegos = 3
num = 0

while repetir == True:

    # --- en el bucle for, digo que se realiza 3 veces con RANGE, para que, de primeras, sean 3 veces
    for jugada in range(nJuegos):
        opciones = { 'PIEDRA': 0, 'PAPEL': 1, 'TIJERA': 2 }
        #--- para 2 jugadores: jugador 1 metro por teclado
        num = (input("0-PIEDRA\n1-PAPEL\n2-TIJERA\n"))

        if num.isalpha():
            num2 = num.upper()
            selectedOption = opciones[num2]
            print(selectedOption)
        elif num.isdigit():
            selectedOption = int(num)
        jugador1 = juego[selectedOption]

        #--- y el jugador 2 es la maquina, asi que genero el random
        jugador2 = juego[random.randint(0, 2)]

        #--- imprimo el resultado de cada jugador
        print('Jugada: ', jugada + 1, ':', jugador1, "", jugador2)

        #--- planteo con los IF los posibles resultados, primero las situacion en la que gana el jugador1
        if ((jugador1 == juego[0] and jugador2 == juego[2]) or (jugador1 == juego[1] and jugador2 == juego[0]) or (jugador1 == juego[2] and jugador2 == juego[1])):
            contJugador1+=1
            print("\tGana el jugador1")
        #--- si la primera condicion no se cumple, verifico a ver si se cumple que gane el jugador2
        elif ((jugador2 == juego[0] and jugador1 == juego[2]) or (jugador2 == juego[1] and jugador1 == juego[0]) or (jugador2 == juego[2] and jugador1 == juego[1])):
            contJugador2+=1
            print("\tGana el jugador2")
        #--- si no ha ganado ni el jugador1 ni el jugador2, entiendo que es que han quedado empatados
        else:
            print("\t>>>> EMPATE <<<<")

    # --- Comparo resultados de las 3 rondas de juego
    if contJugador1 > contJugador2: print(" \nJUGADOR1 es el ganador! ", contJugador1, " VS ", contJugador2, " puntos del jugador2")
    elif contJugador1 < contJugador2: print(" \nJUGADOR2 es el ganador! ", contJugador2, " VS ", contJugador1, " puntos del jugador1")
    elif contJugador1 == contJugador2: print(" \nHa habido un empate!", contJugador1, " // ", contJugador2)
    

    #-------------------------------------------------------------------------
    #--- Creo el la misma estructura para dar la opción de jugar una vez mas:
    #-------------------------------------------------------------------------
    opcionRepetir = { 'SI': 1, 'NO': 2 }
    # --- repetir? valoro el Boolean y cambio valor de nJuegos a 1
    jugarDeNuevo = (input("Quieres jugar otra vez?\n1-SI\n2-NO\n"))

    if jugarDeNuevo.isalpha():
        jugarDeNuevo2 = jugarDeNuevo.upper()
        jugarDeNuevo = opcionRepetir[jugarDeNuevo2]
       
    elif jugarDeNuevo.isdigit():
        jugarDeNuevo = int(jugarDeNuevo)

    else: 
        print("Valor no valido")
        break
        

    if jugarDeNuevo==1:
        nJuegos = 1 #aqui es donde le pongo que sea solo una ronda
    elif jugarDeNuevo==2:
        repetir=False


