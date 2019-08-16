import random
from random import randint

# --- defino el array
juego = ['piedra', 'papel', 'tijera']

#--- defino contadores para cada jugador
contJugador1 = 0;
contJugador2 = 0;
repetir=True;
nJuegos = 3;

while repetir == True:

    # --- en el bucle for, digo que se realiza 3 veces con RANGE, y defino cuantas opciones hay (0, 2) = 3 opciones (piedra, papel o tijera)
    for jugada in range(nJuegos):
        #--- para 2 jugadores, genero el random
        jugador1 = juego[random.randint(0, 2)]
        jugador2 = juego[random.randint(0, 2)]

        #--- imprimo el resultado de cada jugador
        print('Jugada: ', jugada + 1, ':', jugador1, "", jugador2)

        #--- planteo con los IF los posibles resultados, primero las situacion en la que gana el jugador1
        if ((jugador1 == juego[0] and jugador2 == juego[2]) or (jugador1 == juego[1] and jugador2 == juego[0]) or (jugador1 == juego[2] and jugador2 == juego[1])):
            contJugador1+=1;
            print("\tGana el jugador1");
        #--- si la primera condicion no se cumple, verifico a ver si se cumple que gane el jugador2
        elif ((jugador2 == juego[0] and jugador1 == juego[2]) or (jugador2 == juego[1] and jugador1 == juego[0]) or (jugador2 == juego[2] and jugador1 == juego[1])):
            contJugador2+=1;
            print("\tGana el jugador2");
        #--- si no ha ganado ni el jugador1 ni el jugador2, entiendo que es que han quedado empatados
        else:
            print("\t>>>> EMPATE <<<<");
    # --- Comparo resultados de las 3 rondas de juego

    if contJugador1 > contJugador2: print(" \nJUGADOR1 es el ganador! ", contJugador1, " VS ", contJugador2, " puntos del jugador2");
    elif contJugador1 < contJugador2: print(" \nJUGADOR2 es el ganador! ", contJugador2, " VS ", contJugador1, " puntos del jugador1");
    elif contJugador1 == contJugador2: print(" \nHa habido un empate!", contJugador1, " // ", contJugador2);
    
    jugarDeNuevo = int(input("Quieres jugar otra vez?\n1-SI\n2-NO\n"));
    if jugarDeNuevo==1:
        nJuegos = 1;
    elif jugarDeNuevo==2:
        repetir=False;

