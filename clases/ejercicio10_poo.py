class Ejercicio10():
    def __init__(self):
        self.num = 0
        self.triangulo = []

    def leerDatos(self):
        self.num = int(input("Ingrese un número entero: "))

    def realizarCalculo(self):
        for i in range(1, self.num + 1):
            self.triangulo.append("0" * i)

    def mostrarResultado(self):
        print("Triángulo:")
        for fila in self.triangulo:
            print(fila)
