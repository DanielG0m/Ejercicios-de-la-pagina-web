import math

def es_primo(numero):
    if numero <=1:
        return False
    for i in range(2, int(math.sqrt(numero))+1):
        if numero % i == 0:
            return False
        return True

def verificar_priom_o_compuesto():
   numero= int(input("Ingrese un numero: "))
   if es_primo(numero):
      print(numero, "es primo")
   else:
       print(numero, "es compuesto")

def primeros_n_primos():
   n=int(input("Cuantos primos: "))
   contador=0
   numero=2
   while contador < n:
      if es_primo(numero):
         print(numero)
         contador+=1
      numero += 1
      