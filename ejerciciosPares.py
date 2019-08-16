
primerNum = int(input("Introduzca el primer valor: "));
segundoNum = int(input("Introduzca el segundo valor: "));

#defino 'a' como el numero menor, y 'b' como el de maypr valor
if primerNum < segundoNum:
    numeroMenor = primerNum;
    numeroMayor = segundoNum;
else:
    numeroMenor = segundoNum;
    numeroMayor=primerNum;

#comienzo a contar en ese rango los pares
"""  
contadorPares = 0;
for i in range(numeroMenor, numeroMayor + 1): #le sumo 1, porque si el segundo numero fuese par, no llegaria a contarlo
    if i % 2 == 0:
        contadorPares += 1;
        print(f"El número {i} es par.");
    else:
        print(f"El número {i} es impar.");
print("En el rango: " , numeroMenor , "-" , numeroMayor ," hay " , contadorPares , " numeros pares");
"""

#mismo ejercicio con WHILE
#"""
contPares = 0;
while numeroMenor <= numeroMayor:
    if numeroMenor % 2 == 0:
        contPares += 1;
    numeroMenor +=1;
print("\n 2- En el rango: " , numeroMenor , "-" , numeroMayor ," hay " , contPares , " numeros pares");
#"""

#Esta es otra forma de hacerlo
#Se ve el uso con "PASO" y el continue
"""  
num1 = int(input("Introduzca el primer valor: "));
num2 = int(input("Introduzca el segundo valor: "));
cont = 0;
paso = 1;
if num1 > num2:
    paso = -1;

    for numero in range ( num1, num2 + paso, paso):
        if numero == 0:
            continue;
        if numero % 2 == 0:
            cont +=1;
print(f"Hay {cont} numeros pares")
"""

i = numero1;
while i <=numero2:
    if i ==0:
        i+=paso;
        continue;
    if i%2==0:
        