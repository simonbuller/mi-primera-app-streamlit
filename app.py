import streamlit as st

import streamlit as st
import pandas as pd

# 🎯 Configuración general
st.set_page_config(page_title="Comparador de Precios de Farmacias", page_icon="💊", layout="centered")

st.title("💊 Comparador de Precios de Farmacias en Chile")
st.markdown("Compara precios de medicamentos entre las principales farmacias del país 🇨🇱")

# 💾 Datos simulados (puedes reemplazar por un CSV o una API)
data = {
    "Medicamento": ["Paracetamol 500mg", "Ibuprofeno 400mg", "Amoxicilina 500mg"],
    "Cruz Verde": [1290, 1850, 3890],
    "Salcobrand": [1150, 1790, 3550],
    "Ahumada": [1350, 1920, 3990]
}

df = pd.DataFrame(data)

# 🔍 Entrada del usuario
producto = st.text_input("Ingresa el nombre del medicamento (ej: Paracetamol 500mg):")

# 📊 Mostrar resultados
if producto:
    resultado = df[df["Medicamento"].str.lower() == producto.lower()]
    if not resultado.empty:
        precios = resultado.melt(id_vars=["Medicamento"], var_name="Farmacia", value_name="Precio (CLP)")
        menor = precios["Precio (CLP)"].min()
        precios["Más barato"] = precios["Precio (CLP)"] == menor

        st.subheader(f"Resultados para: `{producto}`")
        st.dataframe(precios.style.apply(lambda x: ['background: #c8e6c9' if v else '' for v in x["Más barato"]], axis=1))
        
        st.success(f"💰 La farmacia más barata es **{precios.loc[precios['Más barato'], 'Farmacia'].values[0]}**, con ${menor:,}")
    else:
        st.warning("⚠️ Producto no encontrado. Intenta con Paracetamol, Ibuprofeno o Amoxicilina.")
else:
    st.info("🔎 Escribe un nombre de medicamento arriba para comenzar la búsqueda.")

# 📈 Información adicional
st.markdown("---")
st.caption("Aplicación demostrativa creada con [Streamlit](https://streamlit.io) — Datos ficticios. Autor: Mónica Stambuk © 2025")
