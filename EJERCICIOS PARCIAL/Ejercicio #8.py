# Creamos dos listas, una con nombres que queremos eliminar de la segunda, y la segunda con 20 nombres.
# La segunda lista solo tiene algunos de los nombres de la primera, más no todos.

nombres1 = ["alejandro", "anacleto", "berenice", "brian", "telesforo"]

nombres2 = ["alejandro", "anacleto", "berenice", "carlos", "carolina", "carmen", "diego", "donna", "eugenio", "emma", "fernando", "fernanda", "gary", "gertrudis", "hector", "hilda", "ignacio", "karla", "martha", "telesforo"]

# Creamos una variable con una condicion con un loop para checar que los nombres de la primera lista, no esten en la segunda lista.

nombres3 = [lista for lista in nombres2 if lista not in nombres1]

# Imprimimos la nueva lista sin los nombres de la primera.

print(nombres3)