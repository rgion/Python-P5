#P5 E9 - rgion
#Escribe un programa que pida la anchura y la altura de
#un rectángulo y lo dibuje de la siguiente manera
altura=int(input("Escribe la altura del rectángulo "))
anchura=int(input("Escribe el ancho del rectángulo "))
for i in range(altura):
    if (i==0) or (i==altura-1):
        print("{}".format("*"*(anchura)))
    else:
        print("*{}*".format(" "*(anchura-2)))


