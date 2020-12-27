int_func = lambda \
    text: text.capitalize()  # Не совсем понял задание. Зачем нужна функцию если можно использовать text.title()
text = input("Введите текст через пробел: ")
text = list(map(int_func,text.split()))
print(" ".join(text))
