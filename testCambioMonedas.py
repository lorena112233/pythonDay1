ImporteAPagar = float(input("Cuanto pagas?"))
importeCoste = float(input("Cuanto cuesta?"))
importeDevolucion = ImporteAPagar-importeCoste 
# print(importe)

# importes de los billetes y monedas con su tipo en singular
tipos = (
    (500, "billete"),
    (200, "billete"),
    (100, "billete"),
    (50, "billete"),
    (20, "billete"),
    (10, "billete"),
    (5, "billete"),
    (2, "moneda"),
    (1, "moneda")
)

centimos = (
    (0.5, "moneda"),
    (0.2, "moneda"),
    (0.1, "moneda"),
    (0.05, "moneda"),
    (0.02, "moneda"),
    (0.01, "moneda")
)

while importeDevolucion>0.4:
    if importeDevolucion >= 1:
        for tipo in tipos:
            valor = tipo[0]
            descripcion = tipo[1]

            # funcion para mostrar la s del plural si es necesario
            def s(valor, text): return valor > 1 and text+"s" or text

            if importeDevolucion/valor > 1:
                # la doble barra es para redonderar en la division, seria lo mismo que seprar los decimales
                print(int(importeDevolucion / valor), s((importeDevolucion / valor), descripcion), valor)
                # la doble barra es para redonderar en la division, seria lo mismo que seprar los decimales
                #print((b / valor), s((importe / valor), descripcion), valor)
                # la doble barra es para redonderar en la division, seria lo mismo que seprar los decimales
                print((importeDevolucion // valor), s((importeDevolucion / valor), descripcion), valor)
                # cogemos el resto de la division
                importeDevolucion = importeDevolucion % valor
                print(importeDevolucion)
    else:
        print("el importe restante es: ", importeDevolucion)
        for centimo in centimos:
            valor = centimo[0]
            descripcion = centimo[1]

            
            # funcion para mostrar la s del plural si es necesario
            def s(valor, text): return valor > 1 and text+"s" or text

            if importeDevolucion/valor > 1:
                b = abs(importeDevolucion) - abs(int(importeDevolucion))  # Parte decimal

                print((b / valor), s((b / valor), descripcion), valor)
                # cogemos el resto de la division
                importeDevolucion = b % valor




