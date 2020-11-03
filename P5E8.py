#P5 E8 - rgion
#Escribe un programa que pida la anchura de un triángulo
#y lo dibuje de la siguiente manera
altura=int(input("Escribe la altura del triángulo "))
for i in range(altura):
    print(i*"*")
    print(" ")
for i in list(range(altura,0,-1)):
    print(i*"*")
    print(" ")

