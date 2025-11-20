import streamlit as st

st.set_page_config(page_title="Compara", page_icon="💊", layout="wide")

# ===== ESTADO =====
if "page" not in st.session_state: st.session_state["page"] = "home"
if "producto" not in st.session_state: st.session_state["producto"] = None
if "categoria" not in st.session_state: st.session_state["categoria"] = "Todos"
if "favoritos" not in st.session_state: st.session_state["favoritos"] = []

# ===== DATOS =====
CATEGORIAS = ["Todos", "Analgésicos", "Antibióticos", "Vitaminas",
              "Respiratorios", "Dermatológicos", "Digestivos", "Cuidado personal"]

PRODUCTOS = [
    {"nombre": "Paracetamol", "img": "https://www.laboratoriochile.cl/wp-content/uploads/2015/11/Paracetamol_500MG_16C_BE_HD.jpg",
     "categoria": "Analgésicos", "precios": {"Cruz Verde": 327, "Salcobrand": 1055, "Ahumada": 790}},
    {"nombre": "Ibuprofeno 400mg", "img": "https://www.laboratoriochile.cl/wp-content/uploads/2019/03/Ibuprofeno_400MG_20C_BE_HD.jpg",
     "categoria": "Analgésicos", "precios": {"Cruz Verde": 1850, "Salcobrand": 1055, "Ahumada": 1920}},
    {"nombre": "Amoxicilina 500mg", "img": "https://product-img.cofar.cl/products/2RSESMdiRTtNZnTBG/images/2.webp",
     "categoria": "Antibióticos", "precios": {"Cruz Verde": 3890, "Salcobrand": 3550, "Ahumada": 3990}},
    {"nombre": "Vitamina C 1g", "img": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT79-M0LnW1j69HsjvaOQrVnrD41dNlTBV_ng&s",
     "categoria": "Vitaminas", "precios": {"Cruz Verde": 2490, "Salcobrand": 2290, "Ahumada": 2590}},
    {"nombre": "Salbutamol 0.5%", "img": "https://farmacia.araucomed.com/8205-large_default/salbutamol-solucion-5mg-ml-x20ml-ethon.jpg",
     "categoria": "Respiratorios", "precios": {"Cruz Verde": 11781, "Salcobrand": 11351, "Ahumada": 13199}},
    {"nombre": "Brexotide LF", "img": "https://www.farmaciasahumada.cl/on/demandware.static/-/Sites-ahumada-master-catalog/default/dw82bc8424/images/products/60146/60146.jpg",
     "categoria": "Respiratorios", "precios": {"Cruz Verde": 38538, "Salcobrand": 52711, "Ahumada": 38726}},
    {"nombre": "Clavam Duo", "img": "https://farmex.cl/cdn/shop/products/clavam-duo-875-mg-x-14-comprimidos-eurofarma-941356.jpg?v=1692989657",
     "categoria": "Antibióticos", "precios": {"Cruz Verde": 21825, "Salcobrand": 21334, "Ahumada": 21559}},
    {"nombre": "Up Omega 3", "img": "https://static.salcobrandonline.cl/spree/products/147184/large_webp/575894.webp?1749560150",
     "categoria": "Vitaminas", "precios": {"Cruz Verde": 21825, "Salcobrand": 39999, "Ahumada": 40589}},
    {"nombre": "Tetralysal", "img": "https://beta.cruzverde.cl/on/demandware.static/-/Sites-masterCatalog_Chile/default/dwff3b20e8/images/large/263025-tetralysal-capsula-28-unidades-limeciclina-300-mg.jpg",
     "categoria": "Dermatológicos", "precios": {"Cruz Verde": 42471, "Salcobrand": 49999, "Ahumada": 40589}},
    {"nombre": "Prozone Gel", "img": "https://beta.cruzverde.cl/on/demandware.static/-/Sites-masterCatalog_Chile/default/dwad1227f9/images/large/565638-prozone-gel-fotoprotector-fps-30-100-gr.jpg",
     "categoria": "Dermatológicos", "precios": {"Cruz Verde": 16050, "Salcobrand": 19999, "Ahumada": 17589}},
]

