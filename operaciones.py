import random
from random import randint

respuesta = int(input("Dime un número: "))
print("respuesta: ", respuesta)

# --- con el randrange, los numeros no se repetirian, generaria 10, y si lo ejecuto 11 veces, falla
#numRandom = int(random.randrange(1,10));

numRandom = int(random.randint(1,10))
print("numero generado RANDOM: ",numRandom)

if respuesta == numRandom:
        print("Has acertado")
while respuesta != numRandom:
        print("El numero no es correcto")
        respuesta = int(input("Introduce otro numero: "))
#--------------------------------------------------------------------
# --- sorteo de regalos ejemplo

# --- defino el array de regalos
regalos = ['sartén', 'jamón', 'mp4', 'muñeca', 'tv',
           'patín', 'balón', 'reloj', 'bicicleta', 'anillo']

# --- en el bucle for, digo que se realiza 5 veces con RANGE, y defino cuantos numeros hay (0, 9)
for sorteo in range(5):
    regalo = regalos[random.randint(0, 9)]
    print('Sorteo', sorteo + 1, ':', regalo)

#--------------------------------------------------------------------
#--- Calcular longitud a partir de Radio de circunferencia
print("\nIntroduce el radio, recuerda que los decimales se separan con un punto (.)")
radio = float(input())
pi = 3.14
length = (2 * pi * radio)
print ("La longitud de la circunferencia es:")
print (length)
print("---------------------------------")

#--------------------------------------------------------------------
#--- Calcular raiz de un numero
import math # para poder usar math.sqrt
print("Dime un número para calcular su RAIZ")
n = float(input())
print ("Su raíz es")
print (math.sqrt(n))