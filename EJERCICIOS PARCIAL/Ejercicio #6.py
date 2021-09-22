# Creamos una variable que le pregunte al usuario por un numero

x = int(input('Favor de escribir un numero:'))

# Los numeros primos solo son divisibles entre ellos mismo y 1, asi que creamos un rango desde 2 hasta el numero preguntado, con la condicional para saber si es divisible con resido de 0, si lo es, entonces no es un numero primo y el loop se terminaria con una impresion de la leyende estableciendo que no es primo y un break.

for z in range(2,x):
    if x % z == 0:
        print(x, "no es un numero primo")
        break

# Por otro lado, si cumple con todo el for loop hasta el final, y si nos arroja residuos en la division, significa que si es un numero primo, lo cual imprimimos en el siguiente mensaje.

else:
    print(x, "es un numero primo")