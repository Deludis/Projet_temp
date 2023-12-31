
import streamlit as st 
import pandas as pd 
import matplotlib.pyplot as plt

st.markdown("# Visualisation des données")
st.sidebar.header("Visualisation des données")


pages = ["Évolution des températures par continent", "Évolution de la population mondiale", "Évolution des anomalies", "Évolution des températures avec incertiture"]
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
    st.write("### Évolution de la population mondiale")
    df_co2 = pd.read_csv('data/CO2 Donnees.csv', sep = ',')
       
    
    # Liste des courbes
    graphics_of_interest = ["PIB", "Température", "Température avec moyenne mobile à 5 ans", "Somme du CO2"]

    selected_graphic = st.selectbox("Sélectionnez le type du graphique", graphics_of_interest)
    
    
    fig, ax1 = plt.subplots(figsize=(25, 12))  # Ajuster la taille du graphique
    # Filtrer les données pour obtenir seulement celles où le pays est "World" et la période est de 1850 à 2021
    world_population_data = df_co2[(df_co2['country'] == 'World') & (df_co2['year'] >= 1850) & (df_co2['year'] <= 2021)]
    ax1.plot(world_population_data['year'], world_population_data['population'], label='Population mondiale', color='blue')
    ax2 = ax1.twinx()   

    if selected_graphic == "PIB":
        ax2.plot()
        ax2.set_title('Évolution Population Mondiale (1850-2021)', fontsize=40)  # Ajuster la taille de la police
        ax2.set_ylabel("", fontsize=32)
    elif selected_graphic == "Température":
        df_anoIncTemp = pd.read_csv('data/Anomalies Incertitude Temperature.csv', sep=';')

        # Ajoutez la constante de 14.185 à la colonne "anomalie"
        df_anoIncTemp['anomalie'] = df_anoIncTemp['anomalie'] + 14.185
        ax2.plot(df_anoIncTemp['year'], df_anoIncTemp['anomalie'], label='Évolution des températures', color='red')
        ax2.set_title('Évolution de la population mondiale et des températures (1850-2021)', fontsize=40)  # Ajuster la taille de la police
        ax2.set_ylabel('Anomalie de température', color='red', fontsize=32)
        ax2.tick_params(axis='y', labelcolor='red')
    elif selected_graphic == "Température avec moyenne mobile à 5 ans":
        ax2.plot()
        ax2.set_title('Évolution Population Mondiale (1850-2021)', fontsize=40)  # Ajuster la taille de la police
        ax2.set_ylabel("", fontsize=32)
    elif selected_graphic == "Somme du CO2":
        ax2.plot()
        ax2.set_title('Évolution Population Mondiale (1850-2021)', fontsize=40)  # Ajuster la taille de la police
        ax2.set_ylabel("", fontsize=32)
    # Tracer la courbe

    ax1.set_xlabel('Année', fontsize=32)  # Ajuster la taille de la police
    ax1.set_ylabel('Population mondiale', color='blue', fontsize=32)  # Ajuster la taille de la police
    ax1.grid(True)
    ax1.legend(loc='upper left', fontsize=28) # Ajuster la taille de la police
    ax2.legend(loc='upper right', fontsize=28)
    
    # Afficher le graphique dans Streamlit
    st.pyplot(fig)
       
    
elif page == pages[2]:
    st.write("### Évolution des anomalies")
else:
    st.write("### Évolution des températures avec incertiture")
    
    
    
    


