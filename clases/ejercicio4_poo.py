class Ejercicio4():
    def __init__(self):
        self.GF=0
        self.GC=0
    def leerDatos(self):
        self.GF= int(input("Ingresa grados Farenheit: "))
    def realizarCalculo(self):
        self.GC= (self.GF-32)*5/9
    def mostrarResultado(self):    
        print("GF",self.GC)