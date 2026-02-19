import math

class Ejercicio5():
    def __init__(self):
        self.opcion = ""
        self.litros = 0
        self.galones = 0
        self.pintas = 0
        self.resultado = ""

    def leerDatos(self):
        print("GALONES Y PINTAS")
        print("a. Convertir litros en galones y pintas.")
        print("b. Convertir galones y pintas en litros.")
        self.opcion = input("Elija una opción: ")

        if self.opcion == "a":
            print("Convertir litros en galones y pintas")
            self.litros = float(input("Número de litros: "))
        elif self.opcion == "b":
            print("Convertir galones y pintas en litros")
            self.galones = float(input("Número de galones: "))
            self.pintas = float(input("Número de pintas: "))

    def realizarCalculo(self):
        if self.opcion == "a":
            galones_totales = self.litros / 3.7854
            galones_enteros = math.floor(galones_totales)
            pintas = (galones_totales - galones_enteros) * 8

            self.resultado = (
                f"{self.litros} litros son "
                f"{galones_enteros} galones y {round(pintas)} pintas."
            )

        elif self.opcion == "b":
            litros = (self.galones * 8 + self.pintas) * 3.785
            self.resultado = (
                f"{self.galones} galones y {self.pintas} pintas son "
                f"{round(litros, 2)} litros."
            )
        else:
            self.resultado = "Debe escribir a o b."

    def mostrarResultado(self):
        print(self.resultado)
        print("Programa terminado")
