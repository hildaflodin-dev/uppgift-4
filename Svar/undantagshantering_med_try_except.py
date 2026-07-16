def hämta_tal():
    while True:
        try:
            tal = float(input("Ange ett tal: "))
            return tal
        except ValueError:
            print("Felaktig inmatning. Vänligen ange ett heltal.")

def dividera_med_tal():
    while True:
        tal = hämta_tal()
        try:
            resultat = f"100 / {tal} = {100 / tal:.2f}"
            return resultat
        except ZeroDivisionError:
            print("Fel: Division med noll är inte tillåten. Försök igen.")

print(dividera_med_tal())