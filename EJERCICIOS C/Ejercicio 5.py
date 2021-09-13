def funcion_numeros():
    lista_numeros = [5, 4, 44, 444, 4444, 4444, 3, 9]
    x = [y for y in lista_numeros if y % 2 == 0]
    print("Número pares dentro de la lista: ", x)

funcion_numeros()