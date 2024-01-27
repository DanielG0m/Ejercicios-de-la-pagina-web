import os
contj1=0
contj2=0
while True:
    primer_jugador=input("Cual fue su jugada jugador 1: ").lower()
    segundo_jugador=input("Cual fue su jugada jugador 2: ").lower()
    primer_jugador=primer_jugador.replace(' ','')
    segundo_jugador=segundo_jugador.replace(' ','')

    if primer_jugador==segundo_jugador:
        print("empate")
        print(f" {contj1} - {contj2}")
    elif (primer_jugador == "piedra" and segundo_jugador == "tijera") or (primer_jugador == "tijera" and segundo_jugador == "papel") or (primer_jugador == "papel" and segundo_jugador == "piedra"):
        contj1+=1
        print(f" {contj1} - {contj2}")
    else:
        contj2=+1
        print(f" {contj1} - {contj2}")
    
    if contj1==3:
        print(f" {contj1} - {contj2}")
        print("A es el ganador")
        break
    elif contj2==3:
        print(f" {contj1} - {contj2}")
        print("B es el ganador")
        break