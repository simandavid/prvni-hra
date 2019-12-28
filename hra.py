# -*- coding: utf-8 -*-
#!/usr/bin/python3

# import knihoven
import msvcrt
import os
import time
from array import *

mapa = []

for i in range(20):
    temp = []
    for j in range(20):
        temp.append(0)
    mapa.append(temp)


# definice jmena hrace, pozdeji se bude ptat
jmeno = "David"
jmeno2 = "Davide"


# nacteni mapy (mapa a pozice by se mela nacist automaticky z posledni hry)
nazevmapy = "prvni.mapa"
f=open(nazevmapy, "r", encoding="utf-8")
if f.mode == 'r':
    f1=f.readlines()
    for a in f1:
        if a[0] != "#":
            abc = (a.split(";"))
            print(abc)
            mapa[int(abc[0])][int(abc[1])]=abc[2]
f.close()
time.sleep(5)


# definice os
x = 1 # vodorovna osa
y = 1 # svisla osa


# samotna hra
while True:
    os.system('cls')
    f = open(jmeno,"w+")
    f.write("x = %d\r\n" % x)
    f.write("y = %d\r\n" % y)
    f.close()
    print("\033[44mTextová hra VLÁDCE HULIXONU\033[0m \033[43m(c) 2019 DaMiSi\033[0m")
    print()
    print(jmeno2,",")
    print(mapa[x][y])
    print()
    print("Mužeš jít na Sever, Východ, Západ, Jih a můžeš seBrat předmět nebo uKončit hru.")
    print()
    print("Co teď uděláš? \033[90m(stiskni příslušnou klávesu)\033[0m")

    input_char = msvcrt.getch().decode("utf-8")

    if input_char.upper() == 'S':
        y = y - 1
        if y < 1:
            y = 1

    if input_char.upper() == 'J':
        y = y + 1

    if input_char.upper() == 'Z':
        x = x - 1
        if x < 1:
            x = 1

    if input_char.upper() == 'V':
        x = x + 1

    if input_char.upper() == 'B':
        x = x

    if input_char.upper() == 'K':
        print("Konec hry ...")
        exit()
