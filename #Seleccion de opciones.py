#Seleccion de opciones
menu=int(input("Menú principal: \n 1.Ingresar un elemento a la lista \n 2.Modificar un elemento de la lista según el índice \n 3.Eliminar un elemento de la lista según el índice \n 4.Eliminar el último elemento de la lista \n 5.Buscar un elemento de la lista según el dato(devuelve el índice) \n 6.Mostrar todos los elementos de la lista \n 7.Salir \n"))
lista=[]
while menu != 7:
    if menu == 1:
        elemento=input("Ingresa un elemento a la lista: ")
        lista.append(elemento)
    elif menu == 2:
        antiguo=int(input("Que elemento se modificara(según el índice): "))
        nuevo=input("Ingresa el elemento nuevo: ")
        lista.pop(antiguo)
        lista.insert(antiguo,nuevo)
    elif menu == 3:
        eliminar=int(input("Que elemento de la lista desea eliminar(según el índice): "))
        lista.pop(eliminar)
    elif menu == 4:
        print("Se elimino el ultimo elemento de la lista...") 
        lista.pop()     
    elif menu == 5:
        buscar=input("Que elemento de la lista desea buscar(según el dato): ")
        if buscar in lista:
            print("si se encuentra",buscar)
        else:
            print("No fue posible encontrar el elemento...")
    elif menu == 6:
        print("Mostrando todos los elementos de la lista")
        print(lista)
    else:
        print("Por favor digite una opcion correcta...")    
    menu=int(input("Menú principal: \n 1.Ingresar un elemento a la lista \n 2.Modificar un elemento de la lista según el índice \n 3.Eliminar un elemento de la lista según el índice \n 4.Eliminar el último elemento de la lista \n 5.Buscar un elemento de la lista según el dato(devuelve el índice) \n 6.Mostrar todos los elementos de la lista \n 7.Salir \n"))

print("Programa finalizado...")