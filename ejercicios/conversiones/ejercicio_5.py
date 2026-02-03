import math
def ejercicio_5():
  print("GALONES Y PINTAS")
  print("a. Convertir litros en galones y pintas.")
  print("b. Convertir galones y pintas en litros.")
  opcion= input("Elija una opción: ")
  if opcion=="a":
    print("Convertir litros en galones y pintas")
    litros= float(input("Número de litros: "))
    galones= litros/3.7854
    pintas= (galones-math.floor(galones))*8

    print(litros,"litros son",math.floor(galones),"galones y",round(pintas,),"pintas.")
  elif opcion=="b":
    print("Convertir galones y pintas en litros")
    galones= float(input("Número de galones: "))
    pintas= float(input("Número de pintas: "))
    litros= (galones*8+pintas)*3.785
    print(galones,"galones y",pintas,"pintas son",round(litros,2),"litros.")
  else:
    print("Debe escribir a o b.")
  print("Programa terminado")