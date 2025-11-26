import pandas as pd
import numpy as np
import tensorflow
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler
from sklearn.dummy import DummyRegressor
from sklearn.metrics import mean_absolute_error
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import InputLayer
from tensorflow.keras.layers import Dense, Dropout
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.callbacks import EarlyStopping
import matplotlib.pyplot as plt

def modelo(features):
    # Starting the model
    model = Sequential(name = "modelo_1")
    # Making the first layer, the input layer
    input = InputLayer(input_shape = (features.shape[1],))
    model.add(input)
    model.add(Dense(128, activation='relu'))
    model.add(Dropout(0.2))
    model.add(Dense(64, activation = 'relu'))
    model.add(Dense(1))

    opt = Adam(learning_rate=0.001)
    model.compile(loss='mse', metrics= ['mae'], optimizer=opt)

    return model

# Load Data and split it
data = pd.read_csv("C:/Users/User/Desktop/Cds/Programas para Project/TreinoTS/data2.csv")
features = data[["duration" , "bitrate", "bitrate(video)", "height", "width", "frame rate", "frame rate(est.)", "codec", "category", "views", "comments"]]
labels = data["likes"]

# Process it
features = pd.get_dummies(features)
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size=0.2, random_state=42) 

# Make it standard
numerical_features = features.select_dtypes(include=['int64', 'float64'])
numerical_columns = numerical_features.columns
ct = ColumnTransformer([('standardize', StandardScaler(), numerical_columns)], remainder='passthrough')
features_train = ct.fit_transform(features_train)
features_test = ct.transform(features_test)

model = modelo(features_train) 
print(model.summary())

# Early stopping callback
es = EarlyStopping(monitor='val_loss', mode='min', verbose=1, patience=15)

# fit the model using 40 epochs and batch size 1
history = model.fit(features_train, labels_train, epochs=200, batch_size=32, verbose=1, validation_split=0.2, callbacks=[es])

# evaluate the model on the test set
val_mse, val_mae = model.evaluate(features_test, labels_test, verbose=0)
print("MAE: ", val_mae)
print("MSE: ", val_mse) 

plt.plot(history.history['loss'], label='Treinamento')
plt.plot(history.history['val_loss'], label='Validação')
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.legend()
plt.title('Curva de Aprendizado')
plt.show()

# Avaliação com Dummy Regressor como baseline
dummy_rgres = DummyRegressor(strategy="mean")
dummy_rgres.fit(features_train, labels_train)
featurePred = dummy_rgres.predict(features_test)
mae = mean_absolute_error(labels_test, featurePred)
print(f"\nMAE Dummy Regressor: {mae:.0f}")