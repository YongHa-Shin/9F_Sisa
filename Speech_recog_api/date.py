import json
import datetime

with open('26_1_20230801_165059.json', 'r', encoding='utf-8') as f:

    json_data = json.load(f)

# print(json.dumps(json_data, indent="\t", ensure_ascii=False) )

f = open("새파일.txt", 'w')

for i in json_data["segments"] :
    # print(type(i["start"]))
    i["start"] /= 1000
    i["start"] = int(i["start"])
    i["start"] = str(datetime.timedelta(seconds=i["start"]))
    print(i["start"])
    print(i["text"] + "\n")

    f.write(i["start"])
    f.write("\n")
    f.write(i["text"])
    f.write("\n\n")

f.close()