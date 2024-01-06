import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import streamlit as st 
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt
import pandas as pd 
import joblib

st.set_page_config(
    page_title="Projet Température",
    page_icon="👋",
    layout="wide",
)

st.markdown("# Exploration des données")
st.sidebar.header("Exploration des données")
footer="""<style>
a:link , a:visited{
color: blue;
background-color: transparent;
text-decoration: underline;
}

a:hover,  a:active {
color: red;
background-color: transparent;
text-decoration: underline;
}

.footer {
position: fixed;
left: 0;
bottom: 0;
width: 100%;
background-color: white;
color: black;
text-align: center;
}
</style>
<div class="footer">
<p>Developed with ❤ by Yves Roig</p>
</div>
"""
st.markdown(footer,unsafe_allow_html=True)

pages = ["Entrainement", "Spearman et Pearson", "Prédiction"]
page = st.sidebar.radio("Aller vers la page :", pages)

df_anoIncTemp = pd.read_csv('data/Anomalies Incertitude Temperature.csv', sep = ';')

if page == pages[0]:
    # Liste des modèles
    model_of_interest = ['Decision tree', 'Random forest', 'XGBRegressor', 'Lasso', 'Ridge', 'Linear regression']

    select1, select2 = st.columns(2)
    with select1:
        # Sélection des modèles à afficher
        selected_models = st.multiselect('Sélectionnez un des modèles :', model_of_interest, default='Linear regression')
    with select2:
        selected_date = st.selectbox("Sélectionner la date de début :", [1950, 1980]) 

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
    linear_model = joblib.load(f"models/linear_regression_{selected_date}")
    linear_predictions = linear_model.predict(X_test)

    # Modèle Ridge
    ridge_model = joblib.load(f"models/ridge_{selected_date}")
    ridge_predictions = ridge_model.predict(X_test)

    lasso_model = joblib.load(f"models/lasso_{selected_date}")
    lasso_predictions = lasso_model.predict(X_test)

    # Modèle Decision Tree Regressor
    dt_model = joblib.load(f"models/TreeRegressor_{selected_date}")
    dt_predictions = dt_model.predict(X_test)

    # Modèle Random Forest Regressor
    rf_model = joblib.load(f"models/random_forest_{selected_date}")
    rf_predictions = rf_model.predict(X_test)

    # Modèle XGBRegressor
    xgb_model = joblib.load(f"models/XGBRegressor_{selected_date}")
    xgb_predictions = xgb_model.predict(X_test)

    col1, col2 = st.columns([2,1])

    fig, ax = plt.subplots(figsize=(20, 12))  # Ajuster la taille du graphique
    ax.scatter(train_data['year'], train_data['anomalie'], color='blue', label='Données d\'entraînement')
    ax.scatter(test_data['year'], test_data['anomalie'], color='red', label='Données de test')
    erreurs_quadratiques = {}
    for model in selected_models:
        if model == "Decision tree":
            predictions = dt_predictions
            label="Prédictions Decision Tree"
            dt_mse = mean_squared_error(y_test, dt_predictions)
            erreurs_quadratiques["Decision Tree :"] = dt_mse
        elif model == 'Random forest':
            predictions = rf_predictions
            label="Prédictions Random forest"
            rf_mse = mean_squared_error(y_test, rf_predictions)
            erreurs_quadratiques["Random Forest :"] = rf_mse
        elif model == 'XGBRegressor':
            predictions = xgb_predictions
            label="Prédictions XGBRegressor"
            xgb_mse = mean_squared_error(y_test, xgb_predictions)
            erreurs_quadratiques["XGBRegressor :"] = xgb_mse
        elif model == "Linear regression":
            predictions = linear_predictions
            label="Prédictions Linear regression"
            # Évaluer les performances du modèle sur les données de test
            linear_mse = mean_squared_error(test_data['anomalie'], linear_predictions)
            erreurs_quadratiques["Régression Linéaire :"] = linear_mse
        elif model == "Ridge":
            predictions = ridge_predictions
            label="Prédictions Ridge"
            ridge_mse = mean_squared_error(test_data['anomalie'], ridge_predictions)
            erreurs_quadratiques["Ridge :"] = ridge_mse
        elif model == "Lasso":
            predictions = lasso_predictions
            label="Prédictions Lasso"
            lasso_mse = mean_squared_error(test_data['anomalie'], lasso_predictions)
            erreurs_quadratiques["Lasso :"] = lasso_mse

        ax.plot(test_data['year'], predictions, label=label)
        plt.title('Prédictions pour les anomalies de température')

    with col1:
        ax.set_xlabel('Année')
        ax.set_ylabel('Anomalie de température')
        ax.legend()
        ax.grid(True)
        st.pyplot(fig)

    with col2:
        st.write("## Erreurs quadratiques des modèles")
        colName, colResult = st.columns([2, 7])
        for erreurs_quadratique in erreurs_quadratiques.keys():
            with colName:
                st.write(erreurs_quadratique)
            with colResult:
                st.write(erreurs_quadratiques[erreurs_quadratique])

