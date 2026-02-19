class Ejercicio2():
    def __init__(self):
        self.r=0
        self.c=0
    
    def leerDatos(self):
        self.r= int(input("Ingresa r: "))
    def realizarCalculo(self):    
        self.c= 2*3.14*self.r
    def mostrarResultado(self):
        print(self.c)