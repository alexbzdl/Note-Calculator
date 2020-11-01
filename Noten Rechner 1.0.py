#Anzahl Fächer
anzahlF = -1
while anzahlF<0 or anzahlF>10:
    try:
        print("Wie viele Fächer: ")
        anzahlF = int(input())
    except:
        continue

#Auswahl der Fächer
for j in range(0,anzahlF+0):
    Fl = ["Fach"]
    summe = 0
    
    print("Noten Rechner")
    print()
 
    print("Fach auswählen")
    Fl[0] = input()
    print(Fl, "Noten")
    
    #Anzahl der Noten
    anzahln = -1
    while anzahln<0 or anzahln>10:
        try:
           print("Wie viele Noten: ")
           anzahln = int(input())
        except:
           continue
    #Eingabe der Noten 
    for i in range(0,anzahln+0):
        try:
            inp = int(input("Note eintragen: "))
            if inp > 6:              #Note kann nicht höher sein als 6
               print("Bitte nur bis Note 6 eintragen") 
            summe += inp             #Berechnung der Noten
            gsn = summe / anzahln
            rx = round(gsn,1)  
        except:
            print("Keine Zahl eingegeben")
            continue
        
    #Anzeige der gesamt Note des Faches
    try: 
        print("Gesamt Note von", Fl, "ist: ", rx)
    except:
        print("Sie haben keine Noten eingegeben")
        continue
    
#Berechnung der gesamt Note der gesamten Fächer
try:
    summe += gsn
    gsn1 = summe / int(input("Wie viele Fächer haben sie ausgewählt:"))
    rx1 = round(gsn1,1)
    print("Durchnitt der Fächer ist: ", rx1)
except:
    print("Fehler")