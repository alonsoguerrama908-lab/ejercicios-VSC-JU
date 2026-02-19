class Ejercicio9():
    def __init__(self):
        self.cantidad=0
        self.interes=0
        self.años=0
        self.vf=0

    def leerDatos(self):
        self.cantidad = float(input("Ingrese la cantidad a invertir"))
        self.interes = float(input("Ingrese el interes anual"))
        self.años = float(input("Ingrese el numero de años"))
    def realizarCalculo(self):
        self.vf= self.cantidad*(self.interes+1)
    def mostrarResultado(self):
        print("Capital obtenido de la inversion por año",self.vf)