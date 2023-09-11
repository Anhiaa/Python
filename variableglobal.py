ANIO = 2000
def es_bisiesto():
    global ANIO
    if ANIO % 4 == 0:
        if ANIO % 400 == 0:
            return True 
        else:
            return False
    else:
        return True
#Ejemplo de llamada a la función 
if es_bisiesto():
    print(f"{ANIO} es bisiesto")
    