class Ejercicio7():
    def __init__(self):
        self.pal = ""
        self.veces = 10

    def leerDatos(self):
        self.pal = input("Ingresa una palabra: ")

    def realizarCalculo(self):
        # No hay cálculo como tal, pero mantenemos el método por estructura
        pass

    def mostrarResultado(self):
        for i in range(self.veces):
            print(self.pal)
