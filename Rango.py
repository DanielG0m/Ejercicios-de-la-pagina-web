rango=[]
while True:
    i=1
    n=int(input("Cuantos valores ingresara? "))
    for i in range(n):
        i+=1
        valor=float(input(f"Valor {i}: "))
        rango.append(valor)
    print(f"El rango es {max(rango)-min(rango)}")
    break