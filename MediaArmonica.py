def media_armonica(n):
    suma=sum(1/x for x in n)
    return len(n) / suma

n = int(input("cuentos numeros: "))
i = 1;
lista = []
while i <= n:
    numeros = int(input(f"ingrese numero {i}: "))
    lista.append(numeros)
    i +=1 
resultado= media_armonica(lista)
print(resultado)
