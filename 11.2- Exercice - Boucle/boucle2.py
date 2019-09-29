# Problème : Etant donné un tableau B de "n" nombres réels, on demande de trier le tableau B avec le tri par insertion
# Données : un tableau B de n nombre réels
# Résultat attendu : Le tableau B trié

B = [2, 6, 8, 5, 4, 12, 98, 34, 1]

cpt = 0
for i in range(1, len(B) ):
    for j in range(1, len(B)):
        if B[i] > B[j]:
            print(B[i])
