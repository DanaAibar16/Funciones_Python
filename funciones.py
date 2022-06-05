#crearemos nuestras propias funciones
#Area funciones
def mensaje():#declaracion de la funcion
    #cuerpo de la funcion.
    print("Estamos aprendiendo Python.")
    print("Estamos aprendiendo instrucciones basicas")
    print("Poco a poco iremos avanzando")

def suma(): 
    num1 = 5
    num2 = 7
    print(num1 + num2)

def suma_p():
    num1 = int(input("Ingrese un numero: "))
    num2 = int(input("Ingrese otro numero: "))
    print(num1 + num2)

def suma_pe(num1, num2):
    print(num1 + num2)

def sumar(num1, num2):
    resultado = num1 + num2
    return resultado

#fin area funciones

#Area principal

suma()
suma_pe(5, 7)
suma_p()
print (sumar(5, 7))


