import streamlit as st

# Configuration de la page
st.set_page_config(page_title="Staq | ROI & Pricing", layout="wide")

# Navigation
page = st.sidebar.radio("Navigation", ["Simulateur ROI", "Modèle Pricing Staq"])

if page == "Simulateur ROI":
    st.title("🚀 Staq ROI Simulator")
    st.write("---")
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.subheader("Paramètres")
        dev_salary = st.number_input("Salaire annuel développeur (€)", value=75000)
        num_devs = st.slider("Nombre de développeurs", 1, 10, 3)
        time_build = st.slider("Temps de build interne (mois)", 6, 24, 18)
        cost_staq = st.number_input("Coût annuel Staq (€)", value=50000)
        
    with col2:
        st.subheader("Analyse de Valeur")
        internal_cost = (dev_salary / 12) * time_build * num_devs
        staq_cost = cost_staq * (time_build / 12)
        savings = internal_cost - staq_cost
        
        m1, m2 = st.columns(2)
        m1.metric("Coût Build Interne", f"{internal_cost:,.0f} €")
        m2.metric("Coût avec Staq", f"{staq_cost:,.0f} €")
        
        st.success(f"Économie totale : {savings:,.0f} €")

elif page == "Modèle Pricing Staq":
    st.title("💰 Modèle de Pricing Staq")
    st.write("Transparence totale. Aucun coût caché.")
    
    st.info("""
    **Best of Both Worlds :**
    *   **PaaS :** Choisissez uniquement les services dont vous avez besoin (Payments, Cards, Accounts).
    *   **SaaS :** Nous gérons le backend, la sécurité et la conformité.
    *   **Scale :** Payez au nombre d'utilisateurs. Plus vous grandissez, plus vos coûts s'optimisent.
    """)
    
    st.table({
        "Service": ["BaaS", "Cartes", "Identité", "Prêts"],
        "Modèle": ["PaaS", "PaaS", "PaaS", "SaaS"],
        "Avantage": ["Infra modulable", "Émission rapide", "Conformité native", "Conversion élevée"]
    })
