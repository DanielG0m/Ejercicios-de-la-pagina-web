x=input("Ingrese un numero: ")
x1=x[::-1]
if x==x1:
    print(f"{x} es palindromo")
else:
    print(f"{x} no es palindromo")