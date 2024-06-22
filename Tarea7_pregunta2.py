lista_n=[]
lista_p=[]
while True:
    palabra=input("Ingrese una palabra: ")
    if palabra=="":
        break
    lista_p.append(palabra)
    cantidad=0
    for letra in palabra:
        if letra == 'a' or letra == 'A':
            cantidad = cantidad + 1
    lista_n.append(cantidad)
for x,y in zip(lista_p,lista_n):
    print()
    print("La palabra",x,"contiene",y,"de caracteres 'a'A' en total.")
