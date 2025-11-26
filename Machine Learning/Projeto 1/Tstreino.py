import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, BatchNormalization
from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import matplotlib.pyplot as plt

# 1. Carregar dados
data = pd.read_csv("C:/Users/User/Desktop/Cds/Programas para Project/TreinoTS/data.csv")

# 2. Separar features e labels
features = data.drop(columns=["ID", "Age"])
labels = data["Age"]

# 3. Pré-processamento (categorias e numéricos)
categorical_features = ["Sex", "Marital status", "Education", "Occupation", "Settlement size"]
numerical_features = ["Income"]

# 4. Pipeline de pré-processamento
preprocessor = ColumnTransformer([
    ("num", StandardScaler(), numerical_features),
    ("cat", OneHotEncoder(drop='first'), categorical_features)
])

# 5. Aplicar pré-processamento
X_processed = preprocessor.fit_transform(features)
y = labels.values

# 6. Dividir treino/teste
X_train, X_test, y_train, y_test = train_test_split(X_processed, y, test_size=0.2, random_state=42)

# 7. Criar modelo Deep Learning
model = Sequential([
    Dense(64, activation='relu', input_shape=(X_train.shape[1],)),
    BatchNormalization(),
    Dropout(0.3),
    Dense(32, activation='relu'),
    BatchNormalization(),
    Dropout(0.2),
    Dense(1)
])

# 8. Compilar modelo
model.compile(optimizer='adam', loss='mean_squared_error', metrics=['mae'])

# 8.1. Definir o earlystop
early_stop = EarlyStopping(monitor='val_loss', patience=10, restore_best_weights=True)

# 8.2. Salvar melhor modelo
checkpoint = ModelCheckpoint(
    'melhor_modelo.keras',
    monitor='val_loss',
    save_best_only=True
)

# 9. Treinar modelo
history = model.fit(X_train, y_train, epochs=200, batch_size=32, validation_split=0.2, callbacks=[early_stop, checkpoint], verbose=1)

# 9.1. Ver treinamento do modelo
plt.plot(history.history['loss'], label='Treino')
plt.plot(history.history['val_loss'], label='Validação')
plt.title('Loss durante o treino')
plt.xlabel('Épocas')
plt.ylabel('Loss')
plt.legend()
plt.grid(True)
plt.show()

# 10. Avaliar no teste
y_pred = model.predict(X_test).flatten()

mae = mean_absolute_error(y_test, y_pred)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
r2 = r2_score(y_test, y_pred)

print(f"Erro médio absoluto (MAE): {mae:.2f}")
print(f"Raiz do erro quadrático médio (RMSE): {rmse:.2f}")
print(f"Coeficiente de determinação (R²): {r2:.4f}")

# 11. Gráfico: Real vs Predito
plt.figure(figsize=(8, 8))
plt.scatter(y_test, y_pred, alpha=0.3, color='blue')
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--')
plt.xlabel('Valores Reais')
plt.ylabel('Valores Preditos')
plt.title('Predito vs Real (Rede Neural)')
plt.grid(True)
plt.tight_layout()
plt.show()