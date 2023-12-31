import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from xgboost import XGBRegressor
import streamlit as st 
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt
import pandas as pd 


df_anoIncTemp = pd.read_csv('data/Anomalies Incertitude Temperature.csv', sep = ';')

st.markdown("# Exploration des données")
st.sidebar.header("Exploration des données")

# Liste des modèles
model_of_interest = ['Decision tree', 'Random forest', 'XGBRegressor', 'Lasso', 'Ridge', 'Linear regression']

# Sélection des modèles à afficher
selected_models = st.multiselect('Sélectionnez un des modèles :', model_of_interest, default=model_of_interest)

selected_date = st.selectbox("Sélectionner la date de début :", [1980, 1950]) 

# Divisez les données en ensembles d'entraînement et de test
train_data = df_anoIncTemp[(df_anoIncTemp['year'] >= selected_date) & (df_anoIncTemp['year'] <= 2010)]
test_data = df_anoIncTemp[(df_anoIncTemp['year'] >= 2011) & (df_anoIncTemp['year'] <= 2021)]

# Séparez les caractéristiques (X) de la cible (y) pour l'entraînement
X_train = np.array(train_data['year']).reshape(-1, 1)
y_train = train_data['anomalie']

# Séparez les caractéristiques (X) de la cible (y) pour le test
X_test = np.array(test_data['year']).reshape(-1, 1)
y_test = test_data['anomalie']

# Modèle de régression linéaire
linear_model = LinearRegression()
linear_model.fit(X_train, y_train)
linear_predictions = linear_model.predict(X_test)

# Modèle Ridge
ridge_model = Ridge(alpha=1.0)
ridge_model.fit(X_train, y_train)
ridge_predictions = ridge_model.predict(X_test)

# Modèle Lasso
lasso_model = Lasso(alpha=1.0)
lasso_model.fit(X_train, y_train)
lasso_predictions = lasso_model.predict(X_test)

# Modèle Decision Tree Regressor
dt_model = DecisionTreeRegressor()
dt_model.fit(X_train, y_train)
dt_predictions = dt_model.predict(X_test)

# Modèle Random Forest Regressor
rf_model = RandomForestRegressor(n_estimators=100)
rf_model.fit(X_train, y_train)
rf_predictions = rf_model.predict(X_test)

# Modèle XGBRegressor
xgb_model = XGBRegressor()
xgb_model.fit(X_train, y_train)
xgb_predictions = xgb_model.predict(X_test)

# Prédire les anomalies de température pour les années de test
dt_predictions = dt_model.predict(X_test)
rf_predictions = rf_model.predict(X_test)
xgb_predictions = xgb_model.predict(X_test)


fig, ax = plt.subplots(figsize=(20, 12))  # Ajuster la taille du graphique
ax.scatter(train_data['year'], train_data['anomalie'], color='blue', label='Données d\'entraînement')
ax.scatter(test_data['year'], test_data['anomalie'], color='red', label='Données de test')
for model in selected_models:
    if model == "Decision tree":
        predictions = dt_predictions
    elif model == 'Random forest':
        predictions = rf_predictions
    elif model == 'XGBRegressor':
        predictions = xgb_predictions
    elif model == "Linear regression":
        predictions = linear_predictions
    elif model == "Ridge":
        predictions = ridge_predictions
    elif model == "Lasso":
        predictions = lasso_predictions

    ax.plot(test_data['year'], predictions, label='Prédictions Decision Tree Regressor')
    plt.title('Decision Tree Regressor pour les anomalies de température (1980-2021)')

ax.set_xlabel('Année')
ax.set_ylabel('Anomalie de température')
ax.legend()
ax.grid(True)
st.pyplot(fig)


dt_mse = mean_squared_error(y_test, dt_predictions)
rf_mse = mean_squared_error(y_test, rf_predictions)
xgb_mse = mean_squared_error(y_test, xgb_predictions)

st.write("## Erreurs quadratiques des modèles")
st.text(f"Decision Tree Regressor : {dt_mse}")
st.text(f"Random Forest Regressor : {rf_mse}")
st.text(f"XGBRegressor : {xgb_mse}")


# Données d'entraînement
plt.scatter(train_data['year'], train_data['anomalie'], color='blue', label='Données d\'entraînement')

# Données de test
plt.scatter(test_data['year'], test_data['anomalie'], color='red', label='Données de test')

# Prédictions Régression Linéaire
plt.plot(test_data['year'], linear_predictions, color='green', label='Prédictions Régression Linéaire')

# Prédictions Ridge
plt.plot(test_data['year'], ridge_predictions, color='purple', label='Prédictions Ridge')

# Prédictions Lasso
plt.plot(test_data['year'], lasso_predictions, color='orange', label='Prédictions Lasso')

# Prédictions Decision Tree Regressor
plt.plot(test_data['year'], dt_predictions, color='brown', label='Prédictions Decision Tree Regressor')

# Prédictions Random Forest Regressor
plt.plot(test_data['year'], rf_predictions, color='pink', label='Prédictions Random Forest Regressor')

# Prédictions XGBRegressor
plt.plot(test_data['year'], xgb_predictions, color='cyan', label='Prédictions XGBRegressor')

plt.title('Comparaison des modèles de régression pour les anomalies de température (1950-2021)')
plt.xlabel('Année')
plt.ylabel('Anomalie de température')
plt.legend()
plt.grid(True)
plt.show()