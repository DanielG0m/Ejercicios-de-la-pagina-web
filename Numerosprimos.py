def ultimo_digito(x):
   x=x%10
   return x

def verificar_suma(lista_numeros):
       return sum(lista_numeros)
 
m={}
n=int(input("Ingrese un numero: "))
m.append(n)

n=ultimo_digito(n)
print(n)

suma=verificar_suma(m)
print(suma)