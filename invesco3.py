# -*- coding: utf-8 -*-
"""
Created on Thu Jun  8 14:19:03 2017

@author: saloni.kothari
"""


import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder
import numpy as np
import sklearn.metrics as metric 

# HAVEN'T USED YET. FOR FUTURE PURPOSE
date_dic = {1:"2015 / 01",
            2:"2015 / 02",
            3:"2015 / 03",
            4:"2015 / 04",
            5:"2015 / 05",
            6:"2015 / 06",
            7:"2015 / 07",
            8:"2015 / 08",
            9:"2015 / 09",
            10:"2015 / 10",
            11:"2015 / 11",
            12:"2015 / 12",
            13:"2016 / 01",
            14:"2016 / 02",
            15:"2016 / 03",
            16:"2016 / 04",
            17:"2016 / 05",
            18:"2016 / 06",
            19:"2016 / 07",
            20:"2016 / 08",
            21:"2016 / 09",
            22:"2016 / 10",
            23:"2016 / 11",
            24:"2016 / 12"}

lb = LabelEncoder()
datasetTrans=pd.read_csv("C:\\Users\\saloni.kothari\\Downloads\\CodeGladiators-Invesco-DataSet\\Code Gladiators-Invesco-DataSet\\Code-Gladiators-Transaction.csv")
datasetAum=pd.read_csv("C:\\Users\\saloni.kothari\\Downloads\\CodeGladiators-Invesco-DataSet\\Code Gladiators-Invesco-DataSet\\Code-Gladiators-AUM.csv")
datasetInesExp=pd.read_csv("C:\\Users\\saloni.kothari\\Downloads\\CodeGladiators-Invesco-DataSet\\Code Gladiators-Invesco-DataSet\\Code-Gladiators-InvestmentExperience.csv")
datasetActivity=pd.read_csv("C:\\Users\\saloni.kothari\\Downloads\\CodeGladiators-Invesco-DataSet\\Code Gladiators-Invesco-DataSet\\Code-Gladiators-Activity.csv")


print("Replacing NaNs")
datasetTrans = datasetTrans.fillna(0)
print("datasetTrans NaNs replaced")
datasetAum = datasetAum.fillna(method = 'pad')
print("datasetAum NaNs replaced")
datasetInesExp = datasetInesExp.fillna(datasetInesExp.mean())
print("datasetInesExp NaNs replaced")
datasetActivity = datasetActivity.fillna(0)
print("datasetActivity NaNs replaced")


# TRAINING THE INVESTMENTS ACCORDING TO THEIR CLASSES (P/R)
trans_temp = datasetTrans[["Unique_Investment_Id","Month","Transaction_Type"]].copy()
trans_temp = trans_temp.drop_duplicates()
exp_temp = datasetInesExp.drop(["Morningstar Category","Investment"],1)
temp_data = pd.merge(trans_temp, exp_temp, how = "left", left_on=['Unique_Investment_Id','Month'], right_on=['Unique_Investment_Id','Month'])
temp_data = temp_data.fillna(temp_data.mean())
available_inv_id = temp_data["Unique_Investment_Id"].drop_duplicates()

print("size:",temp_data.shape[0])
for i in range(0,temp_data.shape[0]):
    inv_id = temp_data.iloc[i].get("Unique_Investment_Id")
    month = temp_data.iloc[i].get("Month")
    if i < temp_data.shape[0]-1:
        next_inv_id = temp_data.iloc[i+1].get("Unique_Investment_Id")
        next_month = temp_data.iloc[i+1].get("Month")
    if inv_id == next_inv_id and month != next_month and i == 0:
        X_data = pd.DataFrame(temp_data.iloc[i].to_frame().T)
        Y_data = pd.DataFrame(temp_data.iloc[i+1].to_frame().T)
    if inv_id == next_inv_id and month != next_month and i < temp_data.shape[0]:
        X_data = X_data.append(temp_data.iloc[i].to_frame().T)
        Y_data = Y_data.append(temp_data.iloc[i+1].to_frame().T)
        
y_data = np.array(Y_data["Transaction_Type"])
x_data = X_data.drop(["Unique_Investment_Id","Month","Transaction_Type"],1)

logit = LogisticRegression()
logit.fit(x_data, y_data)