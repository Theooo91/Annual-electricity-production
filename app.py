import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import os

from streamlit_navigation_bar import st_navbar
from streamlit_option_menu import option_menu

# Configuration du nom et de l'îcone de la page 
st.set_page_config(page_title="EXPLAIN", page_icon="🔲", layout="wide", initial_sidebar_state="auto")


# Configuration de la première barre de tâche 
selected = option_menu(
    menu_title=None,  # Ne pas afficher de titre
    options=["Documentation", "Tutorials", "Examples", "Community", "GitHub", "Settings", "Features"],
    icons=["book", "play-circle", "file-earmark", "people", "github", "gear", "star"],  # Icônes associées
    menu_icon="cast",  # Icône du menu
    default_index=0,  # Option par défaut
    orientation="horizontal",  # Orientation horizontale
)

# Définir des actions selon la page sélectionnée
if selected == "Documentation":
    st.write("Bienvenue dans la Documentation.")
elif selected == "Tutorials":
    st.write("Ici, vous trouverez des tutoriels.")
elif selected == "Examples":
    st.write("Exemples de projet.")
elif selected == "Community":
    st.write("Communauté.")
elif selected == "GitHub":
    st.write("[Lien vers GitHub](https://github.com/GIF-Alyex/Projet-EXPLAIN-mastercamp)")
elif selected == "Settings":
    st.write("Paramètres.")
elif selected == "Features":
    st.write("Fonctionnalités.")




# On charge le fichier sur notre machine
df = pd.read_csv('production-electrique-par-filiere-a-la-maille-region.csv', sep=';')

# On place les années dans l'ordre décroissant
df_sorted = df.sort_values(by='annee', ascending=False)

# On reset tous les index
df_sorted = df_sorted.reset_index(drop=True)

# On remplace les valeurs manquantes
df_sorted = df_sorted.fillna(0)


