#P5 E11 - rgion
#Escribe un programa que pida un número e imprima todos sus divisores.
numero=int(input("Escribe un número para obtener sus divisores "))
for i in range(numero+1):
    if ((i!=0)and(numero%i==0)):
        print(i,end=" ")

"""for i in range(1,numero+1):
       if(numero%i==0):
              print(i,end=" ")"""
