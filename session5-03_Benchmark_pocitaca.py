import time
import random
import hashlib


# benchmark pocitaca

abeceda = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
def vzorka():
    vysledok = list()
    for _ in range(0, 1000000):
        retazec = str()  # ""
        for znak in range(0,10):
            retazec += random.choice(abeceda)
        vysledok.append(retazec)
    return vysledok

def hash_it(text):
    h = hashlib.md5()
    data = bytes(text, encoding='utf8')
    h.update(data)  # mixer
    return h.hexdigest()


t1 = time.time()
vygenerovane_retazce = vzorka()
for i in vygenerovane_retazce:
    hash_it(i)
t2 = time.time()
print(t1,'\t\t', t2)
print('VYSLEDNY CAS V SEC: ', t2-t1)


# Andrej 3.68 sec  i5-11400H
# Vlado 4.8 sec   i5 - 8300H
# Veronika 2.72 sec  i7 - ??
# Peter 2.55 sec  M1 Pro
# Eniko 4.04 sec i5

