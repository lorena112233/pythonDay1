
# ________________________________________________________

ImporteAPagar = int(input("Cuanto cuesta?"))
importePagado = int(input("Con cuánto paga?"))
importeADevolver = (ImporteAPagar - importePagado)

# importes de los billetes y monedas con su tipo en singular
tipos = (
    (500,"billete"),
    (200,"billete"),
    (100,"billete"),
    (50,"billete"),
    (20,"billete"),
    (10,"billete"),
    (5,"billete"),
)

for tipo in tipos:
    valor=tipo[0]
    descripcion=tipo[1]
 
    # funcion para mostrar la s del plural si es necesario
    s=lambda valor,text: valor > 1 and text+"s" or text
 
    if importeADevolver/valor>0:
        print((importeADevolver / valor), s((importeADevolver / valor),descripcion), valor)
        # cogemos el resto de la division
        importeADevolver = importeADevolver % valor

print(importeADevolver)