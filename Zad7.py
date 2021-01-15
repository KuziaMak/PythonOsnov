with open("Test7.txt", "r", encoding="utf-8-sig") as f:
    firm = f.readlines()
    massa = []
    aree = {}
    for i in firm:
        i = i.split()
        aree[f"{i[0]}"] = float(i[2]) - float(i[3])
    alle = [j for j in aree.values() if j >= 0]
    sred = {"average_profit": (sum(alle) / len(firm))}
    print(aree, sred)
print("Файл закрыт")
import json
data = [aree,sred]
with open("data.json", "w") as f:
    json.dump(data,f)
print("json-объекта закрыт")






