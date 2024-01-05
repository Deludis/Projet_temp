import streamlit as st 
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns 
import plotly.express as px

st.set_page_config(
    page_title="Projet Température",
    page_icon="👋",
    layout="wide",
)

st.markdown("# Visualisation des données")
st.sidebar.header("Visualisation des données")


pages = ["Évolution des températures par continent", "Évolution de la population mondiale", "Évolution des anomalies", "Évolution des températures avec incertitude"]
page = st.sidebar.radio("Aller vers la page :", pages)

if page == pages[0]:

    df_co2 = pd.read_csv('data/CO2 Donnees.csv', sep = ',')

    st.write("### Évolution des températures par continent")
    
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

    ax.set_title('Évolution du changement de température pour différents continents (1850-2021)', fontsize=30)  # Ajuster la taille de la police
    ax.set_xlabel('Année', fontsize=30)  # Ajuster la taille de la police
    ax.set_ylabel('Changement de température total', fontsize=30)  # Ajuster la taille de la police
    ax.legend(fontsize=20)  # Ajuster la taille de la police
    ax.grid(True)
    
    

    # Afficher le graphique dans Streamlit
    st.pyplot(fig)
    
    st.write("Ce graphique indique l'évolution des températures par continents.")
    st.write("Nous remarquons rapidement que l'Europe et l'Amérique du nord ont un démarrage précoce, car dès le début du XXème siècle l'augmentation des températures est enclenchée.")
    st.write("Il est vrai que l'Europe est le berceau de la Révolution Industrielle parfois spontanée comme en Grande-Bretagne, parfois en réaction géopolitique comme en France ou imposée légalement en Allemagne ou en Russie (puis en Union Soviétique) avec le Plan Quinquénal.")
    st.write("Il est intéressant de noter qu'à partir des années 1980-1990, la courbe s'infléchit sans toutefois retomber. La délocalisation des industries polluantes vers la Chine essentiellement en est responsable. Il apparait donc qu'il existe d'autres sources de pollution provoquant une augmentation des températures.")
    st.write("Pour l'Amérique du nord le réel décollage a lieu après la Guerre de Sécession en 1865, décrite comme étant la première guerre industrielle. L'industrialisation des anciens états sudistes essentiellement agricoles sera un ajout conséquent à la puissance indutrielle des USA. ")
    st.write("Pour l'Asie, le Japon comprend rapidement les avantages de l'industrialisation avec les Meijis en 1868, toutefois au niveau du continent la mise en place d'une politique de réindustralisatoin de la Chine avec Mao Zedong est nettement visible en 1950.")
    st.write("Pour les continents Sud-américain et Africain l'émergence en tant que puissances industrielles est beaucoup plus tardive. Toutefois elle a bien démarré au passage du XXIéme siècle.")
    st.write("L'Australasie est un cas intéressant car ce continent est industrialisé et même avancé dans le cas de l'Australie et de la Nouvelle-Zélande et malgré cela sa contribution à l'volution des températures reste minime.")    
    st.write("\n")
    st.write("\n")
    
    tabHemi, tabHemiMoyMob= st.tabs(["## Evolutions des températures dans hémisphère nord et sud", "## Evolutions des températures dans hémisphère nord et sud avec moyenne mobile à 5 ans"])
    
    df_zone = pd.read_csv('data/Temperature Moyenne Index Global 100.csv', sep=',')
    # Filtrer les données pour obtenir seulement celles de 1880 à 2022
    df_zone_filtered = df_zone[(df_zone['Year'] >= 1880) & (df_zone['Year'] <= 2022)]

    # Diviser les valeurs par 100 et ajouter 14.185
    df_zone_filtered['NHem'] = df_zone_filtered['NHem'] / 100 + 14.185
    df_zone_filtered['SHem'] = df_zone_filtered['SHem'] / 100 + 14.185

    with tabHemi: 
        # Tracer les courbes
        fig = plt.figure(figsize=(25, 12))
        plt.plot(df_zone_filtered['Year'], df_zone_filtered['NHem'], label='NHem')
        plt.plot(df_zone_filtered['Year'], df_zone_filtered['SHem'], label='SHem')
        plt.title('Évolution des températures dans l\'hémisphère nord et sud (1880-2022)', fontsize=30)
        plt.axhline(y=14.185, color='red', linestyle='--', linewidth=1)
        plt.xlabel('Année', fontsize=30)
        plt.ylabel('Anomalie de température', fontsize=30)
        plt.legend(fontsize=20)
        plt.grid(True)
        st.pyplot(fig)
    with tabHemiMoyMob: 
        # Tracer les courbes
        fig = plt.figure(figsize=(25, 12))
        # Ajoutez une colonne pour la moyenne mobile sur 5 ans
        df_zone_filtered['NHem_moyenne_mobile_5ans'] = df_zone_filtered['NHem'].rolling(window=5).mean()
        df_zone_filtered['SHem_moyenne_mobile_5ans'] = df_zone_filtered['SHem'].rolling(window=5).mean()
        plt.plot(df_zone_filtered['Year'], df_zone_filtered['NHem_moyenne_mobile_5ans'], label='NHem - Moyenne mobile 5 ans')
        plt.plot(df_zone_filtered['Year'], df_zone_filtered['SHem_moyenne_mobile_5ans'], label='SHem - Moyenne mobile 5 ans')
        plt.title('Évolution des températures avec moyennes mobiles à 5 ans (1880-2022)', fontsize=30)
        plt.axhline(y=14.185, color='red', linestyle='--', linewidth=1)
        plt.xlabel('Année', fontsize=30)
        plt.ylabel('Anomalie de température', fontsize=30)
        plt.legend(fontsize=20)
        plt.grid(True)
        st.pyplot(fig)
        
    st.image("images/carte-du-monde-continents.jpg")  
    st.write("carte-du-monde.net")
    st.write("## L'hémisphère Nord :")
    st.write("Environ 100 millions de kilomètres carrés de terres émergées sont situés dans cet hémisphère, soit les deux tiers du total mondial.")
    st.write("Comme l'hémisphère nord a une surface de 255 millions de kilomètres carrés, il est couvert de terres émergées à hauteur de 40 %.")
    st.write("Il est à remarquer que la plus grande partie de l'humanité (près de 90 % de la population totale) vit dans cet hémisphère,")
    st.write("ce qui n'est guère surprenant étant donné que l'Asie, qui compte à elle seule environ 60 % de la population mondiale, est presque entièrement située dans l'hémisphère nord. ")
    
    st.write("## L'hémisphère Sud :")
    st.write("L'hémisphère sud terrestre est essentiellement marin. Les terres émergées (50 millions de kilomètres carrés) ne représentent que 20 % de sa surface et le tiers des terres émergées terrestres.")
    st.write("Entre 50 et 65 degrés de latitude sud, il n'y a quasiment pas de terre émergée, ce qui n'est pas le cas de l'hémisphère nord.")
    st.write("L'Antarctique est le seul continent sans population indigène. ")
    
    st.write("### La population est peut-être aussi un facteur contribuant à l'évolution des températures ?")

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
        # Filtrer les données pour obtenir seulement celles où la colonne "iso_code" est renseignée et la période est de 1850 à 2018
        df_filtered = df_co2[(df_co2['iso_code'].notna()) & (df_co2['year'] >= 1850) & (df_co2['year'] <= 2018)]

        # Groupby par année et sum pour obtenir la somme du PIB (gdp) pour chaque année
        df_sum_gdp = df_filtered.groupby('year')['gdp'].sum().reset_index()

        ax2.plot(df_sum_gdp['year'], df_sum_gdp['gdp'], label='Somme du PIB mondial', color='black')
        ax2.set_title('Évolution Population Mondiale (1850-2021)', fontsize=30)  # Ajuster la taille de la police
        ax2.set_ylabel('Somme du PIB mondial', color='black', fontsize=30)
        ax2.tick_params(axis='y', labelcolor='black')
    elif selected_graphic == "Température":
        df_anoIncTemp = pd.read_csv('data/Anomalies Incertitude Temperature.csv', sep=';')
        # Ajoutez la constante de 14.185 à la colonne "anomalie"
        df_anoIncTemp['anomalie'] = df_anoIncTemp['anomalie'] + 14.185

        ax2.plot(df_anoIncTemp['year'], df_anoIncTemp['anomalie'], label='Évolution des températures', color='red')
        ax2.set_title('Évolution de la population mondiale et des températures (1850-2021)', fontsize=40)  # Ajuster la taille de la police
        ax2.set_ylabel('Anomalie de température', color='red', fontsize=30)
        ax2.tick_params(axis='y', labelcolor='red')
    elif selected_graphic == "Température avec moyenne mobile à 5 ans":
        df_anoIncTemp = pd.read_csv('data/Anomalies Incertitude Temperature.csv', sep=';')
        # Ajoutez la constante de 14.185 à la colonne "anomalie"
        df_anoIncTemp['anomalie'] = df_anoIncTemp['anomalie'] + 14.185
        
        ax2.plot(df_anoIncTemp['year'], df_anoIncTemp['anomalie'].rolling(window=5).mean(), label='Moyenne mobile (5 ans)', color='green')
        ax2.set_title('Évolution de la population mondiale et des températures (1850-2021)\n avec moyenne mobile (5 ans)', fontsize=30)  # Ajuster la taille de la police
        ax2.set_ylabel("Anomalie de température", color="green" , fontsize=30)
        ax2.tick_params(axis='y', labelcolor='green')
    elif selected_graphic == "Somme du CO2":
        # Filtrer les données pour obtenir seulement celles où la colonne "iso_code" est renseignée et la période est de 1850 à 2018
        df_filtered = df_co2[(df_co2['iso_code'].notna()) & (df_co2['year'] >= 1850) & (df_co2['year'] <= 2018)]

        # Groupby par année et sum pour obtenir la somme de co2_including_luc et de la population pour chaque année
        df_sum_co2_population = df_filtered.groupby('year')[['co2_including_luc', 'population']].sum().reset_index()

        ax2.plot(df_sum_co2_population['year'], df_sum_co2_population['co2_including_luc'], label='Somme de CO2 (y compris LUC)', color='orange')
        ax2.set_title('Évolution Population Mondiale (1850-2021)', fontsize=40)  # Ajuster la taille de la police
        ax2.set_ylabel('Somme de CO2 (y compris LUC)', color='orange', fontsize=32)
        ax2.tick_params(axis='y', labelcolor='orange')

    ax1.set_xlabel('Année', fontsize=32)  # Ajuster la taille de la police
    ax1.set_ylabel('Population mondiale', color='blue', fontsize=32)  # Ajuster la taille de la police
    ax1.grid(True)
    ax1.legend(loc='upper left', fontsize=28) # Ajuster la taille de la police
    ax2.legend(loc='upper right', fontsize=28)
    
    # Afficher le graphique dans Streamlit
    st.pyplot(fig)
       
    
