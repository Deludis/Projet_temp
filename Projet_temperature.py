# -*- coding: utf-8 -*-
"""
Created on Tue Jul 18 14:57:06 2023

@author: PC.054
"""

import streamlit as st

st.set_page_config(
    page_title="Hello",
    page_icon="👋",
)

st.write("# Bienvenue au Projet Temperature MAI23 ! 👋")

st.sidebar.success("Choisissez un menu")

st.write("### Le Projet")
    
st.write("Ce projet est centré sur une étude de l'évolution des températures terrestres dans le passé afin de pouvoir prédire une éventuelle évolution future, à l'horizon 2050.")

st.write("Nous aurons à notre disposition une série de fichiers au format *.csv qui nous permettront d'obtenir in fine un dataset nommé CO2.csv sur lequel nous baserons l'étude.")

st.write("En premier lieu, nous explorerons ce dataset. Puis, grâce à la Data Visualisation, nous extrairons des informations pertinentes. Et nous terminerons par l'implémentations de modèles de Machine Learning pour prédire l'évolution des températures.")


st.image ("images/earth.jpg")

"""
import pandas as pd 
import numpy as np 
import streamlit as st 
import seaborn as sns 
import matplotlib.pyplot as plt
import plotly.express as px
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
import joblib
from sklearn.metrics import r2_score


df_anoIncTemp = pd.read_csv('data/Anomalies Incertitude Temperature.csv', sep = ';')
df_anoMoyGlobal = pd.read_csv('data/Anomalies moyenne Global.csv', sep = ';')
df_co2 = pd.read_csv('data/CO2 Donnees.csv', sep = ',')
df_geo = pd.read_csv('data/Geographie.csv', sep = ';')
df_global = pd.read_csv('data/Temperature Index Global 100.csv', sep = ',')
df_north = pd.read_csv('data/Temperature Index Nord 100.csv', sep = ',')
df_south = pd.read_csv('data/Temperature Index Sud 100.csv', sep = ',')
df_tempAbs = pd.read_csv('data/Temperature Mensuelle Absolue 1951_1980.csv', sep = ';')
df_zone = pd.read_csv('data/Temperature Moyenne Index Global 100.csv', sep = ',')

 
elif page == pages[2]: 
    st.write("### Analyse de données")
    
    

 """