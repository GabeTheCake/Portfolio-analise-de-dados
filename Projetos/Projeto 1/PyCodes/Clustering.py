import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
import seaborn as sns

#Loading the database
db = pd.read_csv("C:/Users/conta/Portfolio/Projetos/Projeto 1/Dados/segmentation data.csv")

#Dropping useless columns
db.drop(labels=["ID"],axis=1,inplace=True)
CList = db.columns.tolist()

#Exploring the database - shallow
print(db.shape)
print(db.head())
print(db.describe())
print(db.nunique())

# HEATMAP
corr = db.corr()
plt.figure(figsize=(10, 8))
sns.heatmap(corr, annot=True, cmap='coolwarm', center=0)
plt.show()

#Treating data - Seems to be no need for this DF to be cleanned. However I changed numbers from the legends archive to make it more easy to read and understand
db['Sex'] = db['Sex'].map({0:'Male', 1:'Female'})
db['Sex'] = db['Sex'].astype('string')

db['Marital status'] = db['Marital status'].map({0:'Single', 1:'Non-single'})
db['Marital status'] = db['Marital status'].astype('string')

db['Education'] = db['Education'].map({0:'other;unknown', 1:'High school', 2:'University', 3:'Graduate school'})
db['Education'] = db['Education'].astype('string')

db['Occupation'] = db['Occupation'].map({0:'Unemployed/Unskilled', 1:'Skilled employee/Official', 2:'Management/Self-employed/Highly qualified employee/Officer'})
db['Occupation'] = db['Occupation'].astype('string')

db['Settlement size'] = db['Settlement size'].map({0:'Small city', 1:'Mid-sized city', 2:'Big city'})
db['Settlement size'] = db['Settlement size'].astype('string')

db['Age'] = db['Age'].astype(int)
db['Income'] = db['Income'].astype(float)

print("\n\n\n",db.dtypes,"\n\n\n")

#EDA - deep
cat_data = db.select_dtypes(include=['string'])
for colname in cat_data.columns:
    print (cat_data[colname].value_counts(), '\n')

sns.countplot(x="Marital status", hue="Sex", data=db);
plt.savefig('Count_Marital_vs_Genre.png')
plt.show()
