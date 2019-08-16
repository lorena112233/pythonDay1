valorParaDescomponer = int(input("Introduzca el numero que quiere descomponer: "))



#x = int(2)
contador = int(0)
#while (valorParaDescomponer != 1):
 #   if(valorParaDescomponer % x == 0):
  #      print(" ", x, " ")
   #     valorParaDescomponer-valorParaDescomponer/x;
    #else:
     #   valorParaDescomponer-valorParaDescomponer +1;


for i in range(2, valorParaDescomponer):
    if valorParaDescomponer % i == 0:
        print(i, end=" ")
