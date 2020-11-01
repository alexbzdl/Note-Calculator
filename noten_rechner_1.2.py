text_logo = """  
    +=========================+
    |      Noten Rechner      |  
    +=========================+
    | Version 1.2             |
    | Aleksej Bezdels         | 
    +=========================+  """
  
print(text_logo)
print()

anzahl_faecher = ""
faecher = []
noten = []

while(True):    
    gewaehltes_fach = input("Fach auswählen: ")
    faecher.append(gewaehltes_fach)

    anzahl_noten = ""
    while not isinstance(anzahl_noten, int):
        try:
            print("Wie viele Noten: ")
            anzahl_noten = int(input())
        except:
            print("Das ist keine Zahl")
            continue
        
    summe_noten = 0        
    print("Bitte gib deine Noten ein: ")
    for j in range(0,anzahl_noten):
        noten_input = ""
        while not isinstance(noten_input, int): 
            try:
                noten_input = input("Note eintragen:")
                
                #abfrage ob input eine Zahl ist                   
                if not noten_input.isdigit():
                    raise Exception("bitte gib eine Zahl ein")
                else:
                    noten_input = int(noten_input)
                    
                #abgrage ob input zwischen 1 und 6 ist 
                if noten_input >= 1 and noten_input <=6:
                    summe_noten += noten_input
                else:
                    raise Exception("Bitte gib eine Zahl zwischen 1 bis 6") #Wirft ein Fehler
            except Exception as e:
                print(e)
                noten_input = ""
                continue
    print("Das ist die Summe der Noten: " + str(summe_noten))
    noten_durchschnitt = summe_noten / anzahl_noten
    print("Das ist der Durchschnitt: " + str(noten_durchschnitt) )
    noten_durchschnitt_rund = round(noten_durchschnitt, 1)
    noten.append(noten_durchschnitt_rund)
    print("Das ist der Durchschnitt in " + str(gewaehltes_fach) + " gerundet: " + str(noten_durchschnitt_rund))        

    inp1 = input("Möchtest du weitere Fächer ausrechnen [j][n]:")
    if inp1 == "j":
        print()
        continue
        
    if inp1 == "n":
        break

gesamt_summe_noten = 0
for note in noten:
    gesamt_summe_noten += note
    
gesamt_durchschnitt = gesamt_summe_noten / len(noten)
gesamt_durchschnitt_rund = round(gesamt_durchschnitt, 1)
print("Der gesamtdurchschnitt aller Noten ist: " + str(gesamt_durchschnitt_rund))
