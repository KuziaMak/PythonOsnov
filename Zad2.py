import re

with open("Text2.txt", "r", encoding="utf-8-sig") as f:
    stroki = f.readlines()
    i = 0
    f.seek(0)
    slove = len(re.split(r"[ \n]+", f.read()))  # я потался, но не смог довести до идеала
    print(f"строк: {len(stroki)} слов: {slove}")
print("Файл закрыт")
