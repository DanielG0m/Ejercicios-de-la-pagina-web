descuento=20
resultado=[]
precios =[]
n=int(input("n: "))
productos= int(input("Cantidad de productos: "))

for i in range(productos):
    precio=float(input(f"Precio producto {i+1}: "))
    precios.append(precio)

for i in range(productos-1):
    if i < n:
        resultado.append(precios[i] * (descuento/100))
    elif i>=n and i<(n+n):
        descuento1 = descuento / 2
        resultado.append(precios[i] * (descuento1/100))

print(f"Precio total: {round(sum(precios))}")
print(f"Descuentos total: {round(sum(resultado))}")
print(f"Precio final despues de aplicar el descuento: {round(sum(precios)- sum(resultado))}")