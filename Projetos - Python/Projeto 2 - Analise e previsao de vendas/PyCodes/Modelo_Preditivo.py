import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

db = pd.read_csv('C:/Users/conta/Portfolio/Projetos/Projeto 2 - Analise e previsao de vendas/Dados/churn_data.csv')
db1 = pd.read_csv('C:/Users/conta/Portfolio/Projetos/Projeto 2 - Analise e previsao de vendas/Dados/customer_data.csv')
db2 = pd.read_csv('C:/Users/conta/Portfolio/Projetos/Projeto 2 - Analise e previsao de vendas/Dados/internet_data.csv')

pd.set_option('display.max_columns',None)
merged = pd.merge(db1,db,on='customerID')
result = pd.merge(merged,db2, on='customerID')

print('\n\n\n\n\n\n\n\n', result.head())
print(result.info())

#EDA
cat_data = result.select_dtypes(include=['string'])
for colname in cat_data.columns:
    print (cat_data[colname].value_counts(), '\n')

Xx= "TotalCharges"
Yy= "gender"
sns.countplot(x= Xx, hue= Yy, data=result);
plt.title(f'Graph of {Xx} vs {Yy}')
plt.show()

