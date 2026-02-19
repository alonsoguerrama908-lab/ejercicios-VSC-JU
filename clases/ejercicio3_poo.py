class Ejercicio3():
    def __init__(self):
        self.millas=0
        self.kmt=0
        self.km=0
    def leerDatos(self):
        self.millas= int(input("Ingresa millas: "))
        self.kmt= 1.609344
    def realizarCalculo(self):
        self.km= self.millas*self.kmt
    def mostrarResultado(self):    
        print("km: ",self.km)