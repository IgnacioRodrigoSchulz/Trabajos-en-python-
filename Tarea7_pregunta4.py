deudores={}
for x in range(5):
    print("")
    rut=input("Ingrese el rut del deudor(con puntos y guion): ")
    deuda=int(input("Ahora ingrese el valor de la deuda: $"))
    deudores[rut]=deuda
while True:
    print(deudores)
    rut=input("Ingresa el rut al cual se abonara: ")
    if rut=="":
        break
    elif rut in deudores:
        print("")
        print("La deuda actual es de $",deudores[rut])
        abono=int(input("Ingresa cuanto es el abono a la deuda: $"))
        deuda = deudores[rut]-abono
        deudores[rut]=deuda
        if deudores[rut] == 0:
            del(deudores[rut])
    else:
        print("El rut esta mal ingresado o no exite en el sistema...porfavor vuelve a ingresar el rut")
    
for z,y in deudores.items():
    print()
    print("La persona con rut",z,"tiene una deuda pendiente de $",y)