#P5 E3 - rgion
#Escribe un programa que pida dos números y escriba la
#suma de enteros desde el primero hasta el último.
numero1=int(input("Escribe un número "))
numero2=int(input("Escribe un número mayor que %d " %(numero1)))
suma=0
for i in list(range(numero1,numero2+1)):
    suma=suma+i
    print(suma)
print("La suma de los enteros entre ",numero1," y ",numero2," es ",suma)