# ===== CSS =====
st.markdown("""
<style>
.topbar{
    position:sticky;
    top:0;
    z-index:1000;
    background:#fff;
    border-bottom:3px solid #aaa;
    padding:40px 0; 
    text-align:center;
}

.topbar button{
    font-size:48px !important;   
    font-weight:900 !important; 
    padding:28px 50px !important;
    border-radius:14px !important;
}

.card{border:1px solid #eee;border-radius:10px;padding:10px;margin-bottom:16px;background:#fff;}
.card img{width:100%;height:140px;object-fit:cover;border-radius:8px;}
.detalle-img{width:300px;height:300px;object-fit:contain;margin:auto;}

.footer{position:fixed;bottom:0;left:0;right:0;background:#fff;border-top:1px solid #eee;}
.footer-inner{display:flex;justify-content:center;gap:20px;padding:10px 0;}
.footer-inner img{width:26px;}
</style>
""", unsafe_allow_html=True)

# ===== TOPBAR =====
def topbar():
    st.markdown("<div class='topbar'>", unsafe_allow_html=True)
    c1, c2 = st.columns([0.90, 0.10])

    with c1:
        if st.button("🏥  COMPARADOR DE FARMACIAS", key="homebanner"):
            st.session_state["page"] = "home"; st.session_state["producto"] = None

    with c2:
        if st.button("☰", key="menu_btn"):
            st.session_state["page"] = "menu"

    st.markdown("</div>", unsafe_allow_html=True)

# ===== FOOTER =====
def footer():
    st.markdown("""
    <div class='footer'>
        <div class='footer-inner'>
            <img src='https://cdn-icons-png.flaticon.com/512/2111/2111463.png'/>
            <img src='https://cdn-icons-png.flaticon.com/512/3046/3046122.png'/>
            <img src='https://cdn-icons-png.flaticon.com/512/732/732200.png'/>
        </div>
    </div>
    """, unsafe_allow_html=True)

# ===== GRID =====
def grid_productos(items):
    cols = st.columns(4)
    idx = 0
    for p in items:
        with cols[idx % 4]:
            st.markdown("<div class='card'>", unsafe_allow_html=True)
            st.image(p["img"])
            st.write(f"**{p['nombre']}**")

            c1, c2 = st.columns([0.7, 0.3])
            with c1:
                if st.button("Ver detalle", key=f"det_{p['nombre']}"):
                    st.session_state["producto"] = p["nombre"]; st.session_state["page"] = "detalle"
            with c2:
                isfav = p["nombre"] in st.session_state["favoritos"]
                if st.button("💔" if isfav else "❤️", key=f"fav_{p['nombre']}"):
                    if isfav: st.session_state["favoritos"].remove(p["nombre"])
                    else: st.session_state["favoritos"].append(p["nombre"])

            st.markdown("</div>", unsafe_allow_html=True)
        idx += 1

# ===== DETALLE =====
def page_detalle():
    topbar()
    prod = next(p for p in PRODUCTOS if p["nombre"] == st.session_state["producto"])

    st.title(prod["nombre"])
    st.markdown(f"<img class='detalle-img' src='{prod['img']}'>", unsafe_allow_html=True)

    precios = prod["precios"]
    menor = min(precios.values())
    for f, p in precios.items():
        st.write(f"• **{f}:** ${p:,}" + (" (más barato)" if p == menor else ""))

    st.write("### Relacionados")
    rel = [p for p in PRODUCTOS if p["categoria"] == prod["categoria"] and p["nombre"] != prod["nombre"]][:4]
    grid_productos(rel)
    footer()

# ===== MENU =====
def page_menu():
    topbar()
    if st.button("❤️ Favoritos"): st.session_state["page"] = "favoritos"
    if st.button("Volver"): st.session_state["page"] = "home"
    footer()

# ===== FAVORITOS =====
def page_favoritos():
    topbar()
    favs = [p for p in PRODUCTOS if p["nombre"] in st.session_state["favoritos"]]
    grid_productos(favs)
    footer()

# ===== BUSCADOR =====
def filtro_busqueda(lista):
    q = st.text_input("🔎 Buscar...", "")
    return [p for p in lista if q.lower() in p["nombre"].lower()]

# ===== ROUTER =====
if st.session_state["page"] == "home":
    topbar()
    st.write("### Categorías")
    st.session_state["categoria"] = st.radio("", CATEGORIAS, horizontal=True)

    prods = [p for p in PRODUCTOS if st.session_state["categoria"] == "Todos"
             or p["categoria"] == st.session_state["categoria"]]

    filtrados = filtro_busqueda(prods)

    st.write("### Productos")
    grid_productos(filtrados)
    footer()

elif st.session_state["page"] == "detalle": page_detalle()
elif st.session_state["page"] == "favoritos": page_favoritos()
else: page_menu()