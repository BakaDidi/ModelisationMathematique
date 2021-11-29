import numpy as np
from pylab import *
from numpy import loadtxt


while True:
    try:
        filename = input("Nom du fichier ") + '.csv'
        raw_data = open(filename, 'rb')
        Tp = loadtxt(raw_data, delimiter=";")
        break
    except FileNotFoundError:
        print("Fichier non trouvé. Réessayer ")

A = []
B = []
C = []
D = []

TableauAffichage = []
TempsChoisi = int(input("temps choisi "))
nbSorties = int(input("Nombre de sorties ? "))
pointDeDepart = input("Point de départ ? ")
pointDeDepart = pointDeDepart.upper()
if nbSorties == 2:

    if pointDeDepart == 'A':
        T0 = np.array([1.00, 0.00])
    elif pointDeDepart == 'B':
        T0 = np.array([0.00, 1.00])

    for i in range(TempsChoisi + 1):
        TableauAffichage.append(i)
        A.append(T0[0])
        B.append(T0[1])
        try:
            T0 = T0 @ Tp
        except ValueError:
            print("Taille de matrice différentes. Fin du programme")

    if TempsChoisi > 10:
        plot(TableauAffichage, A, "r:", label="Probabilité de A", )
        plot(TableauAffichage, B, "g:", label="Probabilité de B")
    else:
        plot(TableauAffichage, A, "r:o", label="Probabilité de A", )
        plot(TableauAffichage, B, "g:o", label="Probabilité de B", )

elif nbSorties == 3:
    if pointDeDepart == 'A':
        T0 = np.array([1.00, 0.00, 0.00])
    elif pointDeDepart == 'B':
        T0 = np.array([0.00, 1.00, 0.00])
    elif pointDeDepart == 'C':
        T0 = np.array([0.00, 0.00, 1.00])
    for i in range(TempsChoisi + 1):
        TableauAffichage.append(i)
        A.append(T0[0])
        B.append(T0[1])
        C.append(T0[2])
        try:
            T0 = T0 @ Tp
        except ValueError:
            print("Taille de matrice différentes. Fin du programme")

    if TempsChoisi > 10:
        plot(TableauAffichage, A, "r:", label="Probabilité de A", )
        plot(TableauAffichage, B, "g:", label="Probabilité de B")
        plot(TableauAffichage, C, "b:", label="Probabilité de C")
    else:
        plot(TableauAffichage, A, "r:o", label="Probabilité de A", )
        plot(TableauAffichage, B, "g:o", label="Probabilité de B", )
        plot(TableauAffichage, C, "b:o", label="Probabilité de C", )

elif nbSorties == 4:
    pointDeDepart = input("Point de départ ?")
    if pointDeDepart == 'A':
        T0 = np.array([1.00, 0.00, 0.00, 0.00])
    elif pointDeDepart == 'B':
        T0 = np.array([0.00, 1.00, 0.00, 0.00])
    elif pointDeDepart == 'C':
        T0 = np.array([0.00, 0.00, 1.00, 0.00])
    elif pointDeDepart == 'D':
        T0 = np.array([0.00, 0.00, 0.00, 1.00])
    for i in range(TempsChoisi + 1):
        TableauAffichage.append(i)
        A.append(T0[0])
        B.append(T0[1])
        C.append(T0[2])
        D.append(T0[3])
        try:
            T0 = T0 @ Tp
        except ValueError:
            print("Taille de matrice différentes. Fin du programme")

    if TempsChoisi > 10:
        plot(TableauAffichage, A, "r:", label="Probabilité de A", )
        plot(TableauAffichage, B, "g:", label="Probabilité de B")
        plot(TableauAffichage, C, "b:", label="Probabilité de C")
        plot(TableauAffichage, D, "b:", label="Probabilité de D")
    else:
        plot(TableauAffichage, A, "r:o", label="Probabilité de A", )
        plot(TableauAffichage, B, "g:o", label="Probabilité de B", )
        plot(TableauAffichage, C, "b:o", label="Probabilité de C", )
        plot(TableauAffichage, D, "b:o", label="Probabilité de D", )

else:
    print("Erreur de saisi")

xlabel("Temps")
xlim([0, TempsChoisi])
ylim([0, 1])
ylabel("Probabilité")
legend()
show()


