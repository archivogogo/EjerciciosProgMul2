# Creamos una lista con las denominaciones requeridas de mayor a menor.

denominaciones = [1000, 500, 200, 100, 50, 20]

# Creamos una variable que le pide al usuario ingresar una cantidad numerica.

x = int(input('favor de escribir una cantidad de dinero en numeros:'))

# Creamos un loop, que itera cada denominacion en la lista
# Cantidad calcula el residuo de la variable x al ser dividida por cada iteracion de billete
# Asignamos un valor actualizado de la variable x que es la reste entre la previa variable x, por el resultado de la multiplicacion de cada iteracion de billete, por la variable de cantidad.
# Al finalizar imprimimos el resultado de la variable cantidad, con la leyenda de billetes, con cada iteración de denominación que conforman los billetes.
# Por ultimo, imprimimos el sobrante que en este contexto seria en monedas, dividiendo la variable introducida entre la ultima denominacion.

for billete in denominaciones:
  cantidad = x // billete
  x = x - (billete * cantidad)
  print((cantidad, "billete(s) de ", billete))

print("El sobrante es:", x%20)