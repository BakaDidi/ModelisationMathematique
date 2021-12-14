from numpy import loadtxt
import numpy as np
import random
import pandas
import matplotlib.pyplot as plt
import numpy as np

names = []

filename = input("Filename:")

with open(filename, 'rb') as file:
    probas = loadtxt(file, delimiter=';')

for i in range(len(probas)):

    names.append(chr(65+i))

depart = int(input("Position départ (entier): "))
nbDeplacements = int(input("Nombre de déplacements autorisés (temps): "))


totalAffichage = []
matricePos = []
pos = depart
for i in range(len(probas)):
    totalAffichage.append([])
    matricePos.append(0.0)
matricePos[depart] = 1.0
matricePos = np.array(matricePos)
probaMatrice = np.array(probas)
for i in range(nbDeplacements):



    for i in range(len(probas)):
        totalAffichage[i].append(matricePos[i])
    matricePos = matricePos @ probaMatrice


i = 0
for line in totalAffichage:
    plt.plot(line, label=chr(65+i))
    plt.legend()
    i+=1
plt.show()


