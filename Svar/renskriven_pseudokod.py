while True:

    try:
        ålder = int(input("Ange din ålder: "))

    except ValueError:
        print("Fel! Ange din ålder som ett heltal.")
        continue
    
    if ålder >= 18:
        print("Du är vuxen.")
        break

    elif 13 <= ålder <= 17:
        print("Du är tonåring.")
        break

    elif ålder < 13:
        print("Du är barn.")
        break