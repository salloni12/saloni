# -*- coding: utf-8 -*-
"""
Created on Thu Jun  8 11:16:58 2017

@author: saloni.kothari
"""

import pandas as pd
from sklearn.preprocessing import LabelEncoder

datasetTrans=pd.read_csv("C:\\Users\\saloni.kothari\\Downloads\\CodeGladiators-Invesco-DataSet\\Code Gladiators-Invesco-DataSet\\Code-Gladiators-Transaction.csv")
datsetAum=pd.read_csv("C:\\Users\\saloni.kothari\\Downloads\\CodeGladiators-Invesco-DataSet\\Code Gladiators-Invesco-DataSet\\Code-Gladiators-AUM.csv")
datsetInesExp=pd.read_csv("C:\\Users\\saloni.kothari\\Downloads\\CodeGladiators-Invesco-DataSet\\Code Gladiators-Invesco-DataSet\\Code-Gladiators-InvestmentExperience.csv")
datsetActivity=pd.read_csv("C:\\Users\\saloni.kothari\\Downloads\\CodeGladiators-Invesco-DataSet\\Code Gladiators-Invesco-DataSet\\Code-Gladiators-Activity.csv")


Advisor_id = raw_input("enter advisor id:")
investment_id=input("enter investment id:")
