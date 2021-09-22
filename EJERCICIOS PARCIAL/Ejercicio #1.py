# Se escribe una variable de dato int con función input para pedirle al usuario que escriba un número de días.

x = int(input('Favor de escribir un número de días:'))

# Se presenta otra variable con la operación matematica que multiplica el número de segundos en un día por la cantidad de días que escribio el usuario.

y = x * 8600

# Se presenta otra variable con la operación matematica que multiplica el número de minutos en un día por la cantidad de días que escribio el usuario.

z = x * 1440 

# Se entrega el resultado en una función print que denota el número de días y el número de segundos en el día, utilizando las variables previas.

print('En',x,'días hay:',z,'minutos '  "y",y, 'segundos.')