def new_func():

    print("piensa un numero del 1 al 100")

    minimo = 1
    maximo = 100

    while True:

        numero = (minimo + maximo) // 2

        print("tu numero es", numero, "?")

        respuesta = input("escribe mayor, menor o correcto ").lower()

        if respuesta == "correcto":
            print("adiviné")
            break

        elif respuesta == "mayor":
            minimo = numero + 1

        elif respuesta == "menor":
            maximo = numero - 1

        else:
            print("respuesta no válida")

new_func()