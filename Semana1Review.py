import random
from random import randint
import string

operador = int(random.randint(1,4))

a = int(random.randint(1,10))
b = int(random.randint(1,10))
if(operador==1): 
    print("Adivina el resultado de la operación\t", a, " + ", b)
    resultado = (a + b)
    respuesta = int(input("Dime el resultado: "))
    if respuesta == resultado: 
        print("Muy bien")
    else: 
        print(">>> Has fallado! El resultado era: ", resultado)
elif(operador==2):
    print("Adivina el resultado de la operación\t", a, " - ", b)
    resultado = (a - b)
    respuesta = int(input("Dime el resultado: "))
    if respuesta == resultado: 
        print("Muy bien")
    else: 
        print(">>> Has fallado! El resultado era: ", resultado)
elif(operador==3):
    print("Adivina el resultado de la operación\t", a, " x ", b)
    resultado = (a * b)
    respuesta = int(input("Dime el resultado: "))
    if respuesta == resultado: 
        print("Muy bien")
    else: 
        print(">>> Has fallado! El resultado era: ", resultado)
elif(operador==4):
    print("Adivina el resultado de la operación\t", a, " / ", b)
    resultado = (a / b)
    respuesta = int(input("Dime el resultado: "))
    if respuesta == resultado: 
        print("Muy bien")
    else: 
        print(">>> Has fallado! El resultado era: ", resultado)
    