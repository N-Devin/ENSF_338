import matplotlib.pyplot as plt

f = open("q3.txt", "r")
text = f.read()
theDict ={chr(y):((text.count((chr(y)).lower()))+(text.count((chr(y)).upper()))) for y in range(65,91)}
print(theDict)
freqDict = {chr(y):((text.count((chr(y)).lower()))+(text.count((chr(y)).upper())))/(sum(theDict.values())) for y in range(65,91)}
print(freqDict)
plt.bar(freqDict.keys(), freqDict.values(), color='g')
plt.show()
