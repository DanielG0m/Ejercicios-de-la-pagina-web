import os
contj1=0
contj2=0
while True:
    primer_jugador=input("Cual fue su jugada jugador 1: ").lower()
    segundo_jugador=input("Cual fue su jugada jugador 2: ").lower()

    if primer_jugador == "tijera" and segundo_jugador == "papel":
        contj1+=1
        print(f"A: {contj1}  B: {contj2}")
    
    if primer_jugador=="tijera" and segundo_jugador=="piedra":
        contj2+=1
        print(f"A: {contj1}  B: {contj2}")
  

    if primer_jugador == "tijera" and segundo_jugador== "tijera":
        print(f"A: {contj1}  B: {contj2}")

    if primer_jugador == "papel" and segundo_jugador == "tijeras":
        contj1+=1
        print(f"A: {contj1}  B: {contj2}")
    
    if primer_jugador=="papel" and segundo_jugador=="piedra":
        contj2+=1
        print(f"A: {contj1}  B: {contj2}")   

    if primer_jugador == "papel" and segundo_jugador== "papel":
        print(f"A: {contj1}  B: {contj2}")

    if primer_jugador == "piedra" and segundo_jugador == "papel":
        contj1+=1
        print(f"A: {contj1}  B: {contj2}")
    
    if primer_jugador=="piedra" and segundo_jugador=="tijera":
        contj2+=1
        print(f"A: {contj1}  B: {contj2}")   

    if primer_jugador == "piedra" and segundo_jugador== "piedra":
        print(f"A: {contj1}  B: {contj2}")