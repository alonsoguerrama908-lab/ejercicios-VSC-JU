class Ejercicio8():
    def __init__(self):
        self.num = 0
        self.resultado = []

    def leerDatos(self):
        self.num = int(input("Ingresa un número: "))

    def realizarCalculo(self):
        # Guardamos los números impares desde 1 hasta num
        for i in range(1, self.num + 1, 2):
            self.resultado.append(i)

    def mostrarResultado(self):
        print("Números impares:", end=" ")
        for numero in self.resultado:
            print(numero, end=", ")
