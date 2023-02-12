import json
import matplotlib.pyplot as plt

with open("songdata.json", "r") as inF:
    content = json.load(inF)
below = []
above = []
for i in range(len(content)):
    if content[i]["danceability"] > .5:
        above.append(content[i]["energy"])
    if content[i]["danceability"] < .5:
        below.append(content[i]["energy"])

plt.hist(above, color='r', alpha=.5, label="Below .5")
plt.show()