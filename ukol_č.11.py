import re

def valid_username(username):  # Uživatelské jméno
    pattern = re.compile(r'^[a-zA-Z]{6,10}$')
    return bool(pattern.match(username))

def valid_password(password):   # Heslo
    pattern = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[_\-.+=])[a-zA-Z\d_\-.+=]{12,30}$')
    return bool(pattern.match(password))

def valid_email(email):   # E-mailová adresa
    pattern = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')
    return bool(pattern.match(email))

username = input("Zadej uživatelské jméno: ")
email = input("Zadej e-mailovou adresu: ")
password = input("Zadej heslo: ")

if valid_username(username):
    print("Uživatelské jméno je platné.")
else:
    print("Uživatelské jméno není platné.")

if valid_email(email):
    print("E-mailová adresa je platná.")
else:
    print("E-mailová adresa není platná.")

if valid_password(password):
    print("Heslo je platné. :-)")
else:
    print("Heslo není platné. :-(")