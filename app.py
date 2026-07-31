import streamlit as st

# Configuration de la page
st.set_page_config(
    page_title="MediShare Pro - Solidarité",
    page_icon="🤝",
    layout="centered"
)

# En-tête chaleureux et solidaire
st.title("🤝 MediShare Pro")
st.subheader("Ensemble, faisons vivre la solidarité et l'entraide")

st.markdown("""
Bienvenue sur notre espace de soutien et de coordination. Cette plateforme a été pensée pour rassembler nos forces, partager les informations essentielles et venir en aide à ceux qui en ont le plus besoin, dans un esprit de fraternité et de transparence.
""")

st.markdown("---")

# Guide simple pour les utilisateurs
st.subheader("💡 Comment participer ?")
st.markdown("""
1. **Consultez les informations** partagées sur cette plateforme.
2. **Laissez votre nom ou un message** de soutien via le formulaire ci-dessous.
3. **Partagez cette initiative** autour de vous pour amplifier notre élan de solidarité.
""")

st.markdown("---")

# Section interactive et accueillante
st.subheader("✍️ Laisser une trace de votre passage ou un message de soutien")

with st.form("form_soutien"):
    nom_utilisateur = st.text_input("Votre Nom ou Prénom :")
    message_soutien = st.text_area("Votre message ou vos conseils (optionnel) :")
    
    bouton_valider = st.form_submit_button("Envoyer mon soutien")

if bouton_valider:
    if nom_utilisateur:
        st.success(f"Barakallahu feekum, {nom_utilisateur} ! Merci du fond du cœur pour votre présence et votre soutien précieux.")
        if message_soutien:
            st.info(f"Votre message enregistré : \"{message_soutien}\"")
    else:
        st.warning("Veuillez s'il vous plaît indiquer votre nom ou prénom avant d'envoyer.")

st.markdown("---")
st.caption("MediShare Pro — Porté par la solidarité et l'espoir.")
