import streamlit as st


st.header("calulatrice")
st.sidebar.title("Configuration")
with st.sidebar:
    figure=st.selectbox("choisir la figure",["cercle","rectangle"])

if figure=='cercle':
    rayon=st.number_input('Rayon',min_value=0,step=1)
    aire=rayon**2*3.14

btn=st.button("calculer l'aire")
if btn:
    st.write("aire=",aire)