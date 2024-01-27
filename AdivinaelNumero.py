from random import randrange
n = randrange(101)
numero=[]
numero2=[]
i=1
titulo="""

        Adivina el numero!

"""
print("1. Adivina mi numero\n2. Adivinare tu numero ")
op=input("Escoge una opcion: ")
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
            break
        i+=1
elif op == 2:
    adivinar= input("Ingresa el numero a adivinar: ")
    numero2.append()
    while True:
        print(f"Intento {i}:", randrange(101))
        print("Ingresa < , >, = ")
        s=input()
        i+=1