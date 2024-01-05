
import pandas as pd 
import numpy as np
from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from xgboost import XGBRegressor
import joblib


df_anoIncTemp = pd.read_csv('data/Anomalies Incertitude Temperature.csv', sep = ';')


for year in [1950, 1980]:
    # Divisez les données en ensembles d'entraînement et de test
    train_data = df_anoIncTemp[(df_anoIncTemp['year'] >= year) & (df_anoIncTemp['year'] <= 2010)]
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
    joblib.dump(linear_model, f"models/linear_regression_{year}")

    # Modèle Ridge
    ridge_model = Ridge(alpha=1.0)
    ridge_model.fit(X_train, y_train)
    joblib.dump(ridge_model, f"models/ridge_{year}")

    # Modèle Lasso
    lasso_model = Lasso(alpha=1.0)
    lasso_model.fit(X_train, y_train)
    joblib.dump(lasso_model, f"models/lasso_{year}")

    # Modèle Decision Tree Regressor
    dt_model = DecisionTreeRegressor()
    dt_model.fit(X_train, y_train)
    joblib.dump(dt_model, f"models/TreeRegressor_{year}")

    # Modèle Random Forest Regressor
    rf_model = RandomForestRegressor(n_estimators=100)
    rf_model.fit(X_train, y_train)
    joblib.dump(rf_model, f"models/random_forest_{year}")

    # Modèle XGBRegressor
    xgb_model = XGBRegressor()
    xgb_model.fit(X_train, y_train)
    joblib.dump(xgb_model, f"models/XGBRegressor_{year}")


from fbprophet import Prophet
df_global = pd.read_csv('data/Temperature Index Global 100.csv', sep=',')

# Renommer les colonnes
df_global = df_global.rename(columns={'Year': 'ds', 'J-D': 'y'})

# Appliquer un format de date au 1er janvier de chaque année dans la colonne "ds"
df_global['y'] = pd.to_numeric(df_global['y'], errors='coerce')
df_global['ds'] = pd.to_datetime(df_global['ds'].astype(str) + '-01-01')

df_prophet = df_global[["ds", "y"]]

prohet_model = Prophet()
prohet_model.fit(df_prophet)
joblib.dump(prohet_model, "models/prophet")
future = prohet_model.make_future_dataframe(periods=10592)
prohet_predictions = prohet_model.predict(future)
joblib.dump(prohet_predictions, "predictions/prophet_2050")
future = prohet_model.make_future_dataframe(periods=18992)
prohet_predictions = prohet_model.predict(future)
joblib.dump(prohet_predictions, "predictions/prophet_2073")
future = prohet_model.make_future_dataframe(periods=28854)
prohet_predictions = prohet_model.predict(future)
joblib.dump(prohet_predictions, "predictions/prophet_2100")