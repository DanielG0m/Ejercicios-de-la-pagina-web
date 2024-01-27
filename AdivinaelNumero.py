import os
from random import randrange
n = randrange(101)
i=1
titulo="""

        Adivina el numero!

"""
opciones=("1. Adivina mi numero\n2. Adivinare tu numero\n3. Salir ")
while True:
    print(titulo)
    print(opciones)
    op = int(input(">. "))

    if op == 1:
        while True:
            print("Adivine el numero. ")
            intento= int(input(f"Intento {i}: "))
            if intento < n:
                print(f"Es mayor que {intento}")
            elif intento > n:
                print(f"Es menor que {intento}")
            else:
                print(f"Correcto. Adivinaste en {i} intentos")
                os.system('pause')
                os.system('cls')
                break
            i+=1

    elif op == 2:
        while True:
            m=randrange(101)
            print(f"Intento {i}:",m)
            print("Ingresa < , >, = ")
            s=input()
            if s == "=":
                print(f"Adivine en {i} intentos B-)")
                os.system('pause')
                os.system('cls')
                break
            i+=1
    elif op == 3:
        break   
