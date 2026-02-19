class Ejercicio1():
    def __init__(self):
        self.x=0
        self.w=0
        self.l=0
        self.f=0
        self.m=0
    def leerDatos(self):
        self.x= int(input("Ingresa x: "))
        self.w= int(input("Ingresa w: "))
        self.l= int(input("Ingresa l: "))  
    def realizarCalculo(self):
        self.m= self.x*self.w*(self.l-self.x)/self.l
    def mostrarResultado(self):
        print(self.m)