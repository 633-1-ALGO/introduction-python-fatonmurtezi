# Problème : Calculer le prix TTC d'une nombre d'articles ayant un prix unitaire donné. Avec une T.V.A à 7.7%.
# Données : Nombres d'articles et prix unitaire HT
# Résultat attendu : Un message "Le prix TTC est de XXX.XXX chf." Utilisez la fonction print().

nb_articles = 13
prix_ht = 42.75

tva = 7.7/100

total = nb_articles * prix_ht * tva + (nb_articles* prix_ht)

print("Le prix TTC est de ",total," chf.")
