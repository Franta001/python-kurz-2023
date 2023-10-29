#úkol č. 5

teploty = [
    [2.1, 5.2, 6.1, -0.1],
    [2.2, 4.8, 5.6, -1.0],
    [3.3, 6.5, 5.9, 1.2],
    [2.9, 5.6, 6.0, 0.0],
    [2.0, 4.6, 5.5, -1.2],
    [1.0, 3.2, 2.1, -2.0],
    [0.4, 2.7, 1.3, -2.8]
]
prumer = [sum(den)/len(den) for den in teploty] 
print(prumer)

ranni_teplota = [den[0] for den in teploty] 
print(ranni_teplota)

nocni_teplota = [den[3] for den in teploty] 
print(nocni_teplota)

p_n_teplota = [[den[1], den[3]] for den in teploty]
print(p_n_teplota)



teploty2 = [
    ["pondělí", 2.1, 5.2, 6.1, -0.1],
    ["úterý", 2.2, 4.8, 5.6, -1.0],
    ["středa", 3.3, 6.5, 5.9, 1.2],
    ["čtvrtek", 2.9, 5.6, 6.0, 0.0],
    ["pátek", 2.0, 4.6, 5.5, -1.2],
    ["sobota", 1.0, 3.2, 2.1, -2.0],
    ["neděle", 0.4, 2.7, 1.3, -2.8]
]
prumerna_teplota = {den: sum(teploty_za_den[1:]) / (len(teploty_za_den) - 1) for den, *teploty_za_den in teploty2}  #* na začátku umožňuje, aby se do ní přiřadily všechny zbývající prvky v každém zanořeném seznamu. Mohu tak pracovat s proměnným počtem prvků v každém zanořeném seznamu.

print(prumerna_teplota)