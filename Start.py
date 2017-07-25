# -*- coding: utf-8 -*-
"""
@author: Andrasz
"""
class cKunststoff:
    def __init__(self, iheight, oheight, idiameter, odiameter, schluesselweite, kopflaenge, name):
        self.h = iheight
        self.H = oheight
        self.d = idiameter
        self.D = odiameter
        self.SW = schluesselweite
        self.K = kopflaenge
        self.n = name
pmeter = ["Innere Höhe","Äußere Höhe", "Innendurchmesser", "Außendurchmesser", "Schlüsselweite", "Kopflänge", "Name" ]
x = int(input("Pls enter a number: "))
# Start, Input muss eine Nummer sein
# 0 für Hilfe und 1-X für alle Folgenden
if x == 0:
    print ("1 -> Kunststoffprodukte")
    print ("2 -> Metallprodukte")
    print ("3 -> Rost und Kompost")
if x == 1:
    print ("Enter details:")
    x = cKunststoff(20, 10, 30, 50, 44, 12, "Kappe")
    print (x.h)
    print (x.H)
    print (x.d)
    print (x.D)
    print (x.SW)
    print (x.K)
    print (x.n)

else:
    print ("Sorry wrong number. Try 0 for help")
    
