def es_primo(numero):
    # Para que un numero sea primo:
    #   1 - divisible entre 1
    #   2 - divisible entre el mismo

    for i in range(2,numero):
        if (numero%i)==0:
            # es divisible
            return False
    return True
 
while True:
    try:
        numero = int(input("inserta un numero // o (0) para salir \t"))
        if numero==0:
            break
        if es_primo(numero):
            print ("El numero %s es primo" % numero, "\n")
        else:
            print ("\nEl numero %s NO es primo" % numero, "\n")
    except:
        print ("\nEl numero tiene que ser entero")