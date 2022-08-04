# GO FOR EXTRACT

## 2.1. Extraction d'un fichier csv

Tu l'as déjà fait plusieurs fois mais ça vaut le coup de le refaire car c'est très fréquent de devoir travailler sur des fichiers csv déjà existants.

Le jeu de données qui nous intéresse aujourd'hui met à disposition la base de données brevets de l’INPI. Chaque brevet est géo-localisés à différents niveaux selon l'adresse des déposants et des inventeurs : pays, régions, départements, unités urbaines, communes.

Nous te demandons ici d'extraire le fichier csv, de supprimer les quatres dernières colonnes, puis de l'afficher.

## 2.2. Extraction d'un fichier json

Direction le Suuuuuud 😎

Sur cette page, tu vas trouver le panorama des festivals en PACA. Télécharge le fichier Json et extrais ses données.

Dis-nous combien il y a de festivals en PACA, quelles sont les 3 villes qui accueillent la majorité des festivals et quel est le mois de l'année le plus chargé en festivals.

## 2.3. Extraction à partir d'une base de données

Finies les vacances, retour à la vraie vie 💼💼 : tu enfiles ton costume de banquier pour aller requêter une base de données qui contient tous tes clients.

Tu vas devoir manipuler cette base de données via Python. Cela nécessite l’import de la librairie 'sqlite3'. Replonge dans la ressource et suis les étapes nécessaires pour accéder à la base de données.

Voici la liste des requêtes que tu dois réaliser sur cette base de données :
- Donner le nom et le prénom de tous les clients.
- Donner le nom et le prénom des clients habitant à Paris.
- Donner les identifiants des comptes de type Livret A.
- Donner les identifiants des opérations de débit sur le compte d’identifiant égal à 1.
- Donner, sans doublon, les identifiants des propriétaires de livret A, classés par ordre croissant.
- Donner l’identifiant des clients n’ayant pas de livret A.
- Donner l’identifiant de compte et le type de compte des clients habitant à Paris.
- Donner la liste des comptes et les types de compte de Dumbledore.
- Donner le nombre de clients par ville, classé par ordre alphabétique de villes.
- Donner la ville ayant le plus de clients.
- Trouver le nombre d’opérations effectuées sur chaque compte.
- Trouver le nombre maximum d’opérations effectuées sur un compte.
- Trouver le ou les numéros de compte réalisant le maximum de la question précédente.
- Afficher, type par type, la moyenne des soldes des comptes (tous clients confondus) de chaque type (en supposant qu’initialement, les comptes sont tous vides).
- Afficher, classé par nom et prénom, le nom, le prénom, le type de compte, et le solde, pour tous les comptes.
- Même question, en se limitant aux clients dont le nom commence par K,L,M ou N.
- Afficher le nom et le prénom des personnes ayant débité au moins un chèque sur leur compte courant, classé par nom.
- Nom, prénom et ville de tous les clients ayant réalisé un nombre maximal d’opérations au guichet.
- Moyenne par ville des fortunes totales des clients (somme sur tous leurs comptes), classé par valeur croissante.

## 2.4. Extraction en scrapant le web

Tu t'es déjà exercé au scraping avec Ruby. Essaye maintenant de réaliser le dernier exercice du scrappeur fou avec Python. Voici la consigne au cas où tu aies oublié :

Tu dois récupérer la liste complète des députés de France ainsi que leurs adresses e-mail. Cherche par toi-même le site le plus aisé à scrapper et stocke les informations extraites dans le format qui te plaît le plus.

## 2.5. Extraction à partir d'une API

Tu possèdes des clés de l'API Twitter, quelle chance ! On va s'en reservir aujourd'hui : à toi d'extraire des infos de la twitosphère ...

Twitter est une mine d'or de données. Contrairement aux autres plateformes sociales, presque tous les tweets des utilisateurs sont entièrement publics et extractibles. C'est un énorme avantage si tu essayes d'obtenir une grande quantité de données sur lesquelles exécuter des analyses.

Ton défi du jour : extraire l'ensemble des tweets publiés dans la journée en lien avec le "PSG" ou l'"OM", comme tu préfères 🙂🙃 Tu compileras ensuite ces tweets dans un fichier Excel.
