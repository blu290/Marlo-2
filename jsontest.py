import json

data = json.load(open("config.json"))
for i in data["sounds"]:
    print(i["value"])
    print(i["type"])
