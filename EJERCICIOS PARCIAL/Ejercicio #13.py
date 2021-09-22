# Se introduce una variable que reciba un número entero por parte del usuario.

x = int(input('favor de escribir un año:'))

# Se escriben una serie de condicionales que cumplan con las caracteristicas de un año bisiesto las cuales son: ser divisible por cuatro, cien o el multiplo de cuatro por cien y no dejar residuo. 

if (x%4) == 0:
    if (x%100) == 0:
        if (x%400) == 0:
            print("El año:", x, "es bisiesto.")
else:
    print("El año:", x, "no es bisiesto.")

# En caso de que el año introducido deje residuo en alguna de las primeras tres condicionales, el programa le indicará al usuario que no es bisiesto.2