# -*- coding: utf-8 -*-
"""
Created on Tue Jul 18 14:57:06 2023

@author: PC.054
"""

import streamlit as st

st.set_page_config(
    page_title="# Projet Température",
    page_icon="👋",
    layout="wide"
)

st.write("# Bienvenue au Projet Temperature MAI23 ! 👋")

st.sidebar.success("Choisissez un menu")

st.write("## Le Projet")
    
st.write("Ce projet est centré sur une étude de l'évolution des températures terrestres dans le passé afin de pouvoir prédire une éventuelle évolution future, à l'horizon 2050.")

st.write("Nous aurons à notre disposition une série de fichiers au format *.csv qui nous permettront de mettre en place plusieurs datasets sur lesquels nous baserons l'étude.")

st.write("Nous procéderons selon le cheminement suivant : Exploration, Visualisation, Analyse et Modélisation.")


st.image ("images/earth.jpg")


st.write("""
         ````python
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
         ````
         """)
         