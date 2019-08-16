#calculadora
valorParaOperar1 = float(input("Introduzca el primer valor: "))

operador = int(input("Qué operación quieres realizar?\n 0 - SUMAR\n1 - RESTAR\n2 - MULTIPLICAR\n3 - DIVIDIR: \n"))

while (operador!=0 and operador!=1 and operador!=2 and operador!=3):
    operador = int(input("Valor introducido no valido// Qué operación quieres realizar?\n 0 - SUMAR\n1 - RESTAR\n2 - MULTIPLICAR\n3 - DIVIDIR: \n"))

valorParaOperar2 = float(input("Introduzca el segundo valor: "))

if operador == 0:
    result = valorParaOperar1 + valorParaOperar2
    print("El resultado de la suma: ", valorParaOperar1, " + ", valorParaOperar2, " = ", result)
elif operador == 1:
    result = valorParaOperar1 - valorParaOperar2
    print("El resultado de la resta: ", valorParaOperar1, " - ", valorParaOperar2, " = ", result)
elif operador == 2:
    result = valorParaOperar1 * valorParaOperar2
    print("El resultado de la multiplicacion: ", valorParaOperar1, " x ", valorParaOperar2, " = ", result)
elif operador==3:
    while valorParaOperar2 ==0:
        valorParaOperar2 = float(input("División entre CERO, no valido. Introduzca otro divisor:"))
    result = valorParaOperar1 / valorParaOperar2
    print("El resultado de la division: ", valorParaOperar1, " / ", valorParaOperar2, " = ", result)
    
