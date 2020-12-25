word = input("введите строку из нескольких слов, разделённых пробелами (слова меньше 10 букв): ")
word = word.split()
num = 1
for i in word:
    print(f"{num} - {i[:10]}")
    num += 1
