#Berechnung der Deutsch Noten 
summez = 0
for i in range(0,6):
    print("Deutsch Noten")
    try:
        inp = int(input("Note eintragen: "))
        summez = summez + inp
        gsn = summez / 6
        rx = round(gsn,1)
    except:
        print("Sie haben keine Zahl eingegeben")    
        continue
print("Gesamt Note von Deutsch ist: ", rx)

#Berechnung der Mathematik Noten
summez1 = 0
for j in range(1,7):
    print("Mathematik Noten")
    try:
        inp1 = int(input("Note eintragen: "))
        summez1 = summez1 + inp1
        gsn1 = summez1 / 6
        rx = round(gsn1,1)
    except:
        print("Sie haben Keine Zahl eingegeben")
        continue
print("Gesamt Note von Mathematik ist: ", rx)

#Berechnung der Englisch Noten
summez2 = 0
for k in range(1,7):
    print("Englisch Noten")
    try:
        inp2 = int(input("Note eintragen: "))
        summez2 = summez2 + inp2
        gsn2 = summez2 / 6
        rx = round(gsn2,1)
    except:
        print("Sie haben keine Zahl eingegebn")
        continue
print("Gesamt Note von Englisch ist: ", rx)

#Berechnung der Noten der Hauptfächer
gsnh = gsn + gsn1+ gsn2
a = gsnh / 3 
rxx = round(a,1)
print("Die Gesamt Note der Hauptfächer:",rxx)

ed = 2.3
if rxx == ed:
    print("Erweiterten Abschluss Geschaft")
elif rxx <= ed+0.4:
    print("Erwiterten fast Geschaft")
else:
    print("Erweiterten nicht geschaft")
     