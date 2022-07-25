#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 25 12:12:06 2022

@author: heloisevanrenterghem
"""

import pandas as pd

data = pd.read_csv("fr-esr-brevets-france-inpi-oeb.csv", sep=";", encoding="latin-1")

print(data)

data_v2 = data.drop(columns=['de_libelle', 'de_sd1_libelle', 'de_sd2_libelle', 'fe_id'], axis=1)

print(data_v2)