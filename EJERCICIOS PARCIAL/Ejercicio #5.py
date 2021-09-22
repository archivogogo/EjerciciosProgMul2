# Creamos una variable donde se le pida al usuario introducir un numero

x = int(input("Favor de escribir un numero:"))

# Nuestra segunda variable crea una lista multiplicada del numero introducido por el usuario, multiplicado por el mismo. 

y = [x] * x

# Creamos una ultima variable que utiliza el modulo de suma que suma todos los valores dentro de la lista y

suma = sum(y)

# Finalizamos imprimiendo el resultado (variable suma) de la suma de la lista.

print(suma)