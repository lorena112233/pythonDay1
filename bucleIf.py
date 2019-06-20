# bucle para diferenciar entre rangos de edad
edad = int(input("Edad: "));
print (edad, " años");
print("-----------------");
#uso una variable para definir la mayoría de edad (podria cambiar en USA)
a = 18
#la mayoria de edad la fijo yo en 65 directamente, para usar las dos maneras
if edad >= a and edad < 65:
  print("mayor de edad")
elif edad < a:
  print("menor de edad")
else:
  print("jubilado")

