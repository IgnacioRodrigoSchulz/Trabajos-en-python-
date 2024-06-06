#PUNTAJES DIARIO DE UN ALUMNO DE UN CURSO DE 15 DIAS
lista=[]
lista_b=[]
mayores=[]
menores=[]
dias=0
while True:
    puntaje=int(input("Ingrese el puntaje diario: "))
    lista.append(puntaje)
    dias = dias + 1
    lista_b.append(dias)
    for i in (lista):
        if i >= 70:
            mayores.append(i)
        else:
            menores.append(i)
    if dias >= 15:
        break
for x,y,w in zip(lista_b,menores,mayores):
    print("día",x,"puntaje",y,"dia",x,"puntaje",y)

