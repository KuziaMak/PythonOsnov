verucka = int(input("Введите выручку фирмы: "))
isder = int(input("Введите издержки: "))
if verucka > isder:
    print("Ура прибыль")
    pribli = verucka - isder  # Ненавижу экономику
    rentab = pribli / verucka
    print("рентабельность фирмы состовляет {}".format(rentab))
    people = int(input("Сколько людей в фирме: "))
    print("Прибыль состовляет на одного человека ", pribli / people)
elif verucka < isder:
    print("фирма в пралёте")
else:
    print("я даже не знаю что и сказать")
