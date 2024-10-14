<h1 align="center">Projeto 1: Customer Clustering</h1>

<p align="justify">
O seguinte projeto fora desenvolvido com base no banco de dados encontrado no site Kaggle. Este banco de dados, o qual chamaremos de bd daqui para frente, possui o nome de Customer Clustering e possui dois arquivos .csv, um chamado “Segmentation data” e outro “Segmentation data legend”. Devido as capacidades que se busca provar com este trabalho, tal bd apresentou-se como apropriado para utilização devido a sua simplicidade e quão rico é em informações de variados tipos. Em um primeiro momento em contato com o banco de dados, sabe-se que as informações extraídas deste bd podem ou não apresentar relações entre si bem como podem ou não demonstrar indicativos de padrões após uma análise mais profunda.
	
Na descrição do banco de dados existia a seguinte descrição:
</p>	

	“Customer Segmentation is the subdivision of a market into discrete customer groups that share similar characteristics. Customer Segmentation can be a
	powerful means to identify unsatisfied customer needs. Using the above data companies can then outperform the competition by developing uniquely appealing
	products and services. You are owing a supermarket mall and through membership cards, you have some basic data about your customers like Customer ID, age,
 	gender, annual income 	and spending score. You want to understand the customers like who are the target customers so that the sense can be given to
  	marketing team and plan the strategy accordingly.”
 
<p align="justify">
Com base na descrição, pode-se saber qual trabalho deve ser executado em tal db. Quer-se saber qual o cliente alvo, qual a condição financeira e o que mais podemos saber sobre ele para com que se possa informar ao setor de marketing e planejar uma estratégia de acordo.
Após o download dos arquivos e processa-los para a visualização no software IDLE (“Compilador de Python’), estudou-se as informações que nele continha, a partir dai começou-se um processo por passos. A seguir estão os processos do início ao fim dos trabalhos exercidos com base nos dados baixados.
</p>

## 1º passo: Definir perguntas que irão definir os processos que serão realizados e definir os processos com base nas perguntas.

Perguntas feitas: 

	Quais os cliente mais recorrentes? Qual o cliente alvo?
	Qual a condições financeira do cliente alvo?
 	Qual o estado civil do cliente alvo?
  	Qual o grau de estudo do cliente alvo?

## 2º passo: Definir e Importar bibliotecas que serão utilizadas.

Para a leitura e manejo dos bancos de dados será utilizada a biblioteca PANDAS. 
Para a plotagem, a transformação dos dados em gráficos e visuais, sera utilizado Matplotlib.pyplot. 
Para tambem auxiliar com gráficos e artigos visuais será importado o Seaborn.

 	import pandas as pd
	import numpy as np
	import matplotlib.pyplot as plt
	import seaborn as sns
	from sklearn.cluster import KMeans
	from matplotlib.colors import ListedColormap

## 3º passo: Carregar bancos de dados (bd) ou database (db) em inglês.
No código chamaremos a base de dados, database, de db. 

	db = pd.read_csv("C:/Users/conta/Portfolio/Projetos/Projeto 1/Dados/segmentation data.csv")

## 4º passo: Explorar banco de dados.
Com alguns comandos básicos analisou-se a estrutura do banco de dados, as colunas, tipo de dados armazenados nas colunas, o tamanho do mesmo, quantidade de linhas e colunas que ele possuia, quantidade de dados únicos e quantidade de dados nulos ou faltantes bem como linhas em branco.

	print("Head\n", db.head(), "\n")
	print("Info\n", db.info(), "\n")
	print("Describe\n", db.describe(), "\n")
	print("Nunique\n", db.nunique(), "\n")

<p align="center"><b>Output</b> </p>
<b> HEAD </b>

|  |         ID | Sex | Marital status | Age | Education | Income | Occupation | Settlement size|
|--|------------|-----|----------------|-----|-----------|--------|------------|----------------|
|0 | 100000001  |  0  |             0  |67   |          2| 124670 |          1 |               2|
|1 | 100000002  |  1  |             1  |22   |          1| 150773 |          1 |               2|
|2 | 100000003  |  0  |             0  |49   |          1|  89210 |          0 |               0|
|3 | 100000004  |  0  |             0  |45   |          1| 171565 |          1 |               1|
|4 | 100000005  |  0  |             0  |53   |          1| 149031 |          1 |               1|

[5 rows x 8 columns] 

<b> INFO </b>

<class 'pandas.core.frame.DataFrame'>
RangeIndex: 2000 entries, 0 to 1999
Data columns (total 8 columns):
| # |  Column          | Non-Null Count | Dtype|
|---|------------------|--------------- |------|
| 0 |  ID              | 2000 non-null  | int64|
| 1 |  Sex             | 2000 non-null  | int64|
| 2 |  Marital status  | 2000 non-null  | int64|
| 3 |  Age             | 2000 non-null  | int64|
| 4 |  Education       | 2000 non-null  | int64|
| 5 |  Income          | 2000 non-null  | int64|
| 6 |  Occupation      | 2000 non-null  | int64|
| 7 |  Settlement size | 2000 non-null  | int64|

