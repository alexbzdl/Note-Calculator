T = """  

             ,----------------,              ,---------,
        ,-----------------------,          ,"        ,"|
      ,"                      ,"|        ,"        ,"  |
     +-----------------------+  |      ,"        ,"    |
     |  .-----------------.  |  |     +---------+      |
     |  |                 |  |  |     | -==----'|      |
     |  |  Noten Rechner  |  |  |     |         |      |
     |  |                 |  |  |/----|`---=    |      |
     |  |  C:\>_          |  |  |   ,/|==== ooo |      ;
     |  |                 |  |  |  // |(((( [33]|    ,"
     |  `-----------------'  |," .;'| |((((     |  ,"
     +-----------------------+  ;;  | |         |,"     
        /_)______________(_/  //'   | +---------+
   ___________________________/___  `,
  /  oooooooooooooooo  .o.  oooo /,   \,"-----------
 / ==ooooooooooooooo==.o.  ooo= //   ,`\--{)B     ,"
/_==__==========__==_ooo__ooo=_/'   /___________,"
`-----------------------------' """
  
print(T)
print() 

anzahlF = -1
while anzahlF<0 or anzahlF>10:
    try:
        print("Wie viel Fächer: ")
        anzahlF = int(input())
    except:
        continue
    
for i in range(0,anzahlF+0):
    Fl = []
    summe = 0
    
    try:
        print("Fach auswählen")
        Fl.append(input())
        print(Fl, "Noten")
    except:
        print("Kein Fach eingegeben")    
        continue
    
    anzahln = -1
    while anzahln<0 or anzahln>10:
        try:
            print("Wie viele Noten: ")
            anzahln = int(input())
        except:
            continue
        
    for j in range(0,anzahln+0):
        try:
            inp = int(input("Note eintragen: "))
            if inp > 6:
                print("Bitte nur bis Note 6 eintragen")
            summe += inp
            gsn = summe / anzahln
            rg = round(gsn,1)
        except:
            print("Keine Zahl eingegeben")
            continue
    
    try:
        print("Gesamt Note von", Fl, "ist", rg)
    except:
        print("Sie haben keine Note eingegeben")
        continue               
    
try:
    summe += gsn
    gsn1 = summe / anzahlF
    rg1 = round(gsn1,1)
    print("Durchnitt der Fächer ist: ", rg1)
except:
    print("Fehler")
    