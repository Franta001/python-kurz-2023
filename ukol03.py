import json

with open('body.json', mode='r', encoding='utf-8') as file:
    body = json.load(file)

print(body)

pocet_fail = 0              #zkusil jsem spočítat i počet Fail/Pass
pocet_pass = 0
                            # vytvoření  slovníku hodnocení
prospech_data = {}

                            # procházení žáků, hodnocení
for jmeno, body in body.items():
    if body >= 60:
        prospech_data[jmeno] = "Pass"
        pocet_pass += 1     #pro součet
    else:
        prospech_data[jmeno] = "Fail"
        pocet_fail += 1     #pro součet

                            # uložení nového slovníku 'prospech.json', měl jsem problém s diakritikou, proto doplněno ensure_ascii
with open('prospech.json', mode='w', encoding='utf-8') as file:
    json.dump(prospech_data, file,ensure_ascii=False, indent=4)

print("Hodnocení je uloženo v souboru 'prospech.json'.")

print("Počet písemek:",len(prospech_data))   #počet písemek
print("Počet Fail:", pocet_fail)
print("Počet Pass:", pocet_pass)


