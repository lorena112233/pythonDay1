#tipo de triangulo
l1 = float(input("Introduzca el Valor Numerico del 1 Lado: "))
l2 = float(input("Introduzca el Valor Numerico del 2 Lado: "))
l3 = float(input("Introduzca el Valor Numerico del 3 Lado: "))
if l1==l2 and l2==l3:
       print("\nEl Triangulo es Equilatero")
elif l1==l2 or l1==l3 or l2==l3:
       print("\nEl Triangulo es Isoceles")
elif l1!=l2 or l1!=l3 or l2!=l3:
       print("\nEl Triangulo es Escaleno")
