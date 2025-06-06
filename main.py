import random

print("Willkommen beim Zahlenratespiel!")
geheime_zahl = random.randint(1, 10)
versuch = 0

while True:
    eingabe = input("Rate eine Zahl zwischen 1 und 10: ")
    versuch += 1

    if not eingabe.isdigit():
        print("Bitte gib eine Zahl ein!")
        continue

    tipp = int(eingabe)

    if tipp < geheime_zahl:
        print("Zu klein!")
    elif tipp > geheime_zahl:
        print("Zu groß!")
    else:
        print(f"Richtig! Du hast {versuch} Versuch(e) gebraucht.")
        break
