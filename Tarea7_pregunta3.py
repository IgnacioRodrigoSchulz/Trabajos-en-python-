supermercado={}
print(" Bienvenido ")
while True:
    producto=input("Ingresa un producto: ")
    if producto=="":
        break
    precio=int(input("Cuanto vale este producto: $"))
    supermercado[producto]=precio
n=int(input("Ingresa un valor númerico por el cual multiplicar el valor de los productos: "))
f=0
for x, y in supermercado.items():
    f=y*n
    print("el producto",x,"tenia un valor de $",y,"el cual se multiplico por",n,"dando un valor final de $",f)