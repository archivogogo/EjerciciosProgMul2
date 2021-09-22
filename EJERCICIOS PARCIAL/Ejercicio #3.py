# Introducimos una lista con 7 caracteres y le asignamos el valor de caracteres.

caracteres = ["a","b","c","d","e","f","g"]

# Creamos nuestra funcion que recibe la lista de caracteres, y calcula cuantos hay dentro de ella con la funcion integrada de len, asignandole el valor de X, que sucesivamente es impresa junto con la leyenda correspondiente.

def contar_caracteres(caracteres):
    x = len(caracteres)
    print('El número de caracteres es:', (x))   
    
# Llamamos a nuestra funcion, que envia la lista a dicha funcion

contar_caracteres(caracteres)