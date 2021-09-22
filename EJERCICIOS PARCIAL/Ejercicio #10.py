# Importamos el modulo de DateTime, que nos otorga diferentes modulos para trabajar con fechas y lapsos de tiempo.

import datetime

# Creamos dos variables, una que le pregunte la hora actual al usuario, para recibir dicha hora
# Y la segunda variable, x, actualiza a la variable previa, que otorga la fecha y hora actual.

x = float(input("Favor de escribir la hora actual:"))
x = datetime.datetime.now()

# Creamos la variable de cada pais y le asignamos un adelanto de horas (float) de acuerdo a la ubicación.

japon = datetime.timedelta(hours=14)
espana = datetime.timedelta(hours=7)
australia = datetime.timedelta(hours=15)
china = datetime.timedelta(hours=13)

# Imprimimos los resultados con su respectiva leyenda y la suma de cada zona horaria.

print("La hora actual es:", x)
print("La hora actual en Japon es de:", x + japon)
print("La hora actual en Espana es de:", x + espana)
print("La hora actual en Australia es de:", x + australia)
print("La hora actual en China es de:", x + china)