def primera_funcion(): 
    altura = float(input("favor de escribir su estatura en metros:"))
    peso = float(input("favor de escribir su peso en kilogramos:"))

    x = peso /  altura ** 2  
    print(x)

    if (x >= 0 ) and (x<= 18.9 ):
        print('Su IMC esta por debajo de lo normal.')
    if (x >= 19) and (x<=24.9 ):
        print('Su IMC esta en nivel normal.')
    if (x >= 25) and (x<=29.9 ):
        print('Su IMC esta por encima de lo normal.')
    if (x>=30 ):
        print('Su IMC indica obesidad, favor de ir a con un médico.')
    
primera_funcion()