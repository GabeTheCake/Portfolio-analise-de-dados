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

## Primeiro passo: Definir perguntas que irão definir os processos que serão realizados e definir os processos com base nas perguntas.

Perguntas feitas: 

	Quais as colunas mais e menos relevantes;
	Quais as informações que mais interagem entre sí;
	O que pode-se saber dos consumidores alvo.

## Segundo passo: Definir e Importar bibliotecas que serão utilizadas.

Para a leitura e manejo dos bancos de dados será utilizada a biblioteca PANDAS. 
Para a plotagem, a transformação dos dados em gráficos e visuais, sera utilizado Matplotlib.pyplot. 
Para tambem auxiliar com gráficos e artigos visuais será importado o Seaborn.

	import pandas as pd
	import matplotlib.pyplot as plt
	from matplotlib.colors import ListedColormap
	import seaborn as sns

## Terceiro passo: Carregar bancos de dados (bd) ou database (db) em inglês.
No código chamaremos a base de dados, database, de db. 

	db = pd.read_csv("C:/Users/conta/Portfolio/Projetos/Projeto 1/Dados/segmentation data.csv")

## Quarto passo: Explorar banco de dados.
Com alguns comandos básicos analisou-se a estrutura do banco de dados, as colunas, tipo de dados armazenados nas colunas, o tamanho do mesmo, quantidade de linhas e colunas que ele possuia, quantidade de dados únicos e quantidade de dados nulos ou faltantes bem como linhas em branco.

	print("Head\n", db.head(), "\n")
	print("Info\n", db.info(), "\n")
	print("Describe\n", db.describe(), "\n")
	print("Nunique\n", db.nunique(), "\n")

<p align="center"><b>Output:</b> </p>
<b> head() </b>

|  |         ID | Sex | Marital status | ...| Income | Occupation | Settlement size|
|--|------------|-----|----------------|----|--------|------------|----------------|
|0 | 100000001  |  0  |             0  |... | 124670 |          1 |               2|
|1 | 100000002  |  1  |             1  |... | 150773 |          1 |               2|
|2 | 100000003  |  0  |             0  |... |  89210 |          0 |               0|
|3 | 100000004  |  0  |             0  |... | 171565 |          1 |               1|
|4 | 100000005  |  0  |             0  |... | 149031 |          1 |               1|

[5 rows x 8 columns] 

<b> info() </b>

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

<b> describe() </b>

|      |         ID   |     Sex     | ... |  Occupation   | Settlement size|
|------|--------------|-------------|-----|---------------|--------------|		  
|count | 2.000000e+03 | 2000.000000 | ... | 2000.000000   |   2000.000000|
|mean  | 1.000010e+08 |    0.457000 | ... |    0.810500   |      0.739000|
|std   | 5.774946e+02 |    0.498272 | ... |    0.638587   |      0.812533|
|min   | 1.000000e+08 |    0.000000 | ... |    0.000000   |      0.000000|
|25%   | 1.000005e+08 |    0.000000 | ... |    0.000000   |      0.000000|
|50%   | 1.000010e+08 |    0.000000 | ... |    1.000000   |      1.000000|
|75%   | 1.000015e+08 |    1.000000 | ... |    1.000000   |      1.000000|
|max   | 1.000020e+08 |    1.000000 | ... |    2.000000   |      2.000000|

<b> nunique() </b>

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
|dtype:           | int64|

Neste ultimo comando, fora necessario acrescentar manualmente para melhor visualização deste documento a parte superior da tabela: "Columns" e "Unique Values".

## Quinto passo: Remover colunas inuteis para analise.
Visando facilita a visualização e analise dos dados, foram removidos as colunas que não possuiriam utilidade. Neste caso foi somente uma: ID.

	db.drop(labels=["ID"],axis=1,inplace=True)

## Sexto passo: HeatMap para averigar o contexto geral.
Antes de continuar para o tratamento dos dados caos houver a necessidade para tal e com a coluna ID removida, chegou-se a conclusão que seria viável uma analise utilizando HeatMap dos dados crús buscando algum insight inicial de para onde a analise poderia estar rumando.

	corr = db.corr()
	plt.figure(figsize=(10, 8))
	sns.heatmap(corr, annot=True, cmap='coolwarm', center=0)
	plt.show()

<p align="center"><b>HeatMap</b> </p>

![heatmap_correlacao](https://github.com/user-attachments/assets/5d65358a-667d-4ea6-ad52-d099495391c6)

O HeatMap apresentou valores inconclusivos, o maior valor 0.68 e o menor -0.30(Lembrando que o maximo é 1 e o minimo é -1, sendo 1 totalmente proporcional e -1 totalmente inversamente proporcional, 0 seria nenhum relação).

## Sétimo passo: Começar o processo de tratamento e limpeza de dados se houver necessidade para EDA(analise de data exploratória).

Após checkar os dados notou-se que não haviam dados nulos (NaN), entretanto, a maioria dos dados estavam dependentes de legendas para interpretação. Exemplo: Na coluna gênero, 0 representava homem e 1 representava mulher. Visando tornar mais intuitivo a demonstração de dados, substitui-se os dados numéricos quando possivel pelos seus reais significados. Além disso, corrigiu-se o tipo de data de duas colunas numericas: Age e Income.

	db['Sex'] = db['Sex'].map({0:'Male', 1:'Female'})
	db['Sex'] = db['Sex'].astype('string')

	db['Marital status'] = db['Marital status'].map({0:'Single', 1:'Non-single'})
	db['Marital status'] = db['Marital status'].astype('string')

	db['Education'] = db['Education'].map({0:'Other/Unknown', 1:'High school', 2:'University', 3:'Graduate school'})
	db['Education'] = db['Education'].astype('string')

	db['Occupation'] = db['Occupation'].map({0:'Unemployed/Unskilled', 1:'Skilled employee/Official', 2:'Management/Self-employed/Highly qualified 			employee/Officer'})
	db['Occupation'] = db['Occupation'].astype('string')

	db['Settlement size'] = db['Settlement size'].map({0:'Small city', 1:'Mid-sized city', 2:'Big city'})
	db['Settlement size'] = db['Settlement size'].astype('string')

	db['Age'] = db['Age'].astype(int)
	db['Income'] = db['Income'].astype(float)


## Sexto passo: Começar o processo de EDA, verificar relações entre colunas, quais colunas são necessárias e quais podem deixar a tabela.

## Sétimo passo: Remover colunas desnecessárias.

## Oitavo passo: Com as colunas relevantes na tabela e a ciência de quais as relações são importantes e interessantes a serem trabalhadas, começar a plotar os gráficos coerentes para o cenário.

