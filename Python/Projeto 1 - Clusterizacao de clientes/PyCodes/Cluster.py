import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
from matplotlib.colors import ListedColormap

#Loading the database
db = pd.read_csv("C:/Users/Gabriel/Portfolio/Projetos/Projeto 1/Dados/segmentation data.csv")

#Exploring the database
print("Head\n", db.head(), "\n")
print("Info\n", db.info(), "\n")
print("Describe\n", db.describe(), "\n")
print("Nunique\n", db.nunique(), "\n")

#Dropping useless columns and saving columns name and order just in case
db.drop(labels=["ID"],axis=1,inplace=True)
CList = db.columns.tolist()

#Treating data
db['Sex'] = db['Sex'].map({0:'Male', 1:'Female'})
db['Sex'] = db['Sex'].astype('string')

db['Marital status'] = db['Marital status'].map({0:'Single', 1:'Non-single'})
db['Marital status'] = db['Marital status'].astype('string')

db['Education'] = db['Education'].map({0:'Other/Unknown', 1:'High school', 2:'University', 3:'Graduate school'})
db['Education'] = db['Education'].astype('string')

db['Occupation'] = db['Occupation'].map({0:'Unemployed/Unskilled', 1:'Skilled employee/Official', 2:'Management/Self-employed/Highly qualified employee/Officer'})
db['Occupation'] = db['Occupation'].astype('string')

db['Settlement size'] = db['Settlement size'].map({0:'Small city', 1:'Mid-sized city', 2:'Big city'})
db['Settlement size'] = db['Settlement size'].astype('string')

db['Income'] = db['Income'].astype(float)

print("\n",db.dtypes,"\n")

#EDA
#cat_data = db.select_dtypes(include=['string'])
#for colname in cat_data.columns:
#    print (cat_data[colname].value_counts(), '\n')
#
#sns.countplot(x="Sex", hue="Matiral Status", data=db);
#plt.show()

#Clustering
X = db[['Age','Income']]

kmeans = KMeans(n_clusters=5, init='k-means++', max_iter=300, n_init=10, random_state=0)
y_kmeans = kmeans.fit_predict(X)
plt.scatter(X.values[y_kmeans == 0, 0], X.values[y_kmeans == 0, 1], s=100, c='red', label='Cluster 1')
plt.scatter(X.values[y_kmeans == 1, 0], X.values[y_kmeans == 1, 1], s=100, c='blue', label='Cluster 2')
plt.scatter(X.values[y_kmeans == 2, 0], X.values[y_kmeans == 2, 1], s=100, c='green', label='Cluster 3')
plt.scatter(X.values[y_kmeans == 3, 0], X.values[y_kmeans == 3, 1], s=100, c='cyan', label='Cluster 4')
plt.scatter(X.values[y_kmeans == 4, 0], X.values[y_kmeans == 4, 1], s=100, c='magenta', label='Cluster 5')
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s=300, c='yellow', label='Centroids')
plt.title('Clusters de Clientes')
plt.xlabel('Age')
plt.ylabel('Income (anually)')
plt.legend()
plt.show()