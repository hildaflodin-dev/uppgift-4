while True:

   try:
       tal = int(input("Ange ett tal: "))
       print(f"100 / {tal} = {100 / tal:.2f}")
       break

   except ValueError:
       print("Felaktig inmatning. Ange ett heltal.")

   except ZeroDivisionError:
       print("Fel: Division med noll är inte tillåten. Försök igen.")
