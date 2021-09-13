palabra = input("Escriba una palabra al azar:")
contarsilaba=0
for y in palabra:
      if(y=='a' or y=='e' or y=='i' or y=='o' or y=='u' or y=='A' or y=='E' or y=='I' or y=='O' or y=='U'):
            contarsilaba=contarsilaba+1
print("El numero de silabas en la palabra son: ")
print(contarsilaba)