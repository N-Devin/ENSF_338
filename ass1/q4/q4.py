import json
with open("buildings.json", "r") as inF:
    content = json.load(inF)
count = 0 
summ = 0
for i in range(len(content)):
    if content[i]["height"] > 5:
        count += 1
        summ += content[i]["height"]
average = summ / count
print("The average height of these buildings is", round(average, 2), "meters.")



