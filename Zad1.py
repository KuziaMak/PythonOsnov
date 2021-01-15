with open("Text1.txt","w",encoding="utf-8") as f:
    while True:
        usertext= input("Введите текст или пустую строку для выхода ")
        if not usertext:
            break
        f.write(f"{usertext}\n")
print("Файл закрыт")