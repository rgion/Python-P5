#P5 E4 - rgion
#Escribe un programa que pida un número y calcule su factorial.
numero=int(input("Escribe un número para calcular su factorial "))
factorial=1
for i in list(range(1,numero+1)):
    factorial=factorial*i
print("El factorial de ",numero," es ",factorial)
