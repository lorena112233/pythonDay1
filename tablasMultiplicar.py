respuesta = int(input("dime un numero: "));
print("respuesta: ",respuesta); 
z = 1;
print("---------------------------------");
print(z," x ",respuesta,"= ", (z*respuesta)); z+=1;
print(z," x ",respuesta,"= ", (z*respuesta)); z+=1;
print(z," x ",respuesta,"= ", (z*respuesta)); z+=1;
print(z," x ",respuesta,"= ", (z*respuesta)); z+=1;
print(z," x ",respuesta,"= ", (z*respuesta)); z+=1;
print(z," x ",respuesta,"= ", (z*respuesta)); z+=1;
print(z," x ",respuesta,"= ", (z*respuesta)); z+=1;
print(z," x ",respuesta,"= ", (z*respuesta)); z+=1;
print(z," x ",respuesta,"= ", (z*respuesta)); z+=1;
print(z," x ",respuesta,"= ", (z*respuesta)); z+=1;

print("---------------------------------");
#ejemplo con while
contador = 1;
while contador <= 10:
    print("blucle WHILE: ",contador, " x ", respuesta, " = ", (contador * respuesta))
    contador+=1;

print("---------------------------------");
# rango con FOR
rango = range(1,11);
for elemento in rango:
    a = elemento * respuesta
    print("blucle FOR: ",elemento, "x", respuesta, "=", (elemento*respuesta));
