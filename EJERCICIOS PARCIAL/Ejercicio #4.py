# Creamos nuestra lista llamada caracteres, ingresamos datos aleatorios incluyendo una letra "e".

caracteres = ["a", 5, "e", 8]

# Creamos nuestra funcion, que realiza la acción de darle un nuevo valor al indice en el espacio #2 el cuál le pertenece a la letra "e", lo cuál la transforma al número 3.

def cambiar_caracteres():
    caracteres[2] = 3
    return(caracteres)

# Imprimimos el llamado a nuestra función, el cuál nos regresa la lista modificada.

print(cambiar_caracteres())