import streamlit as st

# Título de la app
st.title("¿QUE MEDICMENTO QUIERES VER HOY?")
# Texto simple
st.header("sigue aca:")

st.write("Hola, soy [TU NOMBRE] y esta es mi primera aplicación con Streamlit.")

# Un input interactivo
cuando = st.number_input("¿en cuantos dias lo quieres?", min_value=0, max_value=10)

opcion = st.selectbox("Elige cuantos medicamentos quieres", ["1", "2", "3"])


# Un botón
if st.button("Presiona aquí"):
    st.balloons()  # Animación de globos
    st.success("¡Funciona perfectamente!")
