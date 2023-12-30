
import streamlit as st 
import pandas as pd 
import matplotlib.pyplot as plt

st.markdown("# Visualisation des données")
st.sidebar.header("Visualisation des données")


pages = ["Évolution des températures par continent", "Évolution des températures par hémisphère", "Évolution des anomalies", "Évolution des températures avec incertiture"]
page = st.sidebar.radio("Aller vers la page :", pages)

if page == pages[0]:

    df_co2 = pd.read_csv('data/CO2 Donnees.csv', sep = ',')

    st.write("### Évolution des températures par continent")
    
    # Charger les données
    # Assurez-vous que df_co2 est chargé à partir de votre script d'origine


    # Liste des continents
    regions_of_interest = ['Africa', 'Asia', 'Europe', 'North America', 'South America', 'Oceania']

    # Sélection des continents à afficher
    selected_regions = st.multiselect('Sélectionnez les continents :', regions_of_interest, default=regions_of_interest)

    # Filtrer les données en fonction des continents sélectionnés
    df_selected_regions = df_co2[(df_co2['country'].isin(selected_regions)) & (df_co2['year'] >= 1850) & (df_co2['year'] <= 2021)].copy()

    # Supprimer les lignes contenant des valeurs NaN dans les colonnes spécifiées
    columns_to_clean = ['temperature_change_from_ch4', 'temperature_change_from_co2', 'temperature_change_from_ghg', 'temperature_change_from_n2o']
    df_selected_regions = df_selected_regions.dropna(subset=columns_to_clean)

    # Ajouter la constante de 14.185 aux colonnes spécifiées
    df_selected_regions['total_temperature_change'] = df_selected_regions[columns_to_clean].sum(axis=1) + 14.185

    # Créer un graphique Matplotlib
    fig, ax = plt.subplots(figsize=(25, 12))  # Ajuster la taille du graphique
    for region in selected_regions:
        df_plot = df_selected_regions[df_selected_regions['country'] == region]
        ax.plot(df_plot['year'], df_plot['total_temperature_change'], label=region)

    ax.set_title('Évolution du changement de température pour différents continents (1850-2021)', fontsize=40)  # Ajuster la taille de la police
    ax.set_xlabel('Année', fontsize=32)  # Ajuster la taille de la police
    ax.set_ylabel('Changement de température total', fontsize=32)  # Ajuster la taille de la police
    ax.legend(fontsize=28)  # Ajuster la taille de la police
    ax.grid(True)

    # Afficher le graphique dans Streamlit
    st.pyplot(fig)
elif page == pages[1]:
    st.write("### Évolution des températures par hémisphère")
elif page == pages[2]:
    st.write("### Évolution des anomalies")
else:
    st.write("### Évolution des températures avec incertiture")





