

import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st 

from fbprophet import Prophet

#https://facebook.github.io/prophet/docs/quick_start.html#python-api
df = pd.read_csv('https://raw.githubusercontent.com/facebook/prophet/main/examples/example_wp_log_peyton_manning.csv')
m = Prophet()
m.fit(df)  # df is a pandas.DataFrame with 'y' and 'ds' columns
future = m.make_future_dataframe(periods=365)
test = m.predict(future)
test
st.dataframe(future)
"""
st.set_page_config(
    page_title="Projet Température",
    page_icon="👋",
    layout="wide",
)

df_anoIncTemp = pd.read_csv('data/Anomalies Incertitude Temperature.csv', sep = ';')

# Supposons que df_anoIncTemp contienne les données de l'anomalie de température
# Assurez-vous que ce DataFrame est correctement défini avec les colonnes 'ds' (datestamp) et 'y' (valeur à prédire).

# Renommer les colonnes pour correspondre aux attentes de Prophet
df_anoIncTemp_prophet = df_anoIncTemp.rename(columns={'year': 'ds', 'anomalie': 'y'})

# Créer et entraîner le modèle Prophet
model = Prophet()
model.fit(df_anoIncTemp_prophet)

# Créer un DataFrame pour les années que vous souhaitez prédire (par exemple, 2021 à 2050)
future_2050 = pd.DataFrame({'ds': pd.date_range(start='2021-01-01', end='2050-01-01', freq='Y')})

# Faire des prédictions pour la période 2021-2050
forecast_2050 = model.predict(future_2050)

# Tracer les résultats pour la période 2021-2050
fig_2050 = model.plot(forecast_2050)
plt.title('Prédictions de l\'anomalie de température (2021-2050)')
plt.xlabel('Année')
plt.ylabel('Anomalie de température')
plt.show()

# Créer un DataFrame pour les années que vous souhaitez prédire (par exemple, 2021 à 2100)
future_2100 = pd.DataFrame({'ds': pd.date_range(start='2021-01-01', end='2100-01-01', freq='Y')})

# Faire des prédictions pour la période 2021-2100
forecast_2100 = model.predict(future_2100)

# Tracer les résultats pour la période 2021-2100
fig_2100 = model.plot(forecast_2100)
plt.title('Prédictions de l\'anomalie de température (2021-2100)')
plt.xlabel('Année')
plt.ylabel('Anomalie de température')
plt.show()
"""


import streamlit as st


# Titre de l'application
st.write("# Dérive des Continents")
st.image("images/hemisphère-nord-temperature-800000.jpg")
# Charger et afficher la vidéo avec une largeur personnalisée
video_path = "derive.mp4" 
video_file = open(video_path, "rb").read()
st.video(video_file)
st.write("Larousse Editions")

st.write("")
st.write("")
st.write("Événement majeur de l'histoire de l'humanité, la conversion des chasseurs-cueilleurs à l'agriculture date d' environ 11 000 ans.")
st.write("Ce fut un processus long et complexe, qui s'est opéré sous diverses latitudes.")

st.write("L’avènement de notre espèce, probablement en Afrique, remonte à quelque 200 000 ans, celle de l’agriculture, à environ 11 000 ans.")
st.write("Le « moment » qui a vu basculer des groupes humains qui vivaient de la chasse et de la collecte depuis des dizaines de millénaires")
st.write("dans la sphère des agriculteurs est donc très récent, observe George Willcox, directeur de recherche émérite au CNRS et grand spécialiste de la domestication de plantes au Proche-Orient.")
st.write("L’homme moderne ( Homo sapiens sapiens ) n’est réellement paysan que depuis quelque 500 générations, ce qui représente moins de 5 % de son histoire.")
st.write("www.science-et-vie.com")

st.image("images/origines-agriculture.jpg")
st.image("images/hemisphère-nord-temperature-16000.jpg")


st.write("La circulation des courants océaniques dans l'Atlantique, qui contribuent à la régulation du climat mondial, est à son plus faible niveau en 1600 ans,")
st.write("en partie à cause du changement climatique, mettent en garde mercredi des chercheurs.")

st.write("Deux études parues dans Nature viennent valider l'hypothèse de longue date d'un affaiblissement de la circulation de ces courants connus sous l'acronyme d'AMOC (circulation méridienne de retournement de l'Atlantique).")

st.write("Cet affaiblissement des courants est le fruit de la fonte de la banquise, des glaciers et de plates-formes glaciaires, qui libèrent de l'eau douce, moins dense que l'eau salée, dans l'Atlantique Nord.")
st.write("L'eau douce affaiblit l'AMOC car elle empêche les eaux de devenir assez denses pour couler, explique à l'AFP David Thornalley, de l'University College London, co-auteur d'une des études.")
st.write("Si le système continue de faiblir, cela pourrait perturber les conditions météorologiques.")

st.write("Cette circulation permanente des eaux marines consiste en une remontée des eaux chaudes des zones tropicales de l'Atlantique vers le Nord grâce au Gulf Stream, réchauffant au passage l'Europe de l'Ouest.")
st.write("Une fois dans l'Atlantique Nord, ces eaux refroidissent, deviennent plus denses et plus lourdes et coulent sous des eaux plus chaudes pour repartir vers le sud.")

st.write("Si le système continue de faiblir, cela pourrait perturber les conditions météorologiques depuis les États-Unis et l'Europe jusqu'au Sahel et provoquer une hausse plus rapide du niveau des mers sur la côte est des États-Unis")
st.write(", avertit le Woods Hole Oceanographic Institution, qui a participé aux recherches.")

st.write("Ces courants marins transportent aussi d'une zone à l'autre des nutriments, de l'oxygène, des larves de coraux ou encore de poissons. Ils contribuent également à la capacité des océans à absorber et à stocker du dioxyde de carbone (CO2), principal responsable du réchauffement climatique.")

st.write("Dans la première étude, David Thornalley et son équipe ont étudié les grains de sable déposés par les courants sur les fonds marins au fil du temps. Plus les grains de sable retrouvés dans les sédiments étaient gros, plus forts devaient être les courants qui les ont transportés.")

st.write("Les résultats révèlent que l'AMOC a été relativement stable entre l'an 400 et 1850 et a commencé à s'affaiblir au début de l'ère industrielle.")

st.write("La seconde étude s'est penchée sur les températures de la surface de l'océan et en déduit que l'AMOC a décliné d'environ 15% au cours des cinquante dernières années, probablement à cause du changement climatique dû à des activités humaines.")

st.write("S'il est difficile de connaître avec certitude le rôle joué par le réchauffement climatique, le fait que l'AMOC soit resté faible et se soit affaibli au cours du 20e siècle, avec un déclin notable à partir de 1950 environ, est très certainement lié à des facteurs humains, estime David Thornalley.")

st.image("images/convoyeur.jpg")
st.write("www.rtbf.be")

st.image("images/slushball-earth_nature_image.jpg")
st.write("astrobiology.com")