import time, os, datetime


#saco la hora del sistema, que se actualiza constantement
a = 1 #asigno uno, de forma que no sale del bucle, y lo actualiza constantemente
while a==1:
    print(time.strftime("%X")) # Obtiene fecha y hora actual e imprime todo con %X
    time.sleep(1)
    os.system("cls")