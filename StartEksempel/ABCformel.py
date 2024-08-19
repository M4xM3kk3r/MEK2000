"""
Dette skriptet løyser ei andregradslikning.
Koeffisientane i polynomet er hard-koda inn i starten.
"""

# Importere NumPy
import numpy as np

#funksjon
def func(a,b,c):
    #diskriminant

    diskriminant = b**2-4*a*c
    #diskriminant negativ?
    if diskriminant >= 0:
        x_1 = (-b - np.sqrt(b**2-4*a*c)) / (2*a)
        x_2 = (-b + np.sqrt(b**2-4*a*c)) / (2*a)

    # Skriv løysingane til skjerm
        print('x1 =', x_1)
        print('x2 =', x_2)
    else:
        print('Likninga har ingen reelle løysingar')
        
# Gir koeffisientane
while True:
    a = int(input("a="))
    b = int(input("b="))             
    c = int(input("c="))

    print(a,b,c)

    func(a,b,c)



    # Reknar ut løysingane - dersom dei er reelle

