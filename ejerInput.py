# --- ejercicio de INPUT + Distintas maneras de imprimir en pantalla
nombre = input("Dime tu nombre: ");
edad = input("Edad: ");
print("---------------------------------")

#1 - normal con + y comillas
print("1- Hola, "+nombre+ " tienes " + edad + " años");

#2 - esta sería necesaria si trato el dato edad como int, porque tengo que pasarlo a string como el resto si uso (+)
    # si hubiera tratado: edad=int(input("Edad: "));
print("2- Hola "+nombre+ " tienes " + str(edad) + " años");

#3 - con comas (,) no tengo que volver a pasar a string como en el anterior
print("3- Hola, ", nombre, " tienes ", edad, " años");

#4
print(f"4- Me alegro de conocerle, {nombre}, tienes {edad} años.")