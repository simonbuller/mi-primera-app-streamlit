import streamlit as st

# ============= CONFIG =============
st.set_page_config(page_title="Compara para ti", page_icon="💊", layout="wide")

# ============= ESTADO DE LA APP =============
if "page" not in st.session_state:
    st.session_state["page"] = "home"
if "producto" not in st.session_state:
    st.session_state["producto"] = None
if "categoria" not in st.session_state:
    st.session_state["categoria"] = "Todos"
if "favoritos" not in st.session_state:
    st.session_state["favoritos"] = []

# ======== DATOS ========
CATEGORIAS = [
    "Todos", "Analgésicos", "Antibióticos", "Vitaminas",
    "Respiratorios", "Dermatológicos", "Digestivos", "Cuidado personal"
]

PRODUCTOS = [
    {
        "nombre": "Paracetamol",
        "img": "https://www.laboratoriochile.cl/wp-content/uploads/2015/11/Paracetamol_500MG_16C_BE_HD.jpg",
        "categoria": "Analgésicos",
        "precios": {"Cruz Verde": 327, "Salcobrand": 1055, "Ahumada": 790}
    },
    {
        "nombre": "Ibuprofeno 400mg",
        "img": "https://www.laboratoriochile.cl/wp-content/uploads/2019/03/Ibuprofeno_400MG_20C_BE_HD.jpg",
        "categoria": "Analgésicos",
        "precios": {"Cruz Verde": 1850, "Salcobrand": 1.055, "Ahumada": 1920}
    },
    {
        "nombre": "Amoxicilina 500mg",
        "img": "https://product-img.cofar.cl/products/2RSESMdiRTtNZnTBG/images/2.webp",
        "categoria": "Antibióticos",
        "precios": {"Cruz Verde": 3890, "Salcobrand": 3550, "Ahumada": 3990}
    },
    {
        "nombre": "Vitamina C 1g",
        "img": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT79-M0LnW1j69HsjvaOQrVnrD41dNlTBV_ng&s",
        "categoria": "Vitaminas",
        "precios": {"Cruz Verde": 2490, "Salcobrand": 2290, "Ahumada": 2590}
    },
    {
        "nombre": "Salbutamol 0,5% Solución para Nebulización 20 mL",
        "img": "https://farmacia.araucomed.com/8205-large_default/salbutamol-solucion-5mg-ml-x20ml-ethon.jpg",
        "categoria": "Respiratorios",
        "precios": {"Cruz Verde": 11.781, "Salcobrand": 11.351, "Ahumada": 13.199}
    },
    {
        "nombre": "Brexotide LF 125 mcg /25 mcg 120 Dosis Aerosol para Inhalación",
        "img": "https://www.farmaciasahumada.cl/on/demandware.static/-/Sites-ahumada-master-catalog/default/dw82bc8424/images/products/60146/60146.jpg",
        "categoria": "Respiratorios",
        "precios": {"Cruz Verde": 38.538, "Salcobrand": 52.711, "Ahumada": 38.726}
    },
    {
        "nombre": "Clavam Duo Amoxicilina 875 mg 14 Comprimidos Recubierto",
        "img": "https://farmex.cl/cdn/shop/products/clavam-duo-875-mg-x-14-comprimidos-eurofarma-941356.jpg?v=1692989657",
        "categoria": "Antibióticos",
        "precios": {"Cruz Verde": 21.825, "Salcobrand": 21.334, "Ahumada": 21.559}
    },
    {
        "nombre": "Up Omega 3 Ultra Pure 150 Cápsulas Suplemento Alimentario",
        "img": "https://static.salcobrandonline.cl/spree/products/147184/large_webp/575894.webp?1749560150",
        "categoria": "Vitaminas",
        "precios": {"Cruz Verde": 21.825, "Salcobrand": 39.999, "Ahumada": 40.589}
    },
    {
        "nombre": "Tetralysal Limeciclina 300 mg 28 Cápsulas",
        "img": "https://beta.cruzverde.cl/on/demandware.static/-/Sites-masterCatalog_Chile/default/dwff3b20e8/images/large/263025-tetralysal-capsula-28-unidades-limeciclina-300-mg.jpg",
        "categoria": "Dermatológicos",
        "precios": {"Cruz Verde": 42.471, "Salcobrand": 49.999, "Ahumada": 40.589}
    },
    {
        "nombre": "Prozone Gel Fotoprotector FPS30 100 gr",
        "img": "https://beta.cruzverde.cl/on/demandware.static/-/Sites-masterCatalog_Chile/default/dwad1227f9/images/large/565638-prozone-gel-fotoprotector-fps-30-100-gr.jpg",
        "categoria": "Dermatológicos",
        "precios": {"Cruz Verde": 16.050, "Salcobrand": 19.999, "Ahumada": 17.589}
    },
    {
        "nombre": "Metoclopramida 10 mg 24 Comprimidos",
        "img": "https://beta.cruzverde.cl/on/demandware.static/-/Sites-masterCatalog_Chile/default/dw06526206/images/large/268208.1.jpg",
        "categoria": "Digestivos",
        "precios": {"Cruz Verde": 1.791, "Salcobrand": 1.999, "Ahumada": 1.589}
    },
    {
        "nombre": "Domperidona 10 mg 20 comprimidos Genéricos",
        "img": "https://beta.cruzverde.cl/on/demandware.static/-/Sites-masterCatalog_Chile/default/dw6955679e/images/large/272620-domperidona-bioequivalente-comprimido-20-unidades-domperidona-10-mg.jpg",
        "categoria": "Digestivos",
        "precios": {"Cruz Verde": 1.386, "Salcobrand": 1.979, "Ahumada": 1.589}
    },
    {
        "nombre": "Desodorante Spray Stainguard 150 ml",
        "img": "https://beta.cruzverde.cl/on/demandware.static/-/Sites-masterCatalog_Chile/default/dw0dbee912/images/large/289097-desodorante-spray-stainguard-150-ml.jpg",
        "categoria": "Cuidado personal",
        "precios": {"Cruz Verde": 2.890, "Salcobrand": 2.861, "Ahumada": 2.589}
    },
    {
        "nombre": "Enjuague Bucal Cuidado Total 1LT",
        "img": "https://beta.cruzverde.cl/on/demandware.static/-/Sites-masterCatalog_Chile/default/dwe2d7c94d/images/large/578312-1.jpg",
        "categoria": "Cuidado personal",
        "precios": {"Cruz Verde": 7.990, "Salcobrand": 8.861, "Ahumada": 7.879}
    },
]

