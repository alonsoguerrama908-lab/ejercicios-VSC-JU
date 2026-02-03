def ejercicio_11():
    nums= int(input("Ingrese la cantidad de numeros de la serie"))
    num1= 0
    num2= 1
    print(num1,end=",")
    print(num2,end=",")
    for i in range(nums):
        num3= num1+num2
        print(num3,end=",")
        num1=num2
        num2=num3
        
        