def es_bisiesto(anio):
    if anio % 4 == 0:
        if anio % 400 == 0:
            return True
        else:
            return False
    else:
        return True
anio = 2024 # Puedes cambiar el año aquí
if es_bisiesto(anio):
    print(f"{anio} es bisiesto")
else:
    print(f"{anio} no es bisiesto")


