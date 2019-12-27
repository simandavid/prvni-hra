#!/usr/bin/python3

# import knihoven
import msvcrt
import os
import time


# definice jmena hrace
jmeno = "David"
jmeno2 = "Davide"






# nacteni mapy
mapa = "prvni.mapa"
f=open(mapa, "r")
if f.mode == 'r':
    f1=f.readlines()
    for a in f1:
        print(a)
f.close()
time.sleep(5)


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
    print(jmeno2, ", nacházíš se na", x, y)
    print("Mužeš jít na \033[4mS\033[0mever, \033[4mV\033[0mýchod, \033[4mZ\033[0mápad, \033[4mJ\033[0mih a můžeš se\033[4mB\033[0mrat předmět nebo u\033[4mK\033[0mončit hru.")
    print("Co teď udelas?")

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
