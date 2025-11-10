import streamlit as st

# ============= CONFIG =============
st.set_page_config(page_title="Compara para ti", page_icon="💊", layout="wide")

# Estado inicial
if "page" not in st.session_state:
    st.session_state["page"] = "home"
if "producto" not in st.session_state:
    st.session_state["producto"] = None
if "categoria" not in st.session_state:
    st.session_state["categoria"] = "Productos destacados"

# ======== DATA DE EJEMPLO (placeholder) ========
CATEGORIAS = ["Analgésicos", "Antibióticos", "Vitaminas", "Respiratorios", "Dermatológicos", "Digestivos", "Cuidado personal"]

PRODUCTOS = [
    {
        "nombre": "Paracetamol 500mg",
        "img": "https://www.laboratoriochile.cl/wp-content/uploads/2015/11/Paracetamol_500MG_16C_BE_HD.jpg",
        "categoria": "Analgésicos",
        "precios": {
            "Cruz Verde": $ 327,
            "Salcobrand": $1.199 "Precio Farmacia"  $1.055 "Precio Internet",
            "Ahumada": 1350
        }
    },
    {
        "nombre": "Ibuprofeno 400mg",
        "img": "https://www.laboratoriochile.cl/wp-content/uploads/2019/03/Ibuprofeno_400MG_20C_BE_HD.jpg",
        "categoria": "Analgésicos",
        "precios": {
            "Cruz Verde": 1850,
            "Salcobrand": 1790,
            "Ahumada": 1920
        }
    },
    {
        "nombre": "Amoxicilina 500mg",
        "img": "https://product-img.cofar.cl/products/2RSESMdiRTtNZnTBG/images/2.webp",
        "categoria": "Antibióticos",
        "precios": {
            "Cruz Verde": 3890,
            "Salcobrand": 3550,
            "Ahumada": 3990
        }
    },
    {
        "nombre": "Vitamina C 1g",
        "img": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT79-M0LnW1j69HsjvaOQrVnrD41dNlTBV_ng&s",
        "categoria": "Vitaminas",
        "precios": {
                "Cruz Verde": 2490,
                "Salcobrand": 2290,
                "Ahumada": 2590
        }
    },
]

ICON_INSTAGRAM = "https://cdn-icons-png.flaticon.com/512/2111/2111463.png"
ICON_TIKTOK    = "https://cdn-icons-png.flaticon.com/512/3046/3046122.png"
ICON_EMAIL     = "https://cdn-icons-png.flaticon.com/512/732/732200.png"
LOGO_URL       = "https://upload.wikimedia.org/wikipedia/commons/7/7d/Medical_icon.png"

# ============= ESTILOS (CSS) =============
st.markdown("""
<style>
/* Contenedor general para compensar el footer fijo */
.main > div { padding-bottom: 90px; }

/* Topbar sticky */
.topbar {
  position: sticky; top: 0; z-index: 999;
  background: #ffffff; border-bottom: 1px solid #eee;
  padding: 8px 12px;
}

/* Distribución topbar */
.topbar-grid {
  display: grid; grid-template-columns: 40px 1fr 40px; align-items: center;
}

/* Logo centrado */
.topbar-logo { text-align: center; font-weight: 700; color: #0b7a6b; }

/* Iconos */
.icon-btn {
  border: 1px solid #eee; border-radius: 8px;
  padding: 6px 0; text-align: center; cursor: pointer;
  user-select: none;
}

/* Carrusel categorías */
.cat-strip {
  display: flex; overflow-x: auto; gap: 12px; padding: 8px 4px 6px 4px; margin-bottom: 10px;
}
.cat-chip {
  white-space: nowrap; border: 1px solid #ddd; border-radius: 20px;
  padding: 6px 12px; font-size: 14px; background: #fff; cursor: pointer;
}
.cat-chip.active { background: #0b7a6b; color: #fff; border-color: #0b7a6b; }

/* Grilla de productos */
.grid {
  display: grid; grid-template-columns: repeat(auto-fill, minmax(220px, 1fr)); gap: 16px;
}
.card {
  border: 1px solid #eee; border-radius: 10px; padding: 10px; background: #fff;
}
.card img { width: 100%; height: 140px; object-fit: cover; border-radius: 8px; }
.card-title { font-weight: 600; margin-top: 8px; }
.card-btn {
  width: 100%; margin-top: 8px; background: #0b7a6b; color: #fff;
  border: none; border-radius: 8px; padding: 8px; cursor: pointer;
}

/* Sección precios */
.price-box { border: 1px solid #eee; border-radius: 10px; padding: 12px; background: #fafafa; }

/* Footer fijo */
.footer {
  position: fixed; bottom: 0; left: 0; right: 0; z-index: 999;
  border-top: 1px solid #eee; background: #ffffff;
}
.footer-inner {
  display: flex; justify-content: center; align-items: center;
  gap: 20px; padding: 10px 0;
}
.footer-inner img { width: 26px; height: 26px; }
.footer-note { text-align: center; font-size: 12px; color: #777; margin-bottom: 6px; }
</style>
""", unsafe_allow_html=True)

