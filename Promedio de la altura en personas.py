#Promedio de la altura en personas
cont=0
suma=0
while(True):
    altura = float (input("Ingresa una altura:"))
    if (altura==0):
        break
    suma = suma + altura
    cont = cont + 1 
prom = suma / cont
print("el promedio de alturas es: ", prom)