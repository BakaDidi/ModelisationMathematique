from numpy import loadtxt
import random




names = []

with open("eggs.csv", 'rb') as file:
    probas = loadtxt(file, delimiter=';')

for i in range(len(probas)):

    names.append(chr(65+i))

# nbLances = int(input("Nombre de lancers: "))
# nbDeplacements = int(input("Nombre de déplacements autorisés: "))

nbLances = 10
nbDeplacements=2



for i in range(nbLances):

    pos = 0 # position = A

    for j in range(nbDeplacements):

        randomNb = random.random()
        k = 0
        unDone = True

        infBorne = 0 # valeur
        supBorne = 0 # index

        resultIndex = None

        while unDone:
            if infBorne < randomNb and randomNb < probas[pos][supBorne]:
                resultIndex = supBorne
                unDone = False
            else:
                infBorne += probas[pos][supBorne]
                supBorne += 1


        print(resultIndex)










