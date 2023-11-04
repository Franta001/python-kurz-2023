class Auto:
    def __init__(self, registracni_znacka, typ_vozidla, najete_km):
        self.registracni_znacka = registracni_znacka
        self.typ_vozidla = typ_vozidla
        self.najete_km = najete_km
        self.dostupne = True

    def pujc_auto(self):
        if self.dostupne:
            self.dostupne = False
            return "Potvrzuji zapůjčení vozidla"
        else:
            return "Vozidlo není k dispozici"

    def get_info(self):
        return f"Registrační značka: {self.registracni_znacka}, Typ vozidla: {self.typ_vozidla}"


def pujceni_automobilu(auto):
    if auto.dostupne:
        print(auto.get_info()) 
        potvrzeni = auto.pujc_auto()
        print(potvrzeni)
    else:
        print("Automobil není k dispozici.")


# Auta
auto_1 = Auto("4A2 3020", "Peugeot 403 Cabrio", 47534)
auto_2 = Auto("1P3 4747", "Škoda Octavia", 41253)


# Dotaz, které auto si uživatel přeje půjčit
volba = input("Zadej značku automobilu (Peugeot nebo Škoda): ")

if volba == "Peugeot":
    pujceni_automobilu(auto_1)
elif volba == "Škoda":
    pujceni_automobilu(auto_2)
else:
    print("Neplatná volba. Zvolte Peugeot nebo Škoda.")