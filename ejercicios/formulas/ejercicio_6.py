import math
def ejercicio_6():
  print("DISTANCIA")
  num1= float(input("Escriba un número: "))
  num2= float(input("Escriba otro número: "))
  distancia= num1 -num2
  if distancia<0:
    distancia= -distancia*1
    print("La distancia entre",num1,"y",num2,"es",distancia)