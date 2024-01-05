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

# Ajouter du style CSS pour centrer le texte
st.write("""
    <style>
        .centered-text {
            text-align: center;
        }
    </style>
""", unsafe_allow_html=True)

# Utiliser la classe CSS pour centrer le texte
st.write("<h1 class='centered-text'>Bienvenue au Projet Temperature MAI23 ! 👋</h1>", unsafe_allow_html=True)

# Ajouter un espace (saut de ligne)
st.write("<br>", unsafe_allow_html=True)

st.image ("images/earth.jpg")


st.sidebar.success("Choisissez un menu")


# Utiliser le composant HTML div pour centrer le texte
st.markdown("""
    <div style='text-align:center'>
        <h2>Le Projet</h2>
    </div>
""", unsafe_allow_html=True)

st.write("### Ce projet est centré sur une étude de l'évolution des températures terrestres dans le passé afin de pouvoir prédire une éventuelle évolution future, à l'horizon 2050 et 2100.")
st.write("### Nous avons à notre disposition un Dataset créé à partir de fichiers provenant de différentes sources, qui nous permettra d'avancer dans notre recherche.")
st.write("### Nous procéderons selon le cheminement suivant : Introduction (vous y êtes), Origines et explorations des données, Visualisation, Prévisions et conclusions/perspectives.")
st.write("### Toutefois avant de commencer, écoutons l'article 1er de la Déclaration Universelle des Droits de l'Homme (Article 1 of the Universal Declaration of Human Rights). La langue ne vous dit probablement rien et pourtant.")
st.write("### Nous verrons plus tard l'impact du climat sur le cours de l'Histoire de l'Humanité. Plus précisément avec les Normands, les Vikings et l'Angleterre en 1066. Sans oublier la Révolution Française.")
st.write("<br>", unsafe_allow_html=True)

st.image ("images/omniglot.jpg")
st.write("<br>", unsafe_allow_html=True)

# Utiliser le composant HTML div pour centrer le texte
st.markdown("""
    <div style='text-align:center'>
        <h2>Vieil Anglais avant Guillaume le Conquérant</h2>
    </div>
""", unsafe_allow_html=True)

# Charger le fichier audio
audio_file = open("oldenglish.mp3", "rb").read()

# Afficher le lecteur audio
st.audio(audio_file, format="audio/mp3")

st.write("https://www.omniglot.com/writing/oldenglish.htm")
st.write("<br>", unsafe_allow_html=True)

# Utiliser le composant HTML div pour centrer le texte
st.markdown("""
    <div style='text-align:center'>
        <h2>Hémisphère Nord - 2000 ans de climat</h2>
    </div>
""", unsafe_allow_html=True)

st.image ("images/hemisphère-nord-temperature-2000-ans.jpg")

st.write("### Mission EPICA, ayant foré et analysé d’immenses carottes de glace en Antarctique. (3600m pour 800 000 ans)")
st.write("### Deux événements sortent du lot; le réchauffement médiéval et le petit âge glaciaire.")
st.write("<br>", unsafe_allow_html=True)

st.write("### Et maintenant, en avant vers les trucs sérieux!")

st.write("## Cependant pas d'inquiétudes nous aborderons les trucs très sérieux dans le chapitre Conclusion et Perspectives.")