import random
from random import randint

# --- defino el array
juego = ['piedra', 'papel', 'tijera']

# --- en el bucle for, digo que se realiza 5 veces con RANGE, y defino cuantas opciones hay (0, 3) = 3 opciones
for jugada in range(1):
    jugador1 = juego[random.randint(0, 2)]
    jugador2 = juego[random.randint(0, 2)]
    print('Jugada: ', jugada + 1, ':', jugador1, "", jugador2)
    if ((jugador1 == juego[0] and jugador2 == juego[2]) or (jugador1 == juego[1] and jugador2 == juego[0]) or (jugador1 == juego[2] and jugador2 == juego[1])):
        print("Gana el jugador1");
    elif ((jugador2 == juego[0] and jugador1 == juego[2]) or (jugador2 == juego[1] and jugador1 == juego[0]) or (jugador2 == juego[2] and jugador1 == juego[1])):
        print("Ganador el JUGADOR2");
    else:
        print(">>>> EMPATE <<<<");
        
