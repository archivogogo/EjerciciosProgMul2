# Hacemos dos listas, la primera con algunos numeros par, e impar. La otra lista será donde pondremos los numeros par.

lista_numeros = [5,10,15,20,25,30,35,40,45]
lista_numerospar = []

# Condicional que verifica si la lista de lista_numeros tiene numeros par con un loop, si los tiene, utilizamos comprension de lista para pasarlos a la lista de numeros par.

for num in lista_numeros:
    
    if num % 2 == 0:
        
       lista_numerospar.append(num)

# Utilizamos el modulo sum para sumar todos los valores dentro de la lista de numeros par.

suma = sum(lista_numerospar)
       
# Imprimimos la variables suma para mostrar el resultado de la suma.

print(suma)
       