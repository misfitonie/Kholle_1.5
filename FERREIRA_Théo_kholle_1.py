#!/usr/bin/python3.6
# Khôlles
# Opérations simples sur liste d'entier stockée sur un fichier .csv
# 22/11/2018
# FERREIRA Théo



#--------IMPORTATION--------#


import argparse
import csv
from statistics import mean


#----------OPTION-----------#


parser = argparse.ArgumentParser()
parser.add_argument("-l", action="store_true", help="Contenu liste")
parser.add_argument("-a", nargs="+", help="Ajouter valeur")
parser.add_argument("-c", action="store_true", help="Supprime toute valeur")
parser.add_argument("-s", action="store_true")
parser.add_argument("--max", action="store_true", help="Affiche valeur max")
parser.add_argument("--min", action="store_true", help="Affiche valeur min")
parser.add_argument("--moy", action="store_true", help="Affiche valeur moyenne")
parser.add_argument("--sum", action="store_true", help="Calcul la somme")
parser.add_argument("-t", action="store_true", help="Trie croissant")
parser.add_argument("--desc", action="store_true", help="Trie décroissant")

args = parser.parse_args()


#------LISTE--VARIABLES-----#

liste = []


#------LISTE--FONCTIONS-----#



#Lit le fichier csv
def lire_csv():
    with open("./liste_item.csv", "r") as file_csv:
        csv_reader = csv.reader(file_csv)
        for ligne in csv_reader:
            for i in range(0, len(ligne)):
                liste.append(ligne[i])


#Ecrit dans le fichier csv
def ecrit_csv(value):
    with open("./liste_item.csv", "w") as file_csv:
        csv_write = csv.writer(file_csv)
        csv_write.writerow(value)

#Ajoute un item au fichier csv
def ajout_item(value):
    liste.append(value)


#Liste les valeur du fichier csv
def affiche_liste():
    lire_csv()
    for row in liste:
        print(row)


#Supprime les valeur du fichier csv
def suppr_all():
    lire_csv()
    while len(liste) > 0:
        del liste[0]
    ecrit_csv(liste)


#Affiche la plus grande valeur du fichier csv
def max_score():
    lire_csv()
    liste_max = [int(a) for a in liste]
    value_max = max(liste_max)
    print(value_max)


#Affiche la plus petite valeur du fichier csv
def min_score():
    lire_csv()
    liste_min = [int(a) for a in liste]
    value_min = min(liste_min)
    print(value_min)


#Affiche la moyenne des valeurs du fichier csv
def moy_score():
    lire_csv()
    liste_moy = [int(a) for a in liste]
    value_moy = mean(liste_moy)
    print(value_moy)


#Calcule la somme des valeurs du fichier csv
def sum_score():
    lire_csv()
    liste_sum = [int(a) for a in liste]
    value_sum = sum(liste_sum)
    print(value_sum)

#Afffiche les valeurs du fichier csv de manière décroissante
def desc_score():
    lire_csv()
    liste_desc = [int(a) for a in liste]
    liste_desc.sort(reverse = True)
    ecrit_csv(liste_desc)

#Afffiche les valeurs du fichier csv de manière croissante
def asc_score():
    lire_csv()
    liste_asc = [int(a) for a in liste]
    liste_asc.sort(reverse = False)
    ecrit_csv(liste_asc)




#---------MAIN-----CODE-----#


if args.l:
    affiche_liste()


elif args.a:
    lire_csv()
    for num in args.a:
        ajout_item(num)
    ecrit_csv(liste)

elif args.c:
    suppr_all()

elif args.s:
    if args.max:
        max_score()
    elif args.min:
       min_score()
    elif args.moy:
        moy_score()
    elif args.sum:
        sum_score()

elif args.t:
    if args.desc:
        desc_score()
    else:
        asc_score()

