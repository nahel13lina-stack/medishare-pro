import streamlit as st

st.title("MediShare Pro")
st.write("Bienvenue sur ton application de gestion et de solidarité !")

# Un petit exemple de formulaire simple pour commencer
nom = st.text_input("Nom ou Prénom :")
if st.button("Valider"):
    if nom:
        st.success(f"Merci pour votre participation, {nom} !")
    else:
        st.warning("Veuillez entrer un nom.")
