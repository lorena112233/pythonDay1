# -*- coding: utf-8 -*-;

repetir = True

while repetir == True: 
    n = input("Introduzca una letra: ") # puedo poner directamente .lower o .upper aqui, y no verificar si son mayusc o minusc
    if n == n.lower():
        if n == 'a' or n == 'e' or n == 'i' or n == 'o' or n == 'u' or n == 'á' or n == 'é' or n == 'í' or n == 'ó' or n == 'ú' or n == 'ä' or n == 'ö' or n == 'ü':
            print ("vocal & minuscula")
        else:
            print("consonante, minuscula")
    if n == n.upper():
        if n == 'A' or n == 'E' or n == 'I' or n == 'O' or n == 'U'or n == 'Á' or n == 'É' or n == 'Í' or n == 'Ó' or n == 'Ú' or n == 'Ä' or n == 'Ö' or n == 'Ü':
            print("vocal MAYUSCULA")
        else:
            print("consonante MAYUSCULA")

    #-------------------------------------------------------------------------
    #--- Creo el la misma estructura para dar la opción de jugar una vez mas:
    #-------------------------------------------------------------------------
    opcionRepetir = { 'SI': 1, 'SÍ': 1,'NO': 2 }

    jugarDeNuevo = (input("Quieres jugar otra vez?\n1-SI\n2-NO\n"))
        
    # --- si responde con letras:
    if jugarDeNuevo.isalpha():
        jugarDeNuevo2 = jugarDeNuevo.upper()
        jugarDeNuevo = opcionRepetir[jugarDeNuevo2]

    # --- si responde con numeros:
    elif jugarDeNuevo.isdigit():
        jugarDeNuevo = int(jugarDeNuevo)
        
    # --------------------------------
    #------ salgo de la repeticion
    #---------------------------------
    if jugarDeNuevo==2:
        repetir=False #Cambio el valor de repetir para que salga del bucle WHILE

##______________________________________________________________________________________
