a=float(input("Ingrese a: "))
b=float(input("Ingrese b: "))

if a != 0:
    x= (-1*b)/a
    print(f"Solucion Unica {x}")
elif a == 0 and b == 0:
    print("No hay solucion unica")
else:
    print("Sin solucion")