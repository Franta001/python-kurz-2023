morse_code = {
    "0": "-----",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    "a": ".-",
    "b": "-...",
    "c": "-.-.",
    "d": "-..",
    "e": ".",
    "f": "..-.",
    "g": "--.",
    "h": "....",
    "i": "..",
    "j": ".---",
    "k": "-.-",
    "l": ".-..",
    "m": "--",
    "n": "-.",
    "o": "---",
    "p": ".--.",
    "q": "--.-",
    "r": ".-.",
    "s": "...",
    "t": "-",
    "u": "..-",
    "v": "...-",
    "w": ".--",
    "x": "-..-",
    "y": "-.--",
    "z": "--..",
    ".": ".-.-.-",
    ",": "--..--",
    "?": "..--..",
    "!": "-.-.--",
    "-": "-....-",
    "/": "-..-.",
    "@": ".--.-.",
    "(": "-.--.",
    ")": "-.--.-",
}
#vypsání různých hodnot
#for znak in morse_code:
    #print(morse_code[znak])
    #print(f"znak: {znak}, hodnota: {morse_code[znak]}")   #vypsání hodnoty a znaku do sloupce
    #print(morse_code[znak],end=" ")                        #vypsání hodnot do řádku
    #print(znak, end=" ")                                    #vypsání znaku do řádku
#print(morse_code)                                           #vypsání celé morseovky


# překlad znaku do morseovky s doplněním znaku "mezera"
morse_code[" "] ="/"
znak = input("Zadej znak: ")
if znak in morse_code:
    print(morse_code[znak])

'''
komentar (M. Jurosz)
Zadani mas splnene castecne, protoze se chtelo, aby uzivatel nezadal jeden znak ale celou vetu napriklad.
Tedy melo by byt rozsireno o vnejsi cyklus, ktery slovo rozdeli na znaky a projde a pritom uklada jednotlive morseovy znaky a na konci vypise.
Napr.
text = input("Zadejte text: ")

for pismeno in text:
    if pismeno == " ":
        print("/")
    else:
        print(morse_code[pismeno], end=" ")

'''
