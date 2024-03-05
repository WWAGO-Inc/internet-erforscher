def addieren(x, y):
    return x + y

def subtrahieren(x, y):
    return x - y

def multiplizieren(x, y):
    return x * y

def dividieren(x, y):
    if y == 0:
        return "Fehler: Division durch Null!"
    else:
        return x / y

print("Wähle eine Operation:")
print("1. Addition")
print("2. Subtraktion")
print("3. Multiplikation")
print("4. Division")

while True:
    wahl = input("Gib deine Auswahl (1/2/3/4) ein: ")

    if wahl in ('1', '2', '3', '4'):
        num1 = float(input("Gib die erste Zahl ein: "))
        num2 = float(input("Gib die zweite Zahl ein: "))

        if wahl == '1':
            print("Ergebnis:", addieren(num1, num2))
        elif wahl == '2':
            print("Ergebnis:", subtrahieren(num1, num2))
        elif wahl == '3':
            print("Ergebnis:", multiplizieren(num1, num2))
        elif wahl == '4':
            print("Ergebnis:", dividieren(num1, num2))
        
        weitere_berechnung = input("Möchtest du eine weitere Berechnung durchführen? (ja/nein): ")
        if weitere_berechnung.lower() != 'ja':
            break
    else:
        print("Ungültige Eingabe")