# ============= COMPONENTES UI =============
def topbar():
    st.markdown("<div class='topbar'>", unsafe_allow_html=True)
    cols = st.columns([0.07, 0.86, 0.07])
    with cols[0]:
        if st.button("🔍", help="Buscar (placeholder)", key="btn_search"):
            pass  # TODO: acción de búsqueda
    with cols[1]:
        st.markdown(f"<div class='topbar-logo'><img src='{LOGO_URL}' width='28' style='vertical-align:middle;margin-right:8px;'/>Comparador de Farmacias</div>", unsafe_allow_html=True)
    with cols[2]:
        if st.button("☰", help="Opciones", key="btn_menu"):
            st.session_state["page"] = "menu"
    st.markdown("</div>", unsafe_allow_html=True)

def footer():
    st.markdown("""
    <div class='footer'>
      <div class='footer-inner'>
        <img src='""" + ICON_INSTAGRAM + """' alt='Instagram'/>
        <img src='""" + ICON_TIKTOK + """' alt='TikTok'/>
        <img src='""" + ICON_EMAIL + """' alt='Email'/>
      </div>
      <div class='footer-note'>© 2025 Comparador de Farmacias Chile — Íconos solo ilustrativos</div>
    </div>
    """, unsafe_allow_html=True)

def strip_categorias():
    st.markdown("<div class='cat-strip'>", unsafe_allow_html=True)
    # Render chips como botones en columnas fluidas (simples y robustos)
    chip_cols = st.columns(len(CATEGORIAS))
    for i, cat in enumerate(CATEGORIAS):
        with chip_cols[i]:
            active = (cat == st.session_state["categoria"])
            label = f"● {cat}" if active else cat
            if st.button(label, key=f"chip_{cat}"):
                st.session_state["categoria"] = cat
    st.markdown("</div>", unsafe_allow_html=True)

def grid_productos(items):
    st.markdown("<div class='grid'>", unsafe_allow_html=True)
    # Hacemos filas a mano con columns para compatibilidad Streamlit
    # chunk de 4 por fila
    for i in range(0, len(items), 4):
        row = items[i:i+4]
        cols = st.columns(len(row))
        for j, p in enumerate(row):
            with cols[j]:
                st.markdown("<div class='card'>", unsafe_allow_html=True)
                st.image(p["img"])
                st.markdown(f"<div class='card-title'>{p['nombre']}</div>", unsafe_allow_html=True)
                if st.button("Ver detalle", key=f"ver_{p['nombre']}"):
                    st.session_state["producto"] = p["nombre"]
                    st.session_state["page"] = "detalle"
                st.markdown("</div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

def productos_filtrados_por_categoria():
    if st.session_state["categoria"] == "Destacados":
        return PRODUCTOS
    return [p for p in PRODUCTOS if p["categoria"] == st.session_state["categoria"]]

# ============= PÁGINAS =============
def page_home():
    topbar()
    # Carrusel / tira de categorías
    st.subheader("Categorías")
    strip_categorias()

    st.subheader("Productos más relevantes")
    items = productos_filtrados_por_categoria()
    if not items:
        st.info("No hay productos en esta categoría (datos de ejemplo).")
    else:
        grid_productos(items)

    footer()

def page_detalle():
    topbar()
    nombre = st.session_state.get("producto") or "Medicamento"
    prod = next((p for p in PRODUCTOS if p["nombre"] == nombre), None)

    st.subheader(nombre)
    # Imagen + precios
    cols = st.columns([1, 1])
    with cols[0]:
        st.image(prod["img"] if prod else "https://via.placeholder.com/300x200.png?text=Medicamento", caption="Imagen del medicamento")
    with cols[1]:
        st.markdown("### Precio y disponibilidad")
        st.markdown("<div class='price-box'>", unsafe_allow_html=True)
        if prod:
            precios = prod["precios"]
            menor = min(precios.values())
            for farmacia, precio in precios.items():
                badge = " (más barato)" if precio == menor else ""
                st.write(f"- **{farmacia}:** ${precio:,}{badge}")
        else:
            st.write("- # Acá poner precios por farmacia")
        st.markdown("</div>", unsafe_allow_html=True)

        st.markdown("**Descuentos / Promos**")
        st.caption("# Acá poner texto: Ej. 2x1, 20% con Bank X, Club Y, etc. (ficticio)")

    st.markdown("---")
    st.subheader("Productos relacionados")
    relacionados = [p for p in PRODUCTOS if p["nombre"] != nombre][:4]
    grid_productos(relacionados)

    footer()

def page_menu():
    topbar()
    st.subheader("Opciones")
    st.write("- # Acá poner texto: Favoritos")
    st.write("- # Acá poner texto: Historial")
    st.write("- # Acá poner texto: Contacto")
    if st.button("Volver al inicio ⬅️"):
        st.session_state["page"] = "home"
    footer()

# ============= ROUTER =============
if st.session_state["page"] == "home":
    page_home()
elif st.session_state["page"] == "detalle":
    page_detalle()
else:
    page_menu()
