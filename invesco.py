# -*- coding: utf-8 -*-
"""
Created on Tue Jun  6 12:10:45 2017

@author: Saloni.Kothari
"""

import pandas as pd
from sklearn.preprocessing import LabelEncoder


le = LabelEncoder()

datasetTrans=pd.read_csv("C:\\Users\\saloni.kothari\\Downloads\\CodeGladiators-Invesco-DataSet\\Code Gladiators-Invesco-DataSet\\Code-Gladiators-Transaction.csv")
datsetAum=pd.read_csv("C:\\Users\\saloni.kothari\\Downloads\\CodeGladiators-Invesco-DataSet\\Code Gladiators-Invesco-DataSet\\Code-Gladiators-AUM.csv")
datsetInesExp=pd.read_csv("C:\\Users\\saloni.kothari\\Downloads\\CodeGladiators-Invesco-DataSet\\Code Gladiators-Invesco-DataSet\\Code-Gladiators-InvestmentExperience.csv")
datsetActivity=pd.read_csv("C:\\Users\\saloni.kothari\\Downloads\\CodeGladiators-Invesco-DataSet\\Code Gladiators-Invesco-DataSet\\Code-Gladiators-Activity.csv")

Advisor_id = input("enter advisor id:")
investment_id=input("enter investment id:")

#if Advisor_id == unique_Advisor_id and investment_id == unique_investment_id:
    

transAum_dataset=pd.merge(datasetTrans,datsetAum,how='left',left_on=['Unique_Investment_Id','Unique_Advisor_Id','Month'], right_on=['Unique_Investment_Id','Unique_Advisor_Id','Month'])
transauminverexp_datset=pd.merge(transAum_dataset,datsetInesExp,how="left",left_on=['Unique_Investment_Id','Month'],right_on=['Unique_Investment_Id','Month'])
transauminesexpactivity_dataset=pd.merge(transauminverexp_datset,datsetActivity,how="inner",left_on=['Unique_Advisor_Id','Month'],right_on=['Unique_Advisor_Id','Month'])

transAum_dataset=transAum_dataset.fillna(method = 'ffill')
transauminesexpactivity_dataset = transauminesexpactivity_dataset.fillna(method = 'backfill') 
transAum_dataset=transAum_dataset.drop(['Code_1','Code_2','Code_3','Code_4','Code_5'],1)
transauminverexp_datset=transauminverexp_datset.drop(['Code_1','Code_2','Code_3','Code_4','Code_5','Morningstar Category','Investment'],1)
transauminesexpactivity_dataset=transauminesexpactivity_dataset.drop(['Code_1','Code_2','Code_3','Code_4','Code_5','Activity_Type'],1)
#feature=transAum_dataset.columns.values
#feature=transAum_dataset.columns.values


feature=transauminverexp_datset.columns.values
for f in feature:
    print(f)

le.fit(transauminesexpactivity_dataset['Month'])
transauminesexpactivity_dataset['Month']=le.transform(transauminesexpactivity_dataset['Month'])

le.fit(transauminesexpactivity_dataset['Transaction_Type'])
transauminesexpactivity_dataset['Transaction_Type']=le.transform(transauminesexpactivity_dataset['Transaction_Type'])


transauminesexpactivity_dataset.drop(['Morningstar Category','Investment'],1,inplace=True)
transauminesexpactivity_dataset.to_csv("C:\\Users\\saloni.kothari\\Downloads\\transauminesexpactivity.csv")


transauminverexp_datset = transauminverexp_datset.fillna(method = 'ffill')
transauminesexpactivity_dataset = transauminesexpactivity_dataset.fillna(method = 'ffill')

dumpdata=transauminesexpactivity_dataset[(transauminesexpactivity_dataset['Month']!=12)]
testingdata=dumpdata[(dumpdata['Month']==10)]

trainingdata=dumpdata[(dumpdata['Month']!=10)]

trainingdata.to_csv('trainingdata.csv')

testingdata.to_csv('testingdata.csv')


