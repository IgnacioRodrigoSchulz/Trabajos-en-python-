# Crear una función llamada area_circulo(radio) que devuelva el área de
# un círculo (con return) a partir de un radio. Calcula el área de un círculo
# utilizando la función a crear para un círculo de 5 de radio.

# Obs.: El área de un círculo se obtiene al elevar el radio a dos y
# multiplicando el resultado por el número Pi. Utilizar el valor 3.14159 como Pi.

def area_circulo(radio):
    area=radio**2*3.14159
    return area
area=area_circulo(5)
print("El área del círculo es de",area)