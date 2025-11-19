import pandas as pd
import tensorflow as ts
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, classification_report, roc_auc_score, RocCurveDisplay
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

# Carregar os dados
db = pd.read_csv('Dados/churn_data.csv')
db1 = pd.read_csv('Dados/customer_data.csv')
db2 = pd.read_csv('Dados/internet_data.csv')

# Juntar os dados
merged = pd.merge(db1, db, on='customerID')
result = pd.merge(merged, db2, on='customerID')
result['TotalCharges'] = pd.to_numeric(result['TotalCharges'], errors='coerce')
result = result.dropna(subset=['TotalCharges'])  # opção mais segura

# Remover colunas desnecessárias
feature = result.drop(columns=['customerID', 'Churn'])
label = result['Churn'].map({'No': 0, 'Yes': 1})

# Converter categóricas em dummies
X = pd.get_dummies(feature, drop_first=True)
y = label


scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Separar em treino e teste
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# Treinar modelo de classificação
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

# Fazer previsões
y_pred = model.predict(X_test)
y_proba = model.predict_proba(X_test)[:, 1]

# Avaliar o modelo
print("Relatório de Classificação:")
print(classification_report(y_test, y_pred))
print("AUC:", roc_auc_score(y_test, y_proba))

# Matriz de Confusão
conf_mat = confusion_matrix(y_test, y_pred)
print("Matriz de Confusão:")
print(conf_mat)

# Curva ROC
RocCurveDisplay.from_estimator(model, X_test, y_test)
plt.show()

# -------------------------------------------
# Previsão para novo cliente
# -------------------------------------------

# 1. Criar dicionário com os dados do novo cliente
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

# 2. Transformar em DataFrame
new_df = pd.DataFrame([new_customer])

# 3. Aplicar get_dummies e alinhar colunas com o X original
new_df_dummies = pd.get_dummies(new_df, drop_first=True)
new_df_dummies = new_df_dummies.reindex(columns=X.columns, fill_value=0)

# 4. Padronizar os dados (usar mesmo scaler do treino)
new_scaled = scaler.transform(new_df_dummies)

# 5. Fazer previsão
pred_class = model.predict(new_scaled)[0]
pred_proba = model.predict_proba(new_scaled)[0][1]

# 6. Mostrar resultados
print("\n📊 Previsão para novo cliente:")
print("→ Vai sair (churn)?", "✅ Sim" if pred_class == 1 else "❌ Não")
print("→ Probabilidade de churn:", f"{round(pred_proba * 100, 2)}%")