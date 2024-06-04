#Cantidad de vocales y de consonantes en cada palabra
palabra="palabra"
vocales="AEIOUaeiou"
lista=[]
lista_a=[]
lista_b=[]
while len(palabra)>0:
    cont1=0
    cont2=0
    palabra=input("Ingresa una palabra: ")
    lista.append(palabra)
    for i in palabra:
        if i in vocales:
            cont1+=1
        else:
            cont2+=1
    lista_a.append(cont1)
    lista_b.append(cont2)
lista.pop()
lista_a.pop()
lista_b.pop()
for x, w, z in zip(lista,lista_a,lista_b):
    print("La palabra",x,"contiene",w,"vocales y",z,"consonantes.")