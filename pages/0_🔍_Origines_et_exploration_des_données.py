
import streamlit as st
import pandas as pd


st.set_page_config(
    page_title="Projet Température",
    page_icon="👋",
    layout="wide",
)

df_anoIncTemp = pd.read_csv('data/Anomalies Incertitude Temperature.csv', sep=';')
df_anoMoyGlobal = pd.read_csv('data/Anomalies moyenne Global.csv', sep=';')
df_co2 = pd.read_csv('data/CO2 Donnees.csv', sep=',')
df_geo = pd.read_csv('data/Geographie.csv', sep=';')
df_global = pd.read_csv('data/Temperature Index Global 100.csv', sep=',')
df_north = pd.read_csv('data/Temperature Index Nord 100.csv', sep=',')
df_south = pd.read_csv('data/Temperature Index Sud 100.csv', sep=',')
df_tempAbs = pd.read_csv('data/Temperature Mensuelle Absolue 1951_1980.csv', sep=';')
df_zone = pd.read_csv('data/Temperature Moyenne Index Global 100.csv', sep=',')

st.write("# Origines et exploration des données")

st.write("## L'incertitude mesurée sur les anomalies de température de 1850 à 2018 en degré Celsius")
st.write("### Ce dataframe contient les données relatives aux anomalies constatées et à l'incertitude causée par les appareillages de mesure. Nous noterons que l'incertitude diminue drastiquement une première fois à la fin du XIXème siècle et une seconde fois dans le dernier tiers tiers du XXème siècle. Depuis nous avons atteint un seuil aux alentours de 0,04 degré Celsius.")
st.dataframe(df_anoIncTemp.head())
st.write("Dimensions du dataframe :")
st.write(df_anoIncTemp.shape)
if st.checkbox("Afficher les valeurs manquantes", key="anoIncTempValeursManquantes") : 
    st.dataframe(df_anoIncTemp.isna().sum())
        
    if st.checkbox("Afficher les doublons", key="anoIncTempDoublons") : 
        st.write(df_anoIncTemp.duplicated().sum())

st.write("## Anomalies moyenne Global de 1750 à 2021 en degré Celsius")
st.write("### Ce datatframe contient les données relatives aux températures mensuelles moyennes (associées aux anomalies détectées) au niveau planétaire.")
st.dataframe(df_anoMoyGlobal.head())
st.write("Dimensions du dataframe :")
st.write(df_anoMoyGlobal.shape)
if st.checkbox("Afficher les valeurs manquantes", key="anoMoyGlobalValeursManquantes") : 
    st.dataframe(df_anoMoyGlobal.isna().sum())
        
    if st.checkbox("Afficher les doublons", key="anoMoyGlobalDoublons") : 
        st.write(df_anoMoyGlobal.duplicated().sum())

st.write("## Informations entités nationales et supra-nationales de 1850 à 2021")
st.write("### Voici le gros dataframe, véritable trésor d'informations statistiques sur tous les pays, territoires et autres entités politico-commerciales. Il y a beaucoup de valeurs absentes pour de nombreux pays et ce jusqu'au lendemain de la Seconde Guerre Mondiale. Notre étude s'articule autour de ce dataframe.")
st.dataframe(df_co2.head())
st.write("Dimensions du dataframe :")
st.write(df_co2.shape)
if st.checkbox("Afficher les valeurs manquantes", key="co2ValeursManquantes") : 
    st.dataframe(df_co2.isna().sum())
        
    if st.checkbox("Afficher les doublons", key="co2Doublons"): 
        st.write(df_co2.duplicated().sum())

st.write("## Geographie")
st.write("### Ce dataframe provient d'un webscraping provenant de https://en.wikipedia.org/wiki/ISO_3166-1 pour les codes à 3 lettres ou CA3 et d'une jointure avec un webscraping sur https://unstats.un.org/unsd/methodology/m49/ pour effectuer un classement des pays par continents. Il est à noter que dans le cas où une entité nationale serait présente sur plusieurs continents, la capitale serait la donnée discrimante.")
st.dataframe(df_geo.head())
st.write("Dimensions du dataframe :")
st.write(df_geo.shape)
if st.checkbox("Afficher les valeurs manquantes", key="geoValeursManquantes") : 
    st.dataframe(df_geo.isna().sum())
        
    if st.checkbox("Afficher les doublons", key="geoDoublons"): 
        st.write(df_geo.duplicated().sum())

st.write("## Temperature Index Global 100")
st.write("### Ce dataframe ainsi que les deux suivants contiennent des valeurs mensuelles et annuelles de 1880 à 2021 concernant les fluctuations de température pour la planète, l'hémisphère Nord et Sud respectivement.")
st.dataframe(df_global.head())
st.write("Dimensions du dataframe :")
st.write(df_global.shape)
if st.checkbox("Afficher les valeurs manquantes", key="globalValeursManquantes") : 
    st.dataframe(df_global.isna().sum())
        
    if st.checkbox("Afficher les doublons", key="globalDoublons"): 
        st.write(df_global.duplicated().sum())

st.write("## Temperature Index Nord 100")
st.dataframe(df_north.head())
st.write("Dimensions du dataframe :")
st.write(df_north.shape)
if st.checkbox("Afficher les valeurs manquantes", key="northValeursManquantes") : 
    st.dataframe(df_north.isna().sum())
        
    if st.checkbox("Afficher les doublons", key="northDoublons"): 
        st.write(df_north.duplicated().sum())

st.write("## Temperature Index Sud 100")
st.dataframe(df_south.head())
st.write("Dimensions du dataframe :")
st.write(df_south.shape)
if st.checkbox("Afficher les valeurs manquantes", key="southValeursManquantes") : 
    st.dataframe(df_south.isna().sum())
        
    if st.checkbox("Afficher les doublons", key="southDoublons"): 
        st.write(df_south.duplicated().sum())

st.write("## Temperature Moyenne Index Global 100")
st.dataframe(df_zone.head())
st.write("Dimensions du dataframe :")
st.write(df_zone.shape)
if st.checkbox("Afficher les valeurs manquantes", key="zoneValeursManquantes") : 
    st.dataframe(df_zone.isna().sum())
        
    if st.checkbox("Afficher les doublons", key="zoneDoublons"): 
        st.write(df_zone.duplicated().sum())
       

st.write("## Temperature Mensuelle Absolue de 1951 à 1980 en degré Celsius")
st.write("### Ce dataframe contient les températures absolues mensuelles. De plus il contient aussi dans sa partie descriptive (avant nettoyage) la moyenne absolue de température au-dessus et au-dessous de la banquise.")
st.write("### Using air temperature above sea ice:   14.185 +/- 0.046, c'est cette valeur qui sera retenue pour notre étude.")
st.write("### Using water temperature below sea ice: 14.729 +/- 0.046")
st.dataframe(df_tempAbs.head())
st.write("Dimensions du dataframe :")
st.write(df_tempAbs.shape)
if st.checkbox("Afficher les valeurs manquantes", key="tempsAbsValeursManquantes") : 
    st.dataframe(df_tempAbs.isna().sum())
        
    if st.checkbox("Afficher les doublons", key="tempsAbsDoublons"): 
        st.write(df_tempAbs.duplicated().sum())

st.write("#### Les fichiers .csv et .txt utilisés pour cette étude proviennent de https://data.giss.nasa.gov/gistemp/ et de https://github.com/owid/co2-data. Dans les autres cas leur provenannce est spécifiée dans la description des dataframes concernés.")