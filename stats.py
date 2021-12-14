from numpy import loadtxt
import numpy as np
import random
import pandas
import matplotlib.pyplot as plt

names = []

filename = input("Filename:")

with open(filename, 'rb') as file:
    probas = loadtxt(file, delimiter=';')

for i in range(len(probas)):

    names.append(chr(65+i))

nbLances = int(input("Nombre de lancers: "))
nbDeplacements = int(input("Nombre de déplacements autorisés: "))

# nbLances = 10
# nbDeplacements=5

total = []


for i in range(nbLances):

    pos = 0 # position = A
    posHistory = ["A"]
    for j in range(nbDeplacements):

        randomNb = random.random()
        k = 0
        unDone = True

        infBorne = 0 # valeur
        supBorneIndex = 0
        supBorne = probas[pos][supBorneIndex]

        resultIndex = None

        while unDone:
            if infBorne < randomNb and randomNb < supBorne:
                resultIndex = supBorneIndex
                unDone = False
            else:
                infBorne += probas[pos][supBorneIndex]
                supBorneIndex += 1
                supBorne += probas[pos][supBorneIndex]


        pos = resultIndex
        posHistory.append(names[pos])

    total.append(posHistory)


totalFreqs = []


totalProba = pandas.DataFrame.from_records(data=total)
# print(total)

for column in totalProba.iteritems():
    freqs = []
    for name in names:
        freqs.append(column[1].values.tolist().count(name) / nbLances)
    totalFreqs.append(freqs)

print("\n[ A,   B,   C ]")

totalFreqs = pandas.DataFrame.from_records(columns=names, data=totalFreqs)

freqsAffichage = []

for freq in totalFreqs.iteritems():
    freqsAffichage.append(freq[1].values.tolist())




freqsAffichage = np.asarray(freqsAffichage)
i = 0
for line in freqsAffichage:
    plt.plot(line, label=chr(65+i))
    plt.legend()
    i+=1
plt.show()





















