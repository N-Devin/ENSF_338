
import json
  
with open("data.json", "r") as inF:
  
    content = json.load(inF)

data = content[::-1]  

with open("samplefile.txt", "w") as fifi:
    json.dump(data, fifi)


