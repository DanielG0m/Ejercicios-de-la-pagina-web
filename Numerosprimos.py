import math

def es_primo(numero):
    if numero <=1:
        return False
    for i in range(2, int(math.sqrt(numero))+1):
        if numero % i == 0:
            return False
        return True

def verificar_primo_o_compuesto():
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

def primos_menores_que_m():
   m=int(input("Primos menores que: "))
   for i in range(2,m):
      if es_primo(i):
         print(i)

def contar_primos_menores_que_m(m):
   contador=0
   for i in range(2,m):
      if es_primo(i):
         contador+=1
   return contador

def factores_primos():
   numero= int(input("Ingrese numero: "))
   for i in range (2,numero + 10):
      while numero % i == 0:
         print(i)
         numero //=i

def suma_de_dos_primos():
   num_par=int(input("Ingrese un numero par: "))
   for i in range(2, num_par // 2+1):
      if es_primo(i) and es_primo(num_par - i):
         print(i, "+", (num_par - i))


def contar_primos_terminan_en_7(limite):
   contador=0
   for i in range(2,limite):
      if es_primo(i) and i % 10 == 7:
         contador +=1
   return contador

def suma_cuadrados_primos_entre_1_y_1000():
   suma = 0
   for i in range(2,1001):
      if es_primo(i):
         suma+=i*i
   return suma

def producto_primos_con_digito_7_menores_que_100():
    producto = 1
    for i in range(2, 100):
        if es_primo(i) and '7' in str(i):
            producto *= i
    return producto

verificar_primo_o_compuesto()
primeros_n_primos()
primos_menores_que_m()
m = int(input("Contar primos menores que: "))
cantidad_primos = contar_primos_menores_que_m(m)
print("Hay", cantidad_primos, "primos menores que", m)
factores_primos()
suma_de_dos_primos()
print("Cantidad de primos menores que diez mil y terminan en 7:", contar_primos_terminan_en_7(10000))
print("Suma de los cuadrados de los números primos entre 1 y 1000:", suma_cuadrados_primos_entre_1_y_1000())
print("Producto de los primos menores que 100 con dígito 7:", producto_primos_con_digito_7_menores_que_100())