elif page == pages[2]:
    st.write("### Évolution des anomalies")
    tabMoyMob, tabIncertitudes= st.tabs(["Moyennes mobiles", "Incertitude"])
    
    df_anoIncTemp = pd.read_csv('data/Anomalies Incertitude Temperature.csv', sep=';')
    # Ajouter la constante de 14.185 à la colonne "anomalie"
    df_anoIncTemp['anomalie'] = df_anoIncTemp['anomalie'] + 14.185

    with tabMoyMob:
        # Ajouter une colonne pour la moyenne mobile sur 5 ans
        df_anoIncTemp['moyenne_mobile_5ans'] = df_anoIncTemp['anomalie'].rolling(window=5).mean()

        # Ajouter une colonne pour la moyenne mobile sur 10 ans
        df_anoIncTemp['moyenne_mobile_10ans'] = df_anoIncTemp['anomalie'].rolling(window=10).mean()
        # Tracer les courbes
        fig = plt.figure(figsize=(20, 10))
        plt.plot(df_anoIncTemp['year'], df_anoIncTemp['anomalie'], label='Anomalie')
        if st.checkbox("Afficher la moyenne mobile à 5 ans", True) : 
            plt.plot(df_anoIncTemp['year'], df_anoIncTemp['moyenne_mobile_5ans'], label='Moyenne mobile 5 ans')

        if st.checkbox("Afficher la moyenne mobile à 10 ans", True): 
            plt.plot(df_anoIncTemp['year'], df_anoIncTemp['moyenne_mobile_10ans'], label='Moyenne mobile 10 ans')

        plt.axhline(y=14.185, color='red', linestyle='--', linewidth=1)
        plt.title('Évolution des températures avec ajout et moyennes mobiles (1850-2021)')
        plt.xlabel('Année')
        plt.ylabel('Anomalie de température')
        plt.legend()
        plt.grid(True)
        st.pyplot(fig)
    with tabIncertitudes:
        # Ajouter la constante de 14.185 à la colonne "anomalie"
        df_anoIncTemp['anomalie_plus_incertitude'] = df_anoIncTemp['anomalie'] + df_anoIncTemp['incertitude']
        df_anoIncTemp['anomalie_moins_incertitude'] = df_anoIncTemp['anomalie'] - df_anoIncTemp['incertitude']

        # Tracer les courbes
        fig = plt.figure(figsize=(20, 10))
        plt.plot(df_anoIncTemp['year'], df_anoIncTemp['anomalie'], label='Anomalie')
        if st.checkbox("Afficher anomalie + Incertitude", True) : 
            plt.plot(df_anoIncTemp['year'], df_anoIncTemp['anomalie_plus_incertitude'], label='Anomalie + Incertitude', color="darkred")
            plt.fill_between(df_anoIncTemp['year'], df_anoIncTemp['anomalie'], df_anoIncTemp['anomalie_plus_incertitude'], color='pink')

        if st.checkbox("Afficher anomalie - Incertitude", True): 
            plt.plot(df_anoIncTemp['year'], df_anoIncTemp['anomalie_moins_incertitude'], label='Anomalie - Incertitude', color="darkred")
            plt.fill_between(df_anoIncTemp['year'], df_anoIncTemp['anomalie'], df_anoIncTemp['anomalie_moins_incertitude'], color='pink')

        plt.axhline(y=14.185, color='red', linestyle='--', linewidth=1)
        plt.title('Évolution des températures avec ajout et soustraction de l\'incertitude (1850-2021)')
        plt.xlabel('Année')
        plt.ylabel('Anomalie de température')
        plt.legend()
        plt.grid(True)
        st.pyplot(fig)

