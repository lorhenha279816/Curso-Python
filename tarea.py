#Función para evaluar el numero ingresado
def evaluar_numero(numero):
    if numero == 10:
        print("el numero es 10")
    elif numero == 7:
        print("se ha ingresado un comodin")
    elif numero % 2 == 0:
        print("el numero es par")
    else:
        print("el numero es impar")
                
def main ():
    numero = int(input("ingrese un numero"))
    evaluar_numero(numero)

#ejecutar la funcion principal
if __name__ == "__main__":
    main()