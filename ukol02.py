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