elif page == pages[1]:
    from scipy.stats import spearmanr
    from sklearn.linear_model import LinearRegression
    from scipy.stats import pearsonr

    df_co2 = pd.read_csv('data/CO2 Donnees.csv', sep=',')
    df_filtered = df_co2[(df_co2['iso_code'].notna()) & (df_co2['year'] >= 1850) & (df_co2['year'] <= 2018)]
    # Groupby par année et sum pour obtenir la somme de co2_including_luc et de la population pour chaque année
    df_sum_co2_population = df_filtered.groupby('year')[['co2_including_luc', 'population']].sum().reset_index()

    df_filtered = df_co2[(df_co2['iso_code'].notna()) & (df_co2['year'] >= 1850) & (df_co2['year'] <= 2021)]
    df_sum_co2 = df_filtered.groupby('year')['co2_including_luc'].sum().reset_index()

    # Supposons que df_sum_co2 contienne les données de la somme du CO2 et df_anoIncTemp contienne les données de l'anomalie de température
    # Assurez-vous que ces DataFrames sont correctement définis avec les colonnes 'year' et les valeurs correspondantes.

    # Fusionner les deux DataFrames sur la colonne 'year'
    df_merged = pd.merge(df_sum_co2, df_anoIncTemp, on='year', how='inner')

    # Calculer la corrélation de Spearman
    correlation_coefficient, p_value = spearmanr(df_merged['co2_including_luc'], df_merged['anomalie'])

    # Afficher les résultats
    st.write(f"Corrélation de Spearman : {correlation_coefficient}")
    st.write(f"P-value : {p_value}")
    # Interprétation du résultat
    if p_value < 0.05:
        st.write("La corrélation est statistiquement significative.")
    else:
        st.write("La corrélation n'est pas statistiquement significative.")

    # Supposons que df_sum_co2 contienne les données de la somme du CO2 et df_anoIncTemp contienne les données de l'anomalie de température
    # Assurez-vous que ces DataFrames sont correctement définis avec les colonnes 'year' et les valeurs correspondantes.

    # Fusionner les deux DataFrames sur la colonne 'year'
    df_merged = pd.merge(df_sum_co2, df_anoIncTemp, on='year', how='inner')

    # Séparer les caractéristiques (X) de la cible (y)
    X = df_merged[['co2_including_luc']]
    y = df_merged['anomalie']

    # Créer et entraîner le modèle de régression linéaire
    linear_model = LinearRegression()
    linear_model.fit(X, y)

    # Calculer la corrélation de Spearman entre les prédictions du modèle et la cible
    predictions = linear_model.predict(X)
    correlation_coefficient, p_value = spearmanr(predictions, y)

    # Afficher les résultats
    st.write(f"Corrélation de Spearman avec la régression linéaire : {correlation_coefficient}")
    st.write(f"P-value : {p_value}")

    # Interprétation du résultat
    if p_value < 0.05:
        st.write("La corrélation est statistiquement significative.")
    else:
        st.write("La corrélation n'est pas statistiquement significative.")



    # Sélectionner les données pour la période spécifiée
    df_selected = df_sum_co2_population[(df_sum_co2_population['year'] >= 1850) & (df_sum_co2_population['year'] <= 2018)]

    # Calculer la corrélation de Pearson
    correlation, p_value = pearsonr(df_selected['co2_including_luc'], df_selected['population'])

    # Afficher le résultat
    st.write(f"Corrélation de Pearson : {correlation}")
    st.write(f"Valeur de p : {p_value}")

    # Interprétation du résultat
    if p_value < 0.05:
        st.write("La corrélation est statistiquement significative.")
    else:
        st.write("La corrélation n'est pas statistiquement significative.")

else:

    selected_date = st.selectbox("Sélectionner la date de début :", [2050, 2073, 2100]) 
    prohet_predictions = joblib.load(f'predictions/prophet_{selected_date}')

    colYhat, colTrend = st.columns(2)
    with colYhat:
        fig = plt.figure(figsize=(20, 10))
        plt.plot(prohet_predictions['ds'], prohet_predictions['yhat'], label='yhat')

        if st.checkbox("Prediction Yhat + Incertitude", True) : 
            plt.plot(prohet_predictions['ds'], prohet_predictions['yhat_upper'], label='Prediction + Incertitude', color="darkred")
            plt.fill_between(prohet_predictions['ds'], prohet_predictions['yhat'], prohet_predictions['yhat_upper'], color='pink')

        if st.checkbox("predictions Yhat - Incertitude", True): 
            plt.plot(prohet_predictions['ds'], prohet_predictions['yhat_lower'], label='Prediction - Incertitude', color="darkred")
            plt.fill_between(prohet_predictions['ds'], prohet_predictions['yhat'], prohet_predictions['yhat_lower'], color='pink')

    
        plt.xticks(pd.date_range(start=prohet_predictions["ds"].min(), end=prohet_predictions["ds"].max(), freq='10Y'), pd.date_range(start=prohet_predictions["ds"].min(), end=prohet_predictions["ds"].max(), freq='10Y', inclusive='both').year)
        plt.grid(True)
        st.pyplot(fig)

    with colTrend:
        fig = plt.figure(figsize=(20, 10))
        plt.plot(prohet_predictions['ds'], prohet_predictions['trend'], label='trend')
        
        if st.checkbox("Prediction Trend + Incertitude", True) : 
            plt.plot(prohet_predictions['ds'], prohet_predictions['trend_upper'], label='Prediction + Incertitude', color="darkred")
            plt.fill_between(prohet_predictions['ds'], prohet_predictions['trend'], prohet_predictions['trend_upper'], color='pink')

        if st.checkbox("predictions Trend - Incertitude", True): 
            plt.plot(prohet_predictions['ds'], prohet_predictions['trend_lower'], label='Prediction - Incertitude', color="darkred")
            plt.fill_between(prohet_predictions['ds'], prohet_predictions['trend'], prohet_predictions['trend_lower'], color='pink')

    
        plt.xticks(pd.date_range(start=prohet_predictions["ds"].min(), end=prohet_predictions["ds"].max(), freq='10Y'), pd.date_range(start=prohet_predictions["ds"].min(), end=prohet_predictions["ds"].max(), freq='10Y', inclusive='both').year)
        plt.grid(True)
        st.pyplot(fig)

    
    st.write(prohet_predictions)