
import streamlit as st
import pandas as pd

df_anoIncTemp = pd.read_csv('data/Anomalies Incertitude Temperature.csv', sep=';')
df_anoMoyGlobal = pd.read_csv('data/Anomalies moyenne Global.csv', sep=';')
df_co2 = pd.read_csv('data/CO2 Donnees.csv', sep=',')
df_geo = pd.read_csv('data/Geographie.csv', sep=';')
df_global = pd.read_csv('data/Temperature Index Global 100.csv', sep=',')
df_north = pd.read_csv('data/Temperature Index Nord 100.csv', sep=',')
df_south = pd.read_csv('data/Temperature Index Sud 100.csv', sep=',')
df_tempAbs = pd.read_csv('data/Temperature Mensuelle Absolue 1951_1980.csv', sep=';')
df_zone = pd.read_csv('data/Temperature Moyenne Index Global 100.csv', sep=',')

st.write("## L'incertitude mesurée sur les anomalies de température")
st.dataframe(df_anoIncTemp.head())
st.write("Dimensions du dataframe :")
st.write(df_anoIncTemp.shape)
if st.checkbox("Afficher les valeurs manquantes", key="anoIncTempValeursManquantes") : 
    st.dataframe(df_anoIncTemp.isna().sum())
        
    if st.checkbox("Afficher les doublons", key="anoIncTempDoublons") : 
        st.write(df_anoIncTemp.duplicated().sum())


st.write("""
         Ce dataframe se présente en 3 colonnes :
         - L'année
         - La somme des anomalies de l'année
         - L'incertitude dû à la qualité des mesures
         """)
st.write("En 1950 les climatologues se sont accordés pour définir qu'une anomalie était une température d'un écart de 14.185 °C par rapport à une normale de saison. ")

st.write("## Anomalies moyenne Global")
st.dataframe(df_anoMoyGlobal.head())
st.write("Dimensions du dataframe :")
st.write(df_anoMoyGlobal.shape)
if st.checkbox("Afficher les valeurs manquantes", key="anoMoyGlobalValeursManquantes") : 
    st.dataframe(df_anoMoyGlobal.isna().sum())
        
    if st.checkbox("Afficher les doublons", key="anoMoyGlobalDoublons") : 
        st.write(df_anoMoyGlobal.duplicated().sum())

st.write("## CO2 Donnees")
st.dataframe(df_co2.head())
st.write("Dimensions du dataframe :")
st.write(df_co2.shape)
if st.checkbox("Afficher les valeurs manquantes", key="co2ValeursManquantes") : 
    st.dataframe(df_co2.isna().sum())
        
    if st.checkbox("Afficher les doublons", key="co2Doublons"): 
        st.write(df_co2.duplicated().sum())

st.write("## Geographie")
st.dataframe(df_geo.head())
st.write("Dimensions du dataframe :")
st.write(df_geo.shape)
if st.checkbox("Afficher les valeurs manquantes", key="geoValeursManquantes") : 
    st.dataframe(df_co2.isna().sum())
        
    if st.checkbox("Afficher les doublons", key="geoDoublons"): 
        st.write(df_co2.duplicated().sum())

st.write("## Temperature Index Global 100")
st.dataframe(df_global.head())
st.write("Dimensions du dataframe :")
st.write(df_global.shape)
if st.checkbox("Afficher les valeurs manquantes", key="globalValeursManquantes") : 
    st.dataframe(df_co2.isna().sum())
        
    if st.checkbox("Afficher les doublons", key="globalDoublons"): 
        st.write(df_co2.duplicated().sum())

st.write("## Temperature Index Nord 100")
st.dataframe(df_north.head())
st.write("Dimensions du dataframe :")
st.write(df_north.shape)
if st.checkbox("Afficher les valeurs manquantes", key="northValeursManquantes") : 
    st.dataframe(df_co2.isna().sum())
        
    if st.checkbox("Afficher les doublons", key="northDoublons"): 
        st.write(df_co2.duplicated().sum())

st.write("## Temperature Index Sud 100")
st.dataframe(df_south.head())
st.write("Dimensions du dataframe :")
st.write(df_south.shape)
if st.checkbox("Afficher les valeurs manquantes", key="southValeursManquantes") : 
    st.dataframe(df_co2.isna().sum())
        
    if st.checkbox("Afficher les doublons", key="southDoublons"): 
        st.write(df_co2.duplicated().sum())

st.write("## Temperature Mensuelle Absolue 1951_1980")
st.dataframe(df_tempAbs.head())
st.write("Dimensions du dataframe :")
st.write(df_tempAbs.shape)
if st.checkbox("Afficher les valeurs manquantes", key="tempsAbsValeursManquantes") : 
    st.dataframe(df_co2.isna().sum())
        
    if st.checkbox("Afficher les doublons", key="tempsAbsDoublons"): 
        st.write(df_co2.duplicated().sum())

st.write("## Temperature Moyenne Index Global 100")
st.dataframe(df_zone.head())
st.write("Dimensions du dataframe :")
st.write(df_zone.shape)
if st.checkbox("Afficher les valeurs manquantes", key="zoneValeursManquantes") : 
    st.dataframe(df_co2.isna().sum())
        
    if st.checkbox("Afficher les doublons", key="zoneDoublons"): 
        st.write(df_co2.duplicated().sum())