#P5 E12 - rgion
#Escribe un programa que pida un número y escriba si primo o no:
numero=int(input("Dame un número: "))
esPrimo=True
for i in range(numero):
    if ((i!=0)and(i!=1)and(numero%i==0)):
        esPrimo=False
if (esPrimo):
    print("El número ",numero," es primo")
else:
    print("El número ",numero," no es primo")