dtypes: int64(8)
memory usage: 125.1 KB

<b> DESCRIBE </b>

|    |     ID      |     Sex     |Marital status|     Age    |  Education  |    Income    | Occupation  | Settlement size|
|----|-------------|-------------|--------------|------------|-------------|--------------|-------------|----------------|
|count|2.000000e+03| 2000.000000 |  2000.000000 |2000.000000 |  2000.00000 |   2000.000000| 2000.000000 |     2000.000000|
|mean |1.000010e+08|    0.457000 |     0.496500 |  35.909000 |     1.03800 | 120954.419000|    0.810500 |        0.739000|
|std  |5.774946e+02|    0.498272 |     0.500113 |  11.719402 |     0.59978 |  38108.824679|    0.638587 |        0.812533|
|min  |1.000000e+08|    0.000000 |     0.000000 |  18.000000 |     0.00000 |  35832.000000|    0.000000 |        0.000000|
|25%  |1.000005e+08|    0.000000 |     0.000000 |  27.000000 |     1.00000 |  97663.250000|    0.000000 |        0.000000|
|50%  |1.000010e+08|    0.000000 |     0.000000 |  33.000000 |     1.00000 | 115548.500000|    1.000000 |        1.000000|
|75%  |1.000015e+08|    1.000000 |     1.000000 |  42.000000 |     1.00000 | 138072.250000|    1.000000 |        1.000000|
|max  |1.000020e+08|    1.000000 |     1.000000 |  76.000000 |     3.00000 | 309364.000000|    2.000000 |        2.000000|

<b> NUNIQUE </b>

|Columns          |Unique Values|
|-----------------|------|
|ID               |  2000|
|Sex              |     2|
|Marital status   |     2|
|Age              |    58|
|Education        |     4|
|Income           |  1982|
|Occupation       |     3|
|Settlement size  |     3|

dtype: int64

Neste ultimo comando, fora necessario acrescentar manualmente para melhor visualização deste documento a parte superior da tabela: "Columns" e "Unique Values".

## 5º passo: Remover colunas inuteis para analise.
Visando facilitar a visualização e analise dos dados, foram removidos as colunas que não possuem utilidade para este trabalho. Neste caso foi somente uma: ID.

	db.drop(labels=["ID"],axis=1,inplace=True)

## 6º passo: HeatMap para averigar o contexto geral.
Antes de continuar para o tratamento dos dados caso houver a necessidade para tal e com a coluna ID removida, chegou-se a conclusão que seria viável uma analise utilizando HeatMap dos dados crús buscando algum insight inicial de para onde a analise poderia estar rumando.

	corr = db.corr()
	plt.figure(figsize=(10, 8))
	sns.heatmap(corr, annot=True, cmap='coolwarm', center=0)
	plt.show()

<p align="center"><b>HeatMap</b> </p>

![heatmap_correlacao](https://github.com/user-attachments/assets/5d65358a-667d-4ea6-ad52-d099495391c6)

O HeatMap apresentou valores inconclusivos, o maior valor 0.68 e o menor -0.30 (Lembrando que o valor do HeatMap maximo é 1 e o minimo é -1, sendo 1 totalmente proporcional e -1 totalmente inversamente proporcional, 0 representa nenhuma relação).

## 7º passo: Tratamento e limpeza de dados para EDA (analise de data exploratória).

Após checkar os dados notou-se que não haviam dados nulos (NaN), entretanto, a maioria dos dados estavam dependentes de legendas para interpretação. Exemplo: Na coluna gênero, 0 representava homem e 1 representava mulher. Visando tornar mais intuitivo a demonstração de dados, substitui-se os dados numéricos quando possivel pelos seus reais significados, assim, grande parte das colunas tornaram-se do tipo String. Além disso, corrigiu-se o tipo de data da coluna numerica "Income" que se tornou float.

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

Após alterar os tipos dos dados, utilizou-se o seguinte comando para confirmar o sucesso da operação:

	print("\n",db.dtypes,"\n")

<p align="center"><b>Output</b> </p>

|      Columns     |     Types     |
|------------------|---------------|
|Sex               | string[python]|
|Marital status    | string[python]|
|Age               |          int64|
|Education         | string[python]|
|Income            |        float64|
|Occupation        | string[python]|
|Settlement size   | string[python]|

dtype: object 

Fora necessario acrescentar manualmente para melhor visualização deste documento a parte superior da tabela: "Columns" e "Types".

## 8º passo: Clustering
<p align="justify">
Com base nas informações retiradas do banco de dados até o momento, decidiu-se começar o processo de clusterização. Para este primeiro em especifico, 
trabalhou-se em cima da relação entre Age e Income (Idade e Renda). Temos então o seguinte código:
</p>
	
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

<p align="center"><b>Output</b> </p>

![AgeXIncome](https://github.com/user-attachments/assets/4a6fc31a-88f7-4954-9a28-543d9ee39510)
