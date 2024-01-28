x=0
y=1
z=0
while True:
    n=int(input("Ingresa un numero mayor a 1: "))
    if n>1:
        break
for i in range(1,n):
    z=x+y
    x=y
    y=z
    print(f"F{n} = {z}")
