import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Configuration du nom et de l'îcone de la page 
st.set_page_config(page_title="EXPLAIN", page_icon="🔲", layout="wide", initial_sidebar_state="auto")



# On charge le fichier sur notre machine
df = pd.read_csv('production-electrique-par-filiere-a-la-maille-region.csv', sep=';')

# On place les années dans l'ordre décroissant
df_sorted = df.sort_values(by='annee', ascending=False)

# On reset tous les index
df_sorted = df_sorted.reset_index(drop=True)

# On remplace les valeurs manquantes
df_sorted = df_sorted.fillna(0)



fig, ax = plt.subplots()
df_sorted[['energie_produite_annuelle_eolien_enedis_mwh', 'energie_produite_annuelle_photovoltaique_enedis_mwh', 'energie_produite_annuelle_hydraulique_enedis_mwh', 'energie_produite_annuelle_bio_energie_enedis_mwh', 'energie_produite_annuelle_cogeneration_enedis_mwh']].sum().plot(kind='bar', ax=ax)
ax.set_ylabel("Production (GWh)")
st.pyplot(fig)