# ============= CSS =============
st.markdown("""
<style>
.main > div { padding-bottom: 90px; }
.topbar { position: sticky; top: 0; z-index: 1000; background: #fff; border-bottom: 1px solid #eee; padding: 8px; }
.card { 
    border: 1px solid #eee; 
    border-radius: 10px; 
    padding: 10px; 
    background: #fff;
    margin-bottom: 16px;
}
.card img { width: 100%; height: 140px; object-fit: cover; border-radius: 8px; }
.footer { position: fixed; bottom:0; left:0; right:0; background:#fff; border-top:1px solid #eee; }
.footer-inner { display:flex; justify-content:center; gap:20px; padding:10px 0; }
.footer-inner img { width:26px; }
</style>
""", unsafe_allow_html=True)

# ============= TOPBAR =============
def topbar():
    st.markdown("<div class='topbar'>", unsafe_allow_html=True)
    c1, c2, c3 = st.columns([0.1, 0.8, 0.1])

    with c1:
        st.button("🔍")

    with c2:
        if st.button("🏥  Comparador de Farmacias"):
            st.session_state["page"] = "home"
            st.session_state["producto"] = None

    with c3:
        if st.button("☰"):
            st.session_state["page"] = "menu"

    st.markdown("</div>", unsafe_allow_html=True)

# ============= FOOTER =============
def footer():
    st.markdown("""
    <div class='footer'>
        <div class='footer-inner'>
            <img src='https://cdn-icons-png.flaticon.com/512/2111/2111463.png'/>
            <img src='https://cdn-icons-png.flaticon.com/512/3046/3046122.png'/>
            <img src='https://cdn-icons-png.flaticon.com/512/732/732200.png'/>
        </div>
        <div style='text-align:center;font-size:12px;color:#777;'>© 2025 Comparador de Farmacias Chile</div>
    </div>
    """, unsafe_allow_html=True)

