# ¿Cual es el porcentaje de preguntas buenas?
preg=int(input("Ingresa cuantas preguntas son en total: "))
pregcorrectas=int(input("Ingresa cuantas preguntas del total estan correctas: "))
total=float
total= 100*pregcorrectas/preg
if total >= 95 :
    print("Nivel máximo")
else:
    if total >= 70 and total < 95:
        print("Nivel medio")
    else:
        if total >= 40 and total < 70:
            print ("Nivel Regular")
        else:
            if total < 40:
                print ("Fuera de nivel")