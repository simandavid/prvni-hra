# -*- coding: utf-8 -*-
#!/usr/bin/python3


# import knihoven
import msvcrt
import os
import time
from array import *





# definice funkci
def hlavicka_hry():
    os.system('cls')
    print("\033[44mTextová hra VLÁDCE HULIXONU\033[0m \033[43m(c) 2019 DaMiSi\033[0m\r\n\r\n")


def zapis_stavu_do_souboru(x,y,jmeno,jmeno2):
    f = open(jmeno,"w+")
    f.write("jmeno = " + jmeno + "\r\n")
    f.write("jmeno2 = " + jmeno2 + "\r\n")
    f.write("x = " + str(x) + "\r\n")
    f.write("y = " + str(y) + "\r\n")
    f.close()


def co_dal(x,y):
    #neco
    return


def co_mam_u_sebe():
    print("U sebe nemáš právě teď nic. Prázdné kapsy kámo.")
    return


# definice jmena hrace, pozdeji se bude ptat
jmeno = "David"
jmeno2 = "Davide"


# priprava kompletni mapy hry
# inicializace pole MAPY, vytvori se 2D pole o zadane velikosti a vyplni se nulama
mapa = []
radkuasloupcu = 20
for i in range(radkuasloupcu):
    temp = []
    for j in range(radkuasloupcu):
        temp.append(0)
    mapa.append(temp)

# nacteni jednotivych "mistnosti" do mapy, tam kde neni v mape zadna mistnost, tam zustane 0
nazevmapy = "prvni.mapa"
try:
    f=open(nazevmapy, "r", encoding="utf-8")
    if f.mode == 'r':
        f1=f.readlines()
        for a in f1:
            if a[0] != "#":
                abc = (a.split(";"))
                #print(abc)
                mapa[int(abc[0])][int(abc[1])]=abc[2]
    f.close()
    #time.sleep(5)
except:
    print("Problém s vytvářením mapy ....")
    exit()

# definice os
x = 1 # vodorovna osa
y = 1 # svisla osa


# samotna hra
while True:

    zapis_stavu_do_souboru(x,y,jmeno,jmeno2)
    hlavicka_hry()
    print()
    print(jmeno2,",")
    print(mapa[x][y])
    print()
    co_mam_u_sebe()
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