else:
    st.write("### Données sur les 10 pays les plus émetteurs")
    tabTemp, tabGreenhouseGas= st.tabs(["Évolution de la température", "Évolution des gaz à effets de serre"])
    df_co2 = pd.read_csv('data/CO2 Donnees.csv', sep=',')
    
    with tabGreenhouseGas: 

        # Filtrer les données pour exclure les lignes où la colonne "iso_code" est vide
        df_filtered = df_co2[df_co2['iso_code'].notnull()]

        # Sélectionner les 10 pays ayant le plus grand total dans les colonnes spécifiées
        top_10_countries = df_filtered.groupby('country').sum()[['co2_including_luc', 'methane', 'nitrous_oxide', 'total_ghg']].sum(axis=1).nlargest(10).index

        # Créer un dataframe combiné avec les données de chaque pays
        df_combined = pd.DataFrame()

        for country in top_10_countries:
            df_country = df_filtered[df_filtered['country'] == country].copy()
            
            # Supprimer les lignes contenant des valeurs NaN dans les colonnes spécifiées
            columns_to_clean = ['co2_including_luc', 'methane', 'nitrous_oxide', 'total_ghg']
            df_country = df_country.dropna(subset=columns_to_clean)
            
            # Ajouter une colonne pour le pays
            df_country['country'] = country
            
            # Concaténer avec le dataframe combiné
            df_combined = pd.concat([df_combined, df_country])

        # Tracer le graphique
        fig = plt.figure(figsize=(20, 10))
        for country in top_10_countries:
            df_plot = df_combined[df_combined['country'] == country]
            plt.plot(df_plot['year'], df_plot['co2_including_luc'] + df_plot['methane'] + df_plot['nitrous_oxide'] + df_plot['total_ghg'], label=country)

        plt.title('Évolution du total des émissions pour les 10 pays les plus émetteurs')
        plt.xlabel('Année')
        plt.ylabel('Total des émissions')
        plt.legend()
        plt.grid(True)
        st.pyplot(fig)

    with tabTemp:
        # Filtrer les données pour exclure les lignes où la colonne "iso_code" est vide
        df_filtered = df_co2[df_co2['iso_code'].notnull()]

        # Sélectionner les 10 pays ayant le plus grand total dans les colonnes spécifiées
        top_10_countries = df_filtered.groupby('country').sum()[['co2_including_luc', 'methane', 'nitrous_oxide', 'total_ghg']].sum(axis=1).nlargest(10).index

        # Créer un dataframe combiné avec les données de chaque pays
        df_combined = pd.DataFrame()

        for country in top_10_countries:
            df_country = df_filtered[df_filtered['country'] == country].copy()
            
            # Supprimer les lignes contenant des valeurs NaN dans les colonnes spécifiées
            columns_to_clean = ['temperature_change_from_ch4', 'temperature_change_from_co2', 'temperature_change_from_ghg', 'temperature_change_from_n2o']
            df_country = df_country.dropna(subset=columns_to_clean)
            
            # Ajouter une colonne pour le pays
            df_country['country'] = country
            
            # Concaténer avec le dataframe combiné
            df_combined = pd.concat([df_combined, df_country])

        # Tracer le graphique
        fig = plt.figure(figsize=(20, 10))
        for country in top_10_countries:
            df_plot = df_combined[df_combined['country'] == country]
            total_temperature_change = df_plot[columns_to_clean].sum(axis=1)
            plt.plot(df_plot['year'], total_temperature_change, label=country)

        plt.title('Évolution du changement de température pour les 10 pays les plus émetteurs')
        plt.xlabel('Année')
        plt.ylabel('Changement de température total')
        plt.legend()
        plt.grid(True)
        st.pyplot(fig)