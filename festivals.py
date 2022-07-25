#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 25 12:21:30 2022

@author: heloisevanrenterghem
"""

import pandas as pd

data = pd.read_json("panorama-des-festivals.json", encoding="latin-1")

print("Il y a", data.shape[0], "festivals en PACA.\n------------------")

fields_df = pd.DataFrame(data['fields'].values.tolist(), index=data.index)
top_cities = fields_df['commune_principale'].value_counts()
print("Voici les trois villes qui accueillent le plus de festivals :\n", top_cities.head(3), "\n------------------")

top_month = fields_df['mois_indicatif_en_chiffre_y_compris_double_mois']
print(top_month.value_counts(), "\nLes .5 signifient que le festival s'étend sur deux mois.\nIl faut donc remplacer chacune de ces valeurs par deux lignes.")

months_to_add = pd.Series([6.0, 6.0, 7.0, 7.0, 7.0, 7.0, 8.0, 8.0, 8.0, 8.0, 9.0, 9.0, 9.0, 9.0, 10.0, 10.0])
months_to_drop = pd.Series([6.5, 7.5, 8.5, 9.5])
top_month = top_month.append(months_to_add, ignore_index=True)
top_month = top_month[~top_month.isin(months_to_drop)].astype('Int64').value_counts().to_frame(name="nb_festivals").reset_index(level=0).rename(columns={"index": "nb_mois"})

names_months = {1: "janvier", 2: "février", 3: "mars", 4: "avril", 5: "mai", 6: "juin", 7: "juillet", 8: "août", 9: "septembre", 10: "octobre", 11: "novembre", 12: "décembre"}
top_month['nom_mois']= top_month['nb_mois'].map(names_months)
cols = top_month.columns.tolist()
cols = cols[-1:] + cols[:-1]
top_month = top_month[cols]
print(top_month)
top_month_result = top_month.iloc[0]
print("Le mois pendant lequel il y a le plus de festivals est donc", top_month_result[0], "avec", top_month_result[-1], "festivals.")