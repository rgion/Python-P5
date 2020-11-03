#P5 E2 - rgion
#Escribe un programa que pida dos números y escriba qué
#números entre ese par de números son pares y cuáles impares.
numero1=int(input("Escribe un número "))
numero2=int(input("Escribe un número mayor que %d " %(numero1)))
for i in list(range(numero1,numero2+1)):
    if(i%2==0):
        print("El número" ,i, "es par.")
    else:
        print("El número" ,i, "es impar.")
