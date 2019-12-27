# -*- coding: utf-8 -*-
#!/usr/bin/python3

# import knihoven
import msvcrt
import os
import time


# definice jmena hrace, pozdeji se bude ptat
jmeno = "David"
jmeno2 = "Davide"


# nacteni mapy (mapa a pozice by se mela nacist automaticky z posledni hry)
mapa = "prvni.mapa"
f=open(mapa, "r", encoding="utf-8")
if f.mode == 'r':
    f1=f.readlines()
    for a in f1:
        print(a)
f.close()
time.sleep(2)


# definice os
x = 1 # vodorovna osa
y = 1 # svisla osa


# samotna hra
while True:
    os.system('cls')
    f = open(jmeno,"w+")
    f.write("y = %d\r\n" % y)
    f.write("x = %d\r\n" % x)
    f.close()
    print("\033[44mTextová hra VLÁDCE HULIXONU\033[0m \033[43m(c) 2019 DaMiSi\033[0m")
    print()
    print(jmeno2, ", nacházíš se na", x, y)
    print()
    print("\033[93mMužeš jít na \033[4mS\033[0m\033[93ever, \033[4mV\033[0m\033[93ýchod, \033[4mZ\033[0m\033[93ápad, \033[4mJ\033[0m\033[93ih a můžeš se\033[4mB\033[0m\033[93rat předmět nebo u\033[4mK\033[0m\033[93ončit hru.\033[0m")
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
