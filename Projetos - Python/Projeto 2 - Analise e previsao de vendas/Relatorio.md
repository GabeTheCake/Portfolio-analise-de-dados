<h1 align="center">Projeto 2: Previsão de Churn de Clientes em uma Empresa de Telecomunicações</h1> <p align="justify"> Este projeto foi desenvolvido com o objetivo de prever o comportamento de churn (cancelamento de contrato) de clientes de uma empresa de telecomunicações. Utilizando um banco de dados com informações sobre os clientes e seus serviços, o modelo desenvolvido usa regressão logística para prever se um cliente irá ou não abandonar a empresa. Abaixo, detalho o processo realizado para o desenvolvimento desse modelo de predição. </p>

<h2 align="center">Descrição do Banco de Dados</h2>

O banco de dados utilizado é composto por três arquivos CSV que contêm as seguintes informações:

- churn_data: Detalhes sobre o comportamento do cliente, incluindo a variável "Churn" (se o cliente cancelou ou não).
- customer_data: Informações demográficas dos clientes, como idade, gênero, estado civil, etc.
- internet_data: Dados sobre o tipo de serviço de internet contratado e as características relacionadas.

Com essas informações, nosso objetivo é prever o "Churn", que é uma variável binária (1 para clientes que cancelaram o serviço e 0 para os que permaneceram).

<p align="justify"> Após explorar e preparar os dados, o modelo de Regressão Logística foi utilizado para classificar os clientes em relação à probabilidade de cancelamento. O modelo foi avaliado com métricas como AUC, matriz de confusão e curva ROC. </p>

<h2 align="center">Etapas do Projeto</h2>

<h3>1. Análise Exploratória dos Dados (EDA)</h3>

Primeiramente, a análise exploratória foi realizada para entender as variáveis, verificar a existência de dados ausentes e mapear as correlações entre as variáveis. O gráfico HeatMap foi utilizado para examinar as relações entre as variáveis.

<h3>2. Limpeza e Transformação dos Dados</h3>

O código foi ajustado para remover colunas desnecessárias e para tratar variáveis categóricas, convertendo-as em variáveis numéricas (dummies). Além disso, foi realizada a padronização das variáveis para melhorar o desempenho do modelo de regressão logística.

<h3>3. Treinamento do Modelo</h3>

O modelo de Regressão Logística foi treinado utilizando os dados de treino, com a seguinte estrutura de código:

model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)


Após o treinamento, foram feitas previsões utilizando o conjunto de teste e as métricas de avaliação foram geradas, incluindo o relatório de classificação e a matriz de confusão.

<h3>4. Avaliação do Modelo</h3>

O modelo foi avaliado usando as seguintes métricas:

- AUC (Area Under the Curve): Medida que indica a performance do modelo, variando de 0 a 1, onde valores mais próximos de 1 indicam um modelo melhor.

- Matriz de Confusão: A matriz de confusão foi utilizada para entender melhor o desempenho do modelo em termos de verdadeiros positivos, falsos positivos, etc.

- Curva ROC: A curva ROC foi gerada para analisar o trade-off entre a taxa de verdadeiros positivos e falsos positivos.

<p align="center">
  <img width="640" height="480" alt="grafico" src="https://github.com/user-attachments/assets/2b220e18-aefb-48d0-9a3f-ddd1c1512f44" />
</p>

<h3>5. Previsão para Novo Cliente</h3>

Para realizar previsões sobre um novo cliente, criamos um dicionário com as informações desse cliente e passamos os dados por todo o pipeline de pré-processamento, transformação e previsão. O código para previsão de um novo cliente foi o seguinte:

    new_customer = {
    'gender': 'Female',
    'SeniorCitizen': 0,
    'Partner': 'Yes',
    'Dependents': 'No',
    'tenure': 5,
    'PhoneService': 'Yes',
    'MultipleLines': 'Yes',
    'InternetService': 'Fiber optic',
    'OnlineSecurity': 'No',
    'OnlineBackup': 'Yes',
    'DeviceProtection': 'No',
    'TechSupport': 'No',
    'StreamingTV': 'Yes',
    'StreamingMovies': 'Yes',
    'Contract': 'Month-to-month',
    'PaperlessBilling': 'Yes',
    'PaymentMethod': 'Electronic check',
    'MonthlyCharges': 85.5,
    'TotalCharges': 430.0
    }

Previsão de churn:

    new_df = pd.DataFrame([new_customer])
    new_df_dummies = pd.get_dummies(new_df, drop_first=True)
    new_df_dummies = new_df_dummies.reindex(columns=X.columns, fill_value=0)

    new_scaled = scaler.transform(new_df_dummies)
    pred_class = model.predict(new_scaled)[0]
    pred_proba = model.predict_proba(new_scaled)[0][1]

    print("Previsão para novo cliente:")
    print("→ Vai sair (churn)?", "✅ Sim" if pred_class == 1 else "❌ Não")
    print("→ Probabilidade de churn:", f"{round(pred_proba * 100, 2)}%")


Isso permite prever a probabilidade de churn para um cliente específico com base nas suas características.

<h3>6. Resultados</h3>

O modelo gerado obteve uma boa performance, com AUC significativo e precisão nas previsões. Abaixo estão os resultados obtidos após treinar o modelo:

- AUC: 0.85
- Relatório de Classificação: O modelo apresentou uma boa precisão e recall para prever os clientes que iriam cancelar o serviço.
- Curva ROC: A curva mostrou uma boa separação entre as classes de churn e não-churn.

<p align="center"><b>Exemplo de Previsão para Novo Cliente</b> </p>

    📊 Previsão para novo cliente:
    → Vai sair (churn)? ❌ Não
    → Probabilidade de churn: 19.51%

<h2 align="center">Conclusão</h2>

<p align="justify">Com base nesse modelo, a empresa de telecomunicações pode identificar os clientes com maior probabilidade de cancelar o serviço e tomar ações preventivas, como oferecer descontos ou melhorar os planos de serviços. Este tipo de análise pode ser muito útil para estratégias de retenção de clientes.</p>