# ============= CATEGORÍAS =============
def strip_categorias():
    cat = st.radio(
        "Selecciona una categoría:",
        CATEGORIAS,
        horizontal=True,
        index=CATEGORIAS.index(st.session_state["categoria"])
    )
    st.session_state["categoria"] = cat

# ============= GRID AUTO (Opción D) CON ❤️ =============
def grid_productos(items):
    cols = st.columns(4)  # Streamlit lo ajusta automáticamente según espacio

    idx = 0
    for p in items:
        with cols[idx % 4]:
            st.markdown("<div class='card'>", unsafe_allow_html=True)

            st.image(p["img"])
            st.write(f"**{p['nombre']}**")

            c1, c2 = st.columns([0.7, 0.3])

            with c1:
                if st.button("Ver detalle", key=f"det_{p['nombre']}"):
                    st.session_state["producto"] = p["nombre"]
                    st.session_state["page"] = "detalle"

            with c2:
                is_fav = p["nombre"] in st.session_state["favoritos"]
                label = "💔" if is_fav else "❤️"

                if st.button(label, key=f"fav_{p['nombre']}"):
                    if is_fav:
                        st.session_state["favoritos"].remove(p["nombre"])
                    else:
                        st.session_state["favoritos"].append(p["nombre"])

            st.markdown("</div>", unsafe_allow_html=True)

        idx += 1

# ============= DETALLE DE PRODUCTO CON ❤️ AL LADO DEL PRECIO =============
def page_detalle():
    topbar()

    prod = next(p for p in PRODUCTOS if p["nombre"] == st.session_state["producto"])

    st.title(prod["nombre"])
    st.image(prod["img"])

    # Encabezado de precios + corazón
    cA, cB = st.columns([0.85, 0.15])

    with cA:
        st.write("### Precio y disponibilidad")

    with cB:
        is_fav = prod["nombre"] in st.session_state["favoritos"]
        label = "💔" if is_fav else "❤️"

        if st.button(label, key=f"favdet_{prod['nombre']}"):
            if is_fav:
                st.session_state["favoritos"].remove(prod["nombre"])
            else:
                st.session_state["favoritos"].append(prod["nombre"])

    precios = prod["precios"]
    menor = min(precios.values())

    for farmacia, precio in precios.items():
        barato = " (más barato)" if precio == menor else ""
        st.write(f"• **{farmacia}:** ${precio:,}{barato}")

    st.divider()
    st.write("### Productos relacionados")

    relacionados = [
        p for p in PRODUCTOS
        if p["categoria"] == prod["categoria"] and p["nombre"] != prod["nombre"]
    ][:4]

    grid_productos(relacionados)
    footer()

# ============= FAVORITOS =============
def page_favoritos():
    topbar()
    st.subheader("❤️ Mis favoritos")

    favs = [p for p in PRODUCTOS if p["nombre"] in st.session_state["favoritos"]]

    if not favs:
        st.info("Todavía no has agregado favoritos.")
    else:
        grid_productos(favs)

    footer()

# ============= MENÚ =============
def page_menu():
    topbar()
    st.subheader("Opciones")

    if st.button("❤️ Favoritos"):
        st.session_state["page"] = "favoritos"

    if st.button("📩 Contacto"):
        st.success("Puedes escribirnos a **soporte@comparadorfarmacias.cl**")

    if st.button("Volver al inicio"):
        st.session_state["page"] = "home"

    footer()

# ============= ROUTER =============
if st.session_state["page"] == "home":
    topbar()
    st.subheader("Categorías")
    strip_categorias()

    st.subheader("Productos")
    prods = [
        p for p in PRODUCTOS
        if st.session_state["categoria"] == "Todos"
        or p["categoria"] == st.session_state["categoria"]
    ]

    grid_productos(prods)
    footer()

elif st.session_state["page"] == "detalle":
    page_detalle()

elif st.session_state["page"] == "favoritos":
    page_favoritos()

else:
    page_menu()