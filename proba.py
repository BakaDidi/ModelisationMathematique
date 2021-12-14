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
E = []

print(Tp.shape)
TableauAffichage = []
TempsChoisi = int(input("temps choisi "))
pointDeDepart = input("Point de départ ? ")
pointDeDepart = pointDeDepart.upper()
if Tp.shape == (2, 2):

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

elif Tp.shape == (3, 3):
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

elif Tp.shape == (4, 4):
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
        plot(TableauAffichage, D, "c:", label="Probabilité de D")
    else:
        plot(TableauAffichage, A, "r:o", label="Probabilité de A", )
        plot(TableauAffichage, B, "g:o", label="Probabilité de B", )
        plot(TableauAffichage, C, "b:o", label="Probabilité de C", )
        plot(TableauAffichage, D, "c:o", label="Probabilité de D", )

elif Tp.shape == (5, 5):
    pointDeDepart = input("Point de départ ?")
    if pointDeDepart == 'A':
        T0 = np.array([1.00, 0.00, 0.00, 0.00, 0.00])
    elif pointDeDepart == 'B':
        T0 = np.array([0.00, 1.00, 0.00, 0.00, 0.00])
    elif pointDeDepart == 'C':
        T0 = np.array([0.00, 0.00, 1.00, 0.00, 0.00])
    elif pointDeDepart == 'D':
        T0 = np.array([0.00, 0.00, 0.00, 1.00, 0.00])
    elif pointDeDepart == 'E':
        T0 = np.array([0.00, 0.00, 0.00, 0.00, 1.00])

    for i in range(TempsChoisi + 1):
        TableauAffichage.append(i)
        A.append(T0[0])
        B.append(T0[1])
        C.append(T0[2])
        D.append(T0[3])
        E.append(T0[4])
        try:
            T0 = T0 @ Tp
        except ValueError:
            print("Taille de matrice différentes. Fin du programme")

    if TempsChoisi > 10:
        plot(TableauAffichage, A, "r:", label="Probabilité de A", )
        plot(TableauAffichage, B, "g:", label="Probabilité de B")
        plot(TableauAffichage, C, "b:", label="Probabilité de C")
        plot(TableauAffichage, D, "c:", label="Probabilité de D")
        plot(TableauAffichage, E, "m:", label="Probabilité de E")
    else:
        plot(TableauAffichage, A, "r:o", label="Probabilité de A", )
        plot(TableauAffichage, B, "g:o", label="Probabilité de B", )
        plot(TableauAffichage, C, "b:o", label="Probabilité de C", )
        plot(TableauAffichage, D, "c:o", label="Probabilité de D", )
        plot(TableauAffichage, E, "m:o", label="Probabilité de E")




else:
    print("Erreur de saisi")

xlabel("Temps")
xlim([0, TempsChoisi])
ylim([0, 1])
ylabel("Probabilité")
legend()
show()