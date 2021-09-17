import json
with open("C:\\Users\\admin\\Desktop\\1.txt", "r", encoding="utf-8") as f:
    a = f.read()
b = json.loads(a)
c = b["hits"]["hits"]
for i in c:
    print(i["_source"]["code"])