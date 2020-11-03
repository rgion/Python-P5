#P5 E5 - rgion
#Escribe un programa que pida la altura y ancho de un rectángulo
#y lo dibuje de la siguiente manera:
altura=int(input("Escribe la altura del triángulo "))
anchura=int(input("Escribe el ancho del triángulo "))
for i in range(altura):
    i=" "
    for j in range(anchura):
        j="*"
        print(j,end="")
    print(i)

