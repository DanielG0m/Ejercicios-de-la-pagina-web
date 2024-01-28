def es_numero_fibonacci(numero):
    if numero < 0:
        return False

    a, b = 0, 1
    while b < numero:
        a, b = b, a + b

    return b == numero

x=0
y=1
z=0
listn=[]
while True:
    n=int(input("Ingresa un numero mayor a 1: "))
    if n>1:
        break
for i in range(1,n):
    z=x+y
    x=y
    y=z
    listn.append(z)
print(f"F{n} = {z}")

try:
    numero = int(input("Ingrese un número entero: "))

    if es_numero_fibonacci(numero):
        print(f"{numero} es un numero de Fibonacci.")
    else:
        print(f"{numero} no es un número de Fibonacci.")
except ValueError:
    print("Por favor, ingrese un número entero válido.")

m=input("Ingrese m: ")
print(listn)
