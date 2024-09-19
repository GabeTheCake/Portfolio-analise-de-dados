import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

db = pd.read_csv('C:/Users/conta/Portfolio/Projetos/Projeto 2/Dados/churn_data.csv')
db1 = pd.read_csv('C:/Users/conta/Portfolio/Projetos/Projeto 2/Dados/customer_data.csv')
db2 = pd.read_csv('C:/Users/conta/Portfolio/Projetos/Projeto 2/Dados/internet_data.csv')

pd.set_option('display.max_columns',None)
merged = pd.merge(db1,db,on='customerID')
result = pd.merge(merged,db2, on='customerID')

print('\n\n\n\n\n\n\n\n', result.head())

#EDA
cat_data = result.select_dtypes(include=['string'])
for colname in cat_data.columns:
    print (cat_data[colname].value_counts(), '\n')

sns.countplot(x="Dependents", hue="gender", data=result);
plt.title('Amount of clients by gender')
plt.xlabel('Gender')
plt.ylabel('Amount')
plt.show()

