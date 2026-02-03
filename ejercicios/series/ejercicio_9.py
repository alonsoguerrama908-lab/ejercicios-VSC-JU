def ejercicio_9():
    cantidad = float(input("Ingrese la cantidad a invertir"))
    interes = float(input("Ingrese el interes anual"))
    años = float(input("Ingrese el numero de años"))

    vf= cantidad*(interes+1)
    print("Capital obtenido de la inversion por año",vf)
    