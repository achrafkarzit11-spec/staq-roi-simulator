import streamlit as st
import pandas as pd

st.set_page_config(page_title="Staq ROI Simulator", layout="centered")

st.title("🚀 Staq ROI Simulator")
st.subheader("Time-to-Market & Business Value Analysis")

# Sidebar inputs
st.sidebar.header("Paramètres du projet")
dev_salary = st.sidebar.number_input("Salaire annuel moyen Développeur (€)", value=75000)
num_devs = st.sidebar.slider("Nombre de développeurs sur le projet", 1, 10, 3)
time_to_build_months = st.sidebar.slider("Temps de build interne (mois)", 6, 24, 18)
staq_annual_cost = st.sidebar.number_input("Coût annuel licence Staq (€)", value=50000)

# Calculations
internal_dev_cost = (dev_salary / 12) * time_to_build_months * num_devs
staq_total_cost = staq_annual_cost * (time_to_build_months / 12)
savings = internal_dev_cost - staq_total_cost

# Display
col1, col2 = st.columns(2)
col1.metric("Coût Build Interne", f"{internal_dev_cost:,.0f} €")
col2.metric("Coût avec Staq", f"{staq_total_cost:,.0f} €")

st.success(f"Économie totale potentielle : {savings:,.0f} €")

st.markdown("""
### Pourquoi Staq est le meilleur choix :
1. **Time-to-Market :** Réduction du temps de développement grâce aux APIs pré-intégrées.
2. **Conformité :** Gestion des enjeux réglementaires (KYC/AML) native.
3. **Risque :** Réduction drastique des risques d'échec technique sur le build de base.
""")