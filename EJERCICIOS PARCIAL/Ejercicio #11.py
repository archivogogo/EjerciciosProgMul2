#Creamos una funcion con una variable, regresamos la variable con la sentencia de un paso hacia atras, la cual hace que la variable comience desde el final y sucesivamente uno hacia el comienzo.

def regresar_texto(x):
    return x[::-1]

#Creamos otra variable que llame nuestra funcion, la cual interpretara un texto
    
texto = regresar_texto(input("favor de escribir un texto:"))

#Imprimimos el texto regresado final

print(texto)
