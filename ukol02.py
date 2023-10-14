sklad = {
  "1N4148": 250,
  "BAV21": 54,
  "KC147": 147,
  "2N7002": 97,
  "BC547C": 10
}


produkt = input("Zadej kod soucastky: ")
if produkt in sklad: 
    print(f"{produkt} je na skladě.")   
else: 
    print(f"Bohužel, součástka {produkt} není na skladě.")

pocet = int(input("Zadej počet kusů: "))
if pocet <= sklad[produkt]:
    print(f"{produkt} je v požadovaném množství na skladě a zbyde {sklad[produkt]-pocet} ks.")
if pocet > sklad[produkt]:
    print(f"{produkt} je dostupný v omezeném množství {sklad[produkt]-pocet} ks.")
    if pocet > sklad[produkt]:
        sklad = sklad.pop(produkt)
    print(sklad)

'''
Komentar (M. Jurosz)
zacatek dobry, ale program spatne resi pokud soucastka neni na sklade, protoze vleze tak ci tak do otazky pocet, coz je pro uzivatele nesmysl.
Tedy mel by jsi cyklus zanorit do sebe, aby v pripade ze neexistuje mnozstvi program skoncil.
produkt = input("Zadej kod soucastky: ")
if produkt in sklad: 
    print(f"{produkt} je na skladě.")  
    pocet = int(input("Zadej počet kusů: "))
    if pocet <= sklad[produkt]:
        print(f"{produkt} je v požadovaném množství na skladě a zbyde {sklad[produkt]-pocet} ks.")
    if pocet > sklad[produkt]:
        print(f"{produkt} je dostupný v omezeném množství {sklad[produkt]-pocet} ks.")
        if pocet > sklad[produkt]:
            sklad = sklad.pop(produkt)
        print(sklad)
else: 
    print(f"Bohužel, součástka {produkt} není na skladě.")

Dale je jeste nesikovne napsana veta na radku 20
Protoze ve chvili kdy vezme vice mnozstvi nez je na sklade tak program vrati vetu:
"je dostupný v omezeném množství -1 ks." tedy spis bych cekal informaci ze dostane o tolik mene kusu
nebo napriklad ze dostane jen 54 kusu misto pozadovanych 55 atd.

Beru jako drobne chyby, jen v budoucich ukolech na to davat pozor.
Diky
'''
