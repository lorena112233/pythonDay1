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
        numero = int(input("inserta un numero // o (0) para salir"));
        if numero==0:
            break
        if es_primo(numero):
            print ("\nEl numero %s es primo" % numero)
        else:
            print ("\nEl numero %s NO es primo" % numero)
    except:
        print ("\nEl numero tiene que ser entero")