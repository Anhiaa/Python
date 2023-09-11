anio = int(input("Ingrese el año: "))

if anio % 4 == 0:
    if anio % 400 == 0:
        print(anio, "es un año bisiesto")
    else:
        print(anio, "no es un año bisiesto")
else:
    print(anio, "es un año bisiesto")
    
