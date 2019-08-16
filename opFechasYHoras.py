from datetime import datetime,  date, time, timedelta
import calendar


ahora = datetime.now()  # Obtiene fecha y hora actual
print("Fecha y Hora:", ahora)  # Muestra fecha y hora
print("Fecha y Hora UTC:",ahora.utcnow())  # Muestra fecha/hora UTC
print("Día:",ahora.day)  # Muestra día
print("Mes:",ahora.month)  # Muestra mes
print("Año:",ahora.year)  # Muestra año
print("Hora:", ahora.hour)  # Muestra hora
print("Minutos:",ahora.minute)  # Muestra minuto
print("Segundos:", ahora.second)  # Muestra segundo
print("Microsegundos:",ahora.microsecond)  # Muestra microsegundo
#-----------------------------------------------------------#
#-----------------------------------------------------------#
print("Horas:")
hora1 = time(10, 5, 0)  # Asigna 10h 5m 0s
print("\tHora1:", hora1)
hora2 = time(23, 15, 0)  # Asigna 23h 15m 0s
print("\tHora2:", hora2)

# Compara horas
print("\tHora1 < Hora2:", hora1 < hora2)  # True

print("Fechas:")
fecha1 = date.today()  # Asigna fecha actual
print("\tFecha1:", fecha1)

# Suma a la fecha actual 2 días
fecha2 = date.today() + timedelta(days=2)
print("\tFecha2:", fecha2)

# Compara fechas
print("\tFecha1 > Fecha2:", fecha1 > fecha2)  # False

#-----------------------------------------------------------#
print("\n")
#-----------------------------------------------------------#

# Asigna formato de ejemplo1
formato1 = "%a %b %d %H:%M:%S %Y"

# Asigna formato de ejemplo2
formato2 = "%d-%m-%y %I:%m %p"

hoy = datetime.today()  # Asigna fecha-hora

# Muestra fecha-hora según ISO 8601
print("Fecha en formato ISO 8601:", hoy)

# Aplica formato ejemplo1
cadena1 = hoy.strftime(formato1)  

# Aplica formato ejemplo2
cadena2 = hoy.strftime(formato2)  

# Muestra fecha-hora según ejemplo1
print("Formato1:", cadena1)

# Muestra fecha-hora según ejemplo2
print("Formato2:", cadena2)

#-----------------------------------------------------------#
#convertir una cadena a objeto:
print("\n")
#-----------------------------------------------------------#

objeto_datetime = datetime.strptime(cadena1, formato1)
print("strptime:", fecha1.strftime(formato1))

#-----------------------------------------------------------#
print("\n")
#OPERACIONES CON LAS FECHAS :
#-----------------------------------------------------------#
# Asigna datetime de la fecha actual
fecha1 = datetime.now()

# Asigna datetime específica
fecha2 = datetime(1995, 11, 5, 0, 0, 0)
diferencia = fecha1 - fecha2
print("Fecha1:", fecha1)
print("Fecha2:", fecha2)
print("Diferencia:", diferencia)
print("Entre las 2 fechas hay ", 
      diferencia.days, 
      "días y ", 
      diferencia.seconds, 
      "seg.")
#-----------------------------------------------------------#
print("\n")
#-----------------------------------------------------------#
formato_fecha = "%d-%m-%Y"
fecha_inicial = datetime.strptime("01-10-2013", 
                                  formato_fecha)
fecha_final = datetime.strptime("25-12-2013", 
                                formato_fecha)
diferencia = fecha_final - fecha_inicial
print("Fecha inicial:", fecha_inicial)
print("Fecha final:", fecha_final)
print("Diferencia:", diferencia.days, "días")
