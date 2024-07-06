# Crear una función separar(lista) que tome una lista de números enteros
# y devuelva dos listas ordenadas. La primera con los números pares y la
# segunda con los números impares.

# Por ejemplo:
# pares, impares = separar([6,5,2,1,7])
# print(pares)
# print(impares)
# [2, 6]
# [1, 5, 7]
lista = [20,64,4,56,7,80,9,12,37,81,45]
def separar(lista):
    pares=[]
    impares=[]
    for x in lista:
        if x%2==0:
            pares.append(x)
        else:
            impares.append(x)
    return pares, impares
pares,impares = separar(lista)
print("\n Los numeros pares son:",pares)
print("\n Los numeros impares son:",impares)
