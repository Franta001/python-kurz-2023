
def overit_cislo(tel_cislo):
    """
    Funkce na overení délky tel. cisla i v mzn. formatu
    """
    # číslo převedu na řetězec a odstraním mezery
    tel_cislo = tel_cislo.replace(" ", "")
    if len(tel_cislo) == 9 or (len(tel_cislo) == 13 and tel_cislo[:4] == "+420"): # kontrola počtu znaků v čísle
        return True
    else:
        return False

JEDNOTKOVA_CENA_SMS = 3
def vypocet_ceny_sms(sms):
    """
    Funkce na výpočet ceny sms; musím spočítat počet znaků zprávy a vydělit 160 (zaokrouhleno nahoru). SMS má 160 znaků (nikoli 180).
    """
    delka_sms = len(sms)
    cena = (delka_sms + 159) // 160 * JEDNOTKOVA_CENA_SMS   #využil jsem globální proměnnou pro jednotkovou cenu sms
    return cena

tel_cislo = input("Zadejte telefonní číslo: ")
if overit_cislo(tel_cislo):
    print("Platné telefonní číslo.")
    sms = input("Zadejte text sms: ")
    cena_sms = vypocet_ceny_sms(sms)
    delka_sms = (len(sms) + 159)//160  # u delších zpráv chci zjistit, do kolika sms bude rozděleno - použita tato proměnná 
    if cena_sms > JEDNOTKOVA_CENA_SMS:
        print(f"Cena celé zprávy je {cena_sms} Kč a je rozdělena do {delka_sms} sms.") #pokud je zpráva delší než 160 znaků, - rozdělena do více sms. Proto jsem zjistil počet sms.
    else:
        print(f"Cena sms je {cena_sms} Kč.")
else:
    print("Neplatné telefonní číslo.")