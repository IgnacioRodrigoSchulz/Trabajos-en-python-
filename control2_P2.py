lista=[]
n=0
m="Aa"
print("Ingrese 7 nombres de personas: ")
while n<7:
    nombre=input("")
    lista.append(nombre)
    n=n+1
for x in lista:
    if m == nombre[-1]:
        lista.remove(x)
print(lista)