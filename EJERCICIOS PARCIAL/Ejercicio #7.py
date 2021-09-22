# Creamos una lista con diferentes palabras, intentando repetir una en especial.

mi_lista = ["camarones", "pulpo,", "camarones", "almejas", "camarones", "pescado", "calamari"]

# Utilizamos el modulo de "count" que nos permite contar las repeticiones de un dato dentro de una lista, y lo guarda en una variable, la cuál nombramos contar_lista.

contar_lista = mi_lista.count("camarones")

# Imprimimos la variable contar_lista, la cuál contiene el numero de veces que la palabra camaron es repetida.

print(contar_lista)