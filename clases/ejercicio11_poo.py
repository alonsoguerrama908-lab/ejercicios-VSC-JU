class Ejercicio11():
    def __init__(self):
        self.nums = 0
        self.serie = []

    def leerDatos(self):
        self.nums = int(input("Ingrese la cantidad de numeros de la serie: "))

    def realizarCalculo(self):
        num1 = 0
        num2 = 1

        if self.nums >= 1:
            self.serie.append(num1)
        if self.nums >= 2:
            self.serie.append(num2)

        for i in range(self.nums - 2):
            num3 = num1 + num2
            self.serie.append(num3)
            num1 = num2
            num2 = num3

    def mostrarResultado(self):
        print("Serie Fibonacci:", end=" ")
        for numero in self.serie:
            print(numero, end=", ")
