usernumb = int(input("Введите секунды: "))
ss = usernumb % 60
mm = (usernumb // 60) % 60
hh = (usernumb // 60) // 60
print(f"Время {hh}:{mm}:{ss}")
