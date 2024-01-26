a=float(input("Ingrese a: "))
b=float(input("Ingrese b: "))

x= (-1*b)/a

if x!=0:
    print(f"Solucion Unica {x}")
elif a == 0 and b == 0:
    print("No hay solucion unica")
else:
    print("Sin solucion")