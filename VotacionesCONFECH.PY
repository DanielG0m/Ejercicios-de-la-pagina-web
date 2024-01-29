import os

while True:
    aceptan=0
    rechazan=0
    empate=0
    voto=str().upper()
    uni=int(input("Numero de universidades: "))
    for i in range(uni):
        A=0
        R=0
        N=0
        B=0
        aceptan=0
        rechazan=0
        empate=0
        universidad=input("Universidad: ").upper()
        while True:
            voto=input("Voto: ").upper()
            if voto == "X":
                print(f"{universidad}: {A} aceptan, {R} rechazan, {B} blancos, {N} nulos. ")
                print("")
                break

            if voto == "A":
                A +=1
            elif voto == "R":
                R+=1
            elif voto == "N":
                N+=1
            elif voto == "B":
                B+=1

    if A > R:
        aceptan+=1
    elif R > A:
        rechazan+=1
    else:
        empate+=1


    print("Universidades que aceptan: ",aceptan)
    print("Universidades que rechazan: ",rechazan)
    print("Universidades con empate: ",empate)
    break