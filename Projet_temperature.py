# -*- coding: utf-8 -*-
"""
Created en catastrophe

@author: Deludis
"""

import streamlit as st
import pandas as pd 
import numpy as np    
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


st.set_page_config(
    page_title="# Projet Température",
    page_icon="👋",
    layout="centered",
)

st.write("# Bienvenue au Projet Temperature MAI23 ! 👋")

st.image ("images/earth.jpg")

st.sidebar.success("Choisissez un menu")

st.write("## Le Projet")
    
st.write("Ce projet est centré sur une étude de l'évolution des températures terrestres dans le passé afin de pouvoir prédire une éventuelle évolution future, à l'horizon 2050.")

st.write("Nous aurons à notre disposition une série de fichiers au format *.csv qui nous permettront de mettre en place plusieurs datasets sur lesquels nous baserons l'étude.")

st.write("Nous procéderons selon le cheminement suivant : Introduction (vous y êtes), Origines et explorations des données, Visualisation, Prévisions et conclusions/persepectives.")

st.write("Toutefois avant de commencer, écoutons l'article 1er de la Déclaration Unverselle des Droits de l'Homme (Article 1 of the Universal Declaration of Human Rights). La langue ne vous dit probablement rien et pourtant.")

st.write("Nous verrons plus tard l'impact de la météorologie au cours de l'Histoire de l'Humanité. Plus précisément avec les Normands, les Vikings et l'Angleterre en 1066")

st.image ("images/Omniglot.jpg")

# Charger le fichier audio
audio_file = open("oldenglish.mp3", "rb").read()

# Afficher le lecteur audio
st.audio(audio_file, format="audio/mp3")

st.write("https://www.omniglot.com/writing/oldenglish.htm")

st.image ("images/hemisphère-nord-temperature-2000-ans.jpg")

st.write("Et maintenant, en avant vers les trucs sérieux!")

st.write("### Cependant pas d'inquiétudes nous aborderons les trucs très sérieux dans le chapitre Conclusion et Perspectives.")