# Se introducen dos números, un minimo y un maximo, cada uno en su respectiva variable.

x = 25
y = 75

# Se introduce una lista de 10 números, algunos por debajo del rango de nuestras dos variables previas, algunos por encima. Debemos eliminar aquellos que se salgan de este rango.

lista_numeros = [11,22,33,44,55,66,77,88,99,111]

# Creamos una lista con una condicional, por lo qué investigué, esto se le conocé como una "list comprehension" o comprensión de listas, lo cual es una lista que lleva por dentro una condicional dentro de un loop.

lista_numeros = [z for z in lista_numeros if x < z < y]

# Al finalizar nuestra comprensión de lista, imprimimos la nueva lista sin los números que salían de rango.

print (lista_numeros)