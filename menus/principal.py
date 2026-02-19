from clases.ejercicio1_poo import Ejercicio1
from clases.ejercicio2_poo import Ejercicio2
from clases.ejercicio3_poo import Ejercicio3
from clases.ejercicio4_poo import Ejercicio4
from clases.ejercicio5_poo import Ejercicio5
from clases.ejercicio6_poo import Ejercicio6
from clases.ejercicio7_poo import Ejercicio7
from clases.ejercicio8_poo import Ejercicio8
from clases.ejercicio9_poo import Ejercicio9
from clases.ejercicio10_poo import Ejercicio10
from clases.ejercicio11_poo import Ejercicio11


def menu_principal():
    while True:
        print("Menú principal")
        print("1.- Ejercicio 1")
        print("2.- Ejercicio 2")
        print("3.- Ejercicio 3")
        print("4.- Ejercicio 4")
        print("5.- Ejercicio 5")
        print("6.- Ejercicio 6")
        print("7.- Ejercicio 7")
        print("8.- Ejercicio 8")
        print("9.- Ejercicio 9")
        print("10.- Ejercicio 10")
        print("11.- Ejercicio 11")
        print("12.- Salir")
        op = int(input("Elija opcion: "))
        match(op):
            case 1:
                #ejercicio_1()
                test= Ejercicio1()
                test.leerDatos()
                test.realizarCalculo()
                test.mostrarResultado()
            case 2:
                #ejercicio_2()
                test= Ejercicio2()
                test.leerDatos()
                test.realizarCalculo()
                test.mostrarResultado()
            case 3:
                #ejercicio_3()
                test= Ejercicio3()
                test.leerDatos()
                test.realizarCalculo()
                test.mostrarResultado()
            case 4:
                #ejercicio_4()
                test= Ejercicio4()
                test.leerDatos()
                test.realizarCalculo()
                test.mostrarResultado()
            case 5:
                #ejercicio_5()
                test= Ejercicio5()
                test.leerDatos()
                test.realizarCalculo()
                test.mostrarResultado()
            case 6:
                #ejercicio_6()
                test= Ejercicio6()
                test.leerDatos()
                test.realizarCalculo()
                test.mostrarResultado()
            case 7:
                #ejercicio_7()
                test= Ejercicio7()
                test.leerDatos()
                test.realizarCalculo()
                test.mostrarResultado()
            case 8:
                #ejercicio_8()
                test= Ejercicio8()
                test.leerDatos()
                test.realizarCalculo()
                test.mostrarResultado()
            case 9:
                #ejercicio_9()
                test= Ejercicio9()
                test.leerDatos()
                test.realizarCalculo()
                test.mostrarResultado()
            case 10:
                #ejercicio_10()
                test= Ejercicio10()
                test.leerDatos()
                test.realizarCalculo()
                test.mostrarResultado()
            case 11:
                #ejercicio_11()
                test= Ejercicio11()
                test.leerDatos()
                test.realizarCalculo()
                test.mostrarResultado()
            case 12:
                break
            case _:
                print("Opcion no válida")
            