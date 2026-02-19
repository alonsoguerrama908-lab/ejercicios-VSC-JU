import math
class Ejercicio6():
    def __init__(self):
       self.num1=0
       self.num2=0
       self.distancia=0

    def leerDatos(self):
        print("DISTANCIA")
        self.num1= float(input("Escriba un número: "))
        self.num2= float(input("Escriba otro número: "))
    def realizarCalculo(self):
        self.distancia= self.num1 -self.num2
        if self.distancia<0:
            self.distancia= -self.distancia*1
    def mostrarResultado(self):        
        print("La distancia entre",self.num1,"y",self.num2,"es",self.distancia)