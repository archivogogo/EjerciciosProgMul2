
# Importamos el modulo de math que nos permite introducir funciones matematicas 
import math

# Preguntamos al usuario una cantidad numerica en una variable

x = int(input('favor de escribir una cantidad de dinero en numeros:'))

# Creamos una funcion que reciba x, la cual fue introducia por el usuario, y la esta determinando dentro de la funcion con el valor de cada denominacion de billete, condicionadola a ser redondeada por math.floor entre la denominacion de billete de mayor a menor-
# El resultado de la operacion es regresado con la leyenda de texto impresa por cada billete.
# Repetimos el mismo paso para cada denominacion de billete
# La funcion es recursiva porque cada condicional esta llamando a la misma funcion, repitiendo cada paso de la condicional segun la denominacion del billete.

def contar_dinero(y):
    if y / 1000 >= 1:
        print("Billete(s) de 1000: ", math.floor(y/1000))
        y = y%1000
        contar_dinero(y)
        return

    if y / 500 >= 1:
        print("Billete(s) de 500: ", math.floor(y/500))
        y = y%500
        contar_dinero(y)
        return

    if y / 200 >= 1:
        print("Billete(s) de 200: ", math.floor(y/200))
        y = y%200
        contar_dinero(y)
        return

    if y / 100 >= 1:
        print("Billete(s) de 100: ", math.floor(y/100))
        y = y%100
        contar_dinero(y)
        return

    if y / 50 >= 1:
        print("Billete(s) de 50: ", math.floor(y/50))
        y = y%50
        contar_dinero(y)
        return

# En esta condicional hacemos la excepción de colocar el residuo junto con la leyenda de texto
# El sobrante de y en este caso siempre sería el residuo de y / 20.

    if y / 20 >= 1:
        print("Billete(s) de 20: ", math.floor(y/20))
        y = y%20
        contar_dinero(y)
        print("El sobrante es: ", y)
        return

# Llamamos a la funcion, entregando el valor de x que fue introducido por el usuario.

contar_dinero(x)