#Sueldos en una empresa
sueldo1=0
sueldo2=0
total=0
while(True):
    sueldo=int(input("Cual es el sueldo del trabajador: $"))
    
    if sueldo==-1:
        break
    if sueldo >= 500000 and sueldo <= 900000:
        sueldo1 = sueldo1 + 1
    else:
        if sueldo > 900000:
            sueldo2 = sueldo2 + 1
    total = total + sueldo 
print("Hay",sueldo1,"trabajadores con sueldo entre los $500000 y $900000 ")
print("Hay",sueldo2,"trabajadores con sueldo superior a los $900000 ")
print("El total de gastos por sueldos es de: $",total)
