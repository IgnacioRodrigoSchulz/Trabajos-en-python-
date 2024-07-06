# Crear una función recursiva sumatoria(numero) que permita calcular la
# sumatoria de un número y devuelva su resultado (con return).

def sumatoria(numero):
    if numero==1:
        return 1
    else:
        return numero + sumatoria(numero-1)
numero=(10)
print("\nLa sumatoria de",numero,"es:",sumatoria(numero))



