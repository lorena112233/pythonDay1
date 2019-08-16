class humano():
        def __init__(self,nombre, edad):
            self.nombre = nombre
            self.edad = edad

        def __eq__(self,objeto):
            if self.nombre == objeto.nombre and self.edad == objeto.edad: #Aqui estoy comparando los campos de dos objetos, si se llaman igual y tienen la misma edad, saldra que si son iguales. Pero en sí, son dos objetos diferentes
                return True
            else:
                return False

        def mayorEdad(self):
            if self.edad > 17:
                return True
            else:
                return False


miHumano1=humano("monica", 23)
miHumano2=humano("pablo", 29)
miHumano3=humano("paula", 41)

if miHumano1 == miHumano2:
    print("son iguales")
else:
    print("no son iguales")

listaTotal = []

listaTotal.append(miHumano1)
listaTotal.append(miHumano2)
listaTotal.append(miHumano3)

print(listaTotal)