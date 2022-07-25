#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 25 15:32:37 2022

@author: heloisevanrenterghem
"""
import numpy as np

import sqlite3
baseDeDonnees = sqlite3.connect('py066-ma_banque.db')
curseur = baseDeDonnees.cursor()

print("\n1) Voici tous les clients :")
curseur.execute("SELECT nom, prenom FROM client")
for x in curseur.fetchall():
    print(x)

print("\n2) Voici les clients domiciliés à Paris :")
curseur.execute("SELECT nom, prenom FROM client WHERE ville = 'Paris'")
for x in curseur.fetchall():
    print(x)
    
print("\n3) Voici les identifiants des comptes de type Livret A :")
curseur.execute("SELECT idcompte FROM compte WHERE type = 'Livret A'")
id_livret_a = []
for x in curseur.fetchall():
    id_livret_a.append(list(x))
print(list(np.hstack(id_livret_a)))

print("\n4) Voici les identifiants des opérations de débit sur le compte d’identifiant égal à 1 :")
curseur.execute("SELECT idop FROM operation WHERE montant LIKE '-%'")
id_op_debit = []
for x in curseur.fetchall():
    id_op_debit.append(list(x))
print(list(np.hstack(id_op_debit)))

print("\n5) Voici, sans doublon, les identifiants des propriétaires de livret A, classés par ordre croissant :")
curseur.execute("SELECT idproprietaire FROM compte WHERE type = 'Livret A' ORDER BY idproprietaire")
id_prop_livret_a = []
for x in curseur.fetchall():
    id_prop_livret_a.append(list(x))
print(list(np.unique(np.hstack(id_prop_livret_a))))

print("\n6) Voici les identifiants des clients n'ayant pas de livret A' :")
curseur.execute("SELECT idproprietaire FROM compte WHERE type NOT LIKE 'Livret A' ORDER BY idproprietaire")
id_prop_no_livret_a = []
for x in curseur.fetchall():
    id_prop_no_livret_a.append(list(x))
id_prop_no_livret_a = [x for x in id_prop_no_livret_a if x not in id_prop_livret_a]
print(list(np.unique(np.hstack(id_prop_no_livret_a))))

print("\n7) Voici l’identifiant de compte et le type de compte des clients habitant à Paris :")
curseur.execute("SELECT idcompte, type FROM client JOIN compte ON client.idclient = compte.idproprietaire WHERE ville = 'Paris'")
comptes_paris = []
for x in curseur.fetchall():
    comptes_paris.append(list(x))
print(comptes_paris)

print("\n8) Voici la liste des comptes et les types de comptes de Dumbledore :")
curseur.execute("SELECT idcompte, type FROM client JOIN compte ON client.idclient = compte.idproprietaire WHERE nom = 'Dumbledore'")
comptes_dumbledore = []
for x in curseur.fetchall():
    comptes_dumbledore.append(list(x))
print(comptes_dumbledore)

print("\n9) Voici le nombre de clients par ville, classé par l'ordre alphabétique des villes :")
curseur.execute("SELECT ville, count(*) AS nb_clients FROM client GROUP By ville ORDER BY ville")
for x in curseur.fetchall():
    print(x)

print("\n10) Voici la ville ayant le plus de clients :")
curseur.execute("SELECT ville, count(*) AS nb_clients FROM client GROUP By ville ORDER BY nb_clients DESC")
top_city = curseur.fetchone()
print(top_city[0], "avec", top_city[1], "clients")

print("\n11) Voici le nombre d’opérations effectuées sur chaque compte :")
curseur.execute("SELECT idcompte, count(*) AS nb_op FROM operation GROUP BY idcompte")
nb_op = []
for x in curseur.fetchall():
    nb_op.append(list(x))
print(nb_op)

print("\n12/13) Voici le nombre maximum d’opérations effectuées sur un compte et le n° de compte associé :")
curseur.execute("SELECT idcompte, count(*) AS nb_op FROM operation GROUP BY idcompte ORDER BY nb_op DESC")
max_op = curseur.fetchone()
print(f"{max_op[1]} (compte n°{max_op[0]})")

print("\n14) Voici, type par type, la moyenne des soldes des comptes (tous clients confondus) de chaque type (en supposant qu’initialement, les comptes sont tous vides):")
curseur.execute("SELECT type, AVG(montant) FROM compte JOIN operation ON compte.idcompte = operation.idcompte GROUP BY type")
for x in curseur.fetchall():
    print(x)

print("\n15) Voici, classés par nom et prénom, le nom, le prénom, le type de compte, et le solde, pour tous les comptes :")
curseur.execute("SELECT compte.idcompte, nom, prenom, type, SUM(montant) FROM compte LEFT JOIN client ON client.idclient = compte.idproprietaire LEFT JOIN operation ON compte.idcompte = operation.idcompte GROUP BY compte.idcompte ORDER BY nom, prenom")
for x in curseur.fetchall():
    print(x)

print("\n16) Idem, en se limitant aux clients dont le nom commence par K, L, M ou N :")
curseur.execute("SELECT compte.idcompte, nom, prenom, type, SUM(montant) FROM compte LEFT JOIN client ON client.idclient = compte.idproprietaire LEFT JOIN operation ON compte.idcompte = operation.idcompte WHERE nom LIKE 'K%' OR nom LIKE 'L%' OR nom LIKE 'M%' or nom LIKE 'N%' GROUP BY compte.idcompte ORDER BY nom, prenom")
for x in curseur.fetchall():
    print(x)

print("\n17) Voici le nom et le prénom des personnes ayant débité au moins un chèque sur leur compte courant, classé par nom :")
curseur.execute("SELECT DISTINCT nom, prenom FROM client JOIN compte ON client.idclient = compte.idproprietaire JOIN operation ON compte.idcompte = operation.idcompte WHERE type = 'Compte Courant' AND informations = 'Cheque' AND montant LIKE '-%' ORDER BY nom, prenom")
for x in curseur.fetchall():
    print(x)

print("\n18) Voici le nom, prénom et ville de tous les clients ayant réalisé un nombre maximal d’opérations au guichet :")
curseur.execute("SELECT nom, prenom, ville, MAX(nb_op) FROM (SELECT nom, prenom, ville, count(*) AS nb_op FROM client JOIN compte ON client.idclient = compte.idproprietaire JOIN operation On compte.idcompte = operation.idcompte GROUP BY client.idclient)")
for x in curseur.fetchall():
    print(x)

print("\n19) Voici la moyenne par ville des fortunes totales des clients (somme sur tous leurs comptes), classé par valeur croissante :")
curseur.execute("SELECT ville, AVG(sum_comptes) FROM (SELECT idclient, nom, prenom, ville, SUM(montant) AS sum_comptes FROM client JOIN compte ON client.idclient = compte.idproprietaire JOIN operation On compte.idcompte = operation.idcompte GROUP BY idclient) GROUP BY ville")
for x in curseur.fetchall():
    print(x)
