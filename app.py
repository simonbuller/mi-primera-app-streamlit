import streamlit as st  
# Importamos la librería Streamlit.
# Esta librería permite crear aplicaciones web interactivas usando solamente Python.
# Toda la estructura de la aplicación (botones, textos, imágenes, etc.) se construye con funciones de Streamlit.


# ======================================================================
# CONFIGURACIÓN GLOBAL DE LA APLICACIÓN
# ======================================================================
# Esta configuración se aplica una sola vez al inicio de la app.
# Define:
# - El título que se ve en la pestaña del navegador.
# - El ícono de la pestaña.
# - El tipo de layout (wide = usa todo el ancho de la pantalla).
st.set_page_config(page_title="Compara", page_icon="💊", layout="wide")



# ======================================================================
# MANEJO DEL ESTADO GLOBAL CON st.session_state
# ======================================================================
# Streamlit ejecuta este archivo de arriba hacia abajo cada vez que
# el usuario realiza una acción (clic, escribir, etc.).
# Para que la aplicación "recuerde" qué página está mostrando,
# qué producto está seleccionado o qué favoritos marcó el usuario,
# usamos st.session_state como una memoria de la sesión.

# st.session_state["page"]:
# Representa la pantalla actual de la aplicación.
# Puede tomar valores como "home", "detalle", "menu" o "favoritos".
if "page" not in st.session_state:
    st.session_state["page"] = "home"   # Por defecto, la app parte en la página principal.

# st.session_state["producto"]:
# Guarda el NOMBRE del producto que el usuario seleccionó para ver el detalle.
# Si está en None, significa que aún no hay un producto seleccionado.
if "producto" not in st.session_state:
    st.session_state["producto"] = None

# st.session_state["categoria"]:
# Guarda la categoría que el usuario seleccionó en el control de categorías.
# Se usa para filtrar qué productos se muestran en la pantalla principal.
if "categoria" not in st.session_state:
    st.session_state["categoria"] = "Todos"

# st.session_state["favoritos"]:
# Es una lista que contiene los nombres de los productos que el usuario
# ha marcado con el corazón (❤️). Se usa para mostrar la pantalla de favoritos.
if "favoritos" not in st.session_state:
    st.session_state["favoritos"] = []



# ======================================================================
# DEFINICIÓN DE LA "BASE DE DATOS" DE LA APP
# ======================================================================
# En este proyecto no usamos una base de datos externa ni una API.
# En su lugar, definimos manualmente los datos en estructuras de Python.
# Esto es suficiente para una demo de aplicación.

# CATEGORIAS:
# Lista con las etiquetas de categorías disponibles.
# "Todos" es una categoría especial que muestra todos los productos.
CATEGORIAS = [
    "Todos",
    "Analgésicos",
    "Antibióticos",
    "Vitaminas",
    "Respiratorios",
    "Dermatológicos",
    "Digestivos"
]

# PRODUCTOS:
# Lista de diccionarios, donde cada diccionario representa un medicamento.
# Cada producto tiene:
# - "nombre": nombre del medicamento
# - "img": URL de una imagen del medicamento
# - "categoria": alguna de las categorías definidas arriba
# - "precios": diccionario con precios en distintas farmacias
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
        "precios": {"Cruz Verde": 1850, "Salcobrand": 1055, "Ahumada": 1920}
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
        "nombre": "Salbutamol 0.5%",
        "img": "https://farmacia.araucomed.com/8205-large_default/salbutamol-solucion-5mg-ml-x20ml-ethon.jpg",
        "categoria": "Respiratorios",
        "precios": {"Cruz Verde": 11781, "Salcobrand": 11351, "Ahumada": 13199}
    },
    {
        "nombre": "Brexotide LF",
        "img": "https://www.farmaciasahumada.cl/on/demandware.static/-/Sites-ahumada-master-catalog/default/dw82bc8424/images/products/60146/60146.jpg",
        "categoria": "Respiratorios",
        "precios": {"Cruz Verde": 38538, "Salcobrand": 52711, "Ahumada": 38726}
    },
    {
        "nombre": "Clavam Duo",
        "img": "https://farmex.cl/cdn/shop/products/clavam-duo-875-mg-x-14-comprimidos-eurofarma-941356.jpg?v=1692989657",
        "categoria": "Antibióticos",
        "precios": {"Cruz Verde": 21825, "Salcobrand": 21334, "Ahumada": 21559}
    },
    {
        "nombre": "Up Omega 3",
        "img": "https://static.salcobrandonline.cl/spree/products/147184/large_webp/575894.webp?1749560150",
        "categoria": "Vitaminas",
        "precios": {"Cruz Verde": 21825, "Salcobrand": 39999, "Ahumada": 40589}
    },
    {
        "nombre": "Tetralysal",
        "img": "https://beta.cruzverde.cl/on/demandware.static/-/Sites-masterCatalog_Chile/default/dwff3b20e8/images/large/263025-tetralysal-capsula-28-unidades-limeciclina-300-mg.jpg",
        "categoria": "Dermatológicos",
        "precios": {"Cruz Verde": 42471, "Salcobrand": 49999, "Ahumada": 40589}
    },
    {
        "nombre": "Prozone Gel",
        "img": "https://beta.cruzverde.cl/on/demandware.static/-/Sites-masterCatalog_Chile/default/dwad1227f9/images/large/565638-prozone-gel-fotoprotector-fps-30-100-gr.jpg",
        "categoria": "Dermatológicos",
        "precios": {"Cruz Verde": 16050, "Salcobrand": 19999, "Ahumada": 17589}
    }
]



# ======================================================================
# CSS PERSONALIZADO PARA LA INTERFAZ
# ======================================================================
# Aquí incluimos estilos CSS para mejorar la apariencia de la app.
# Esto afecta:
# - La barra superior (topbar)
# - Las tarjetas de productos (card)
# - La imagen de detalle
# - El footer inferior
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
.card{
    border:1px solid #eee;
    border-radius:10px;
    padding:10px;
    margin-bottom:16px;
    background:#fff;
}
.card img{
    width:100%;
    height:140px;
    object-fit:cover;
    border-radius:8px;
}
.detalle-img{
    width:300px;
    height:300px;
    object-fit:contain;
    margin:auto;
}
.footer{
    position:fixed;
    bottom:0;
    left:0;
    right:0;
    background:#fff;
    border-top:1px solid #eee;
}
.footer-inner{
    display:flex;
    justify-content:center;
    gap:20px;
    padding:10px 0;
}
.footer-inner img{
    width:26px;
}
</style>
""", unsafe_allow_html=True)



# ======================================================================
# FUNCIÓN: topbar()  → Barra superior de navegación
# ======================================================================
def topbar():
    """
    Esta función dibuja la barra superior fija (topbar) en la app.
    Contiene dos elementos interactivos:
    - Un botón grande con el nombre de la app: "🏥 COMPARADOR DE FARMACIAS".
    - Un botón de menú "☰".
    
    ¿Qué pasa cuando el usuario hace clic?
    - Al apretar el botón principal:
      · Se cambia la página actual a "home".
      · Se limpia el producto seleccionado, por si estaba en la vista de detalle.
    - Al apretar el botón "☰":
      · Se cambia la página actual a "menu".
      · Luego el router, al final del archivo, mostrará page_menu().
    """

    # Abrimos el contenedor HTML de la barra superior.
    st.markdown("<div class='topbar'>", unsafe_allow_html=True)

    # Creamos dos columnas: una con 90% del espacio y otra con 10%.
    c1, c2 = st.columns([0.90, 0.10])

    # Columna de la izquierda: botón principal de la app.
    with c1:
        # Este botón sirve como "logo clicable".
        if st.button("🏥  COMPARADOR DE FARMACIAS", key="homebanner"):
            # Al apretar este botón:
            # 1) Mandamos al usuario a la página home.
            st.session_state["page"] = "home"
            # 2) Reseteamos el producto seleccionado (por si estaba en detalle).
            st.session_state["producto"] = None

    # Columna de la derecha: botón de menú.
    with c2:
        if st.button("☰", key="menu_btn"):
            # Al apretar este botón:
            # Solo cambiamos la página a "menu".
            # El router se encargará de llamar a page_menu().
            st.session_state["page"] = "menu"

    # Cerramos el contenedor de la barra superior.
    st.markdown("</div>", unsafe_allow_html=True)



# ======================================================================
# FUNCIÓN: footer()  → Barra inferior fija
# ======================================================================
def footer():
    """
    Esta función dibuja el footer (barra inferior) fijo en la aplicación.
    Muestra simplemente tres íconos a modo decorativo.
    No hay lógica ni acciones del usuario asociadas a estos íconos en esta demo.
    """
    st.markdown("""
    <div class='footer'>
        <div class='footer-inner'>
            <img src='https://cdn-icons-png.flaticon.com/512/2111/2111463.png'/>
            <img src='https://cdn-icons-png.flaticon.com/512/3046/3046122.png'/>
            <img src='https://cdn-icons-png.flaticon.com/512/732/732200.png'/>
        </div>
    </div>
    """, unsafe_allow_html=True)



# ======================================================================
# FUNCIÓN: grid_productos(items)  → Grilla de productos
# ======================================================================
def grid_productos(items):
    """
    Esta función recibe una lista de productos (items) y se encarga de mostrarlos
    en formato de grilla, de 4 columnas por fila.

    Para cada producto muestra:
    - La imagen del medicamento.
    - El nombre en negrita.
    - Un botón "Ver detalle".
    - Un botón con un corazón (❤️ o 💔) para agregar o quitar de favoritos.

    Acciones clave que ocurren aquí:
    --------------------------------
    1. Cuando el usuario presiona "Ver detalle":
       - Se guarda el nombre del producto seleccionado en st.session_state["producto"].
       - Se cambia st.session_state["page"] a "detalle".
       - Eso hace que el router, al final del archivo, cargue la pantalla de detalle.

    2. Cuando el usuario presiona el corazón:
       - Si el producto YA está en favoritos, se elimina de la lista.
       - Si NO está en favoritos, se agrega.
       - La lista se guarda en st.session_state["favoritos"].
    """

    # Creamos cuatro columnas donde iremos distribuyendo las cards.
    cols = st.columns(4)

    # Recorremos la lista de productos, con enumerate para tener un índice 'i'.
    for i, p in enumerate(items):
        # Usamos i % 4 para ir repartiéndolos de forma circular entre las 4 columnas.
        with cols[i % 4]:
            # Abrimos una "card" usando HTML para aplicar nuestros estilos CSS.
            st.markdown("<div class='card'>", unsafe_allow_html=True)

            # Mostramos la imagen del producto.
            st.image(p["img"])

            # Mostramos el nombre del producto en negrita.
            st.write(f"**{p['nombre']}**")

            # Creamos una fila interna dentro de la card: una columna para "Ver detalle"
            # y otra para el corazón de favoritos.
            c1, c2 = st.columns([0.7, 0.3])

            # ------------------------------------------------
            # BOTÓN "Ver detalle"
            # ------------------------------------------------
            # Este botón sirve para ir a la vista de detalle del producto.
            with c1:
                if st.button("Ver detalle", key=f"det_{i}"):
                    # Cuando el usuario APRETA ESTE BOTÓN:
                    # 1) Guardamos el NOMBRE del producto en session_state["producto"].
                    st.session_state["producto"] = p["nombre"]

                    # 2) Cambiamos la página a "detalle".
                    # Esto dispara que el router llame a page_detalle().
                    st.session_state["page"] = "detalle"

            # ------------------------------------------------
            # BOTÓN "Favorito" (corazón)
            # ------------------------------------------------
            with c2:
                # Primero verificamos si el producto ya está en la lista de favoritos.
                isfav = p["nombre"] in st.session_state["favoritos"]

                # Elegimos qué ícono mostrar según si es favorito o no.
                # 💔 si ya es favorito (para indicar que al apretar lo quita).
                # ❤️ si no es favorito (para indicar que al apretar lo agrega).
                if st.button("💔" if isfav else "❤️", key=f"fav_{i}"):

                    # Aquí ocurre la acción de AGREGAR o QUITAR de favoritos.
                    if isfav:
                        # Si ya era favorito, se quita el nombre de la lista.
                        st.session_state["favoritos"].remove(p["nombre"])
                    else:
                        # Si no era favorito, se agrega el nombre a la lista.
                        st.session_state["favoritos"].append(p["nombre"])

            # Cerramos la card.
            st.markdown("</div>", unsafe_allow_html=True)



# ======================================================================
# FUNCIÓN: page_detalle()  → Pantalla de detalle del producto
# ======================================================================
def page_detalle():
    """
    Esta función muestra la pantalla de detalle de un producto específico.

    ¿Cómo se llega a esta función?
    - Antes, en grid_productos(), el usuario presiona "Ver detalle".
    - Eso guarda el nombre del producto en st.session_state["producto"]
      y cambia st.session_state["page"] a "detalle".
    - El router, al final del archivo, detecta ese valor y llama a page_detalle().

    ¿Qué muestra esta pantalla?
    - El título con el nombre del medicamento.
    - Una imagen grande del producto.
    - Una lista de precios por farmacia, indicando cuál es el más barato.
    - Una sección de "Productos relacionados" que muestra otros productos
      de la misma categoría.
    """

    # Dibujamos la barra superior.
    topbar()

    # Si por alguna razón no hay producto seleccionado, regresamos al home.
    if not st.session_state["producto"]:
        st.session_state["page"] = "home"
        return

    # Buscamos dentro de PRODUCTOS aquel cuyo nombre coincida con el seleccionado.
    prod = next((p for p in PRODUCTOS if p["nombre"] == st.session_state["producto"]), None)

    # Si no encontramos el producto, también volvemos al home.
    if prod is None:
        st.session_state["page"] = "home"
        return

    # Mostramos el nombre del producto como título principal.
    st.title(prod["nombre"])

    # Mostramos la imagen del producto con la clase CSS 'detalle-img' para controlar su tamaño.
    st.markdown(f"<img class='detalle-img' src='{prod['img']}'>", unsafe_allow_html=True)

    # Obtenemos el diccionario de precios del producto.
    precios = prod["precios"]

    # Calculamos el menor precio de todas las farmacias.
    menor = min(precios.values())

    # Mostramos la lista de precios y marcamos cuál es el más barato.
    for farmacia, precio in precios.items():
        st.write(
            f"• **{farmacia}:** ${precio:,}" +
            (" (más barato)" if precio == menor else "")
        )

    # Ahora definimos los productos relacionados:
    # Son aquellos que pertenecen a la misma categoría,
    # pero excluyendo al producto actual (para no repetirse).
    relacionados = [
        p for p in PRODUCTOS
        if p["categoria"] == prod["categoria"] and p["nombre"] != prod["nombre"]
    ][:4]  # Limitamos a un máximo de 4 productos relacionados.

    st.write("### Relacionados")

    # Reutilizamos la grilla para mostrar los productos relacionados.
    grid_productos(relacionados)

    # Dibujamos el footer.
    footer()



# ======================================================================
# FUNCIÓN: page_menu()  → Pantalla de menú
# ======================================================================
def page_menu():
    """
    Esta función representa una pantalla sencilla de menú.
    Permite moverse a:
    - La sección de favoritos.
    - Volver a la página principal (home).
    """

    topbar()

    # Botón para ir a la página de favoritos.
    if st.button("❤️ Favoritos"):
        # Cuando se aprieta, simplemente cambiamos la página a "favoritos".
        st.session_state["page"] = "favoritos"

    # Botón para volver al inicio.
    if st.button("Volver"):
        st.session_state["page"] = "home"

    footer()



# ======================================================================
# FUNCIÓN: page_favoritos()  → Pantalla de favoritos
# ======================================================================
def page_favoritos():
    """
    Esta pantalla muestra todos los productos que el usuario ha marcado con el corazón.
    Para lograr esto:
    - Miramos st.session_state["favoritos"], que contiene nombres de productos.
    - Filtramos la lista PRODUCTOS usando esa información.
    - Luego reutilizamos grid_productos() para mostrar esos elementos.
    """

    topbar()

    # Filtramos la lista de productos originales para quedarnos
    # solo con aquellos cuyo nombre está en la lista de favoritos.
    favoritos = [
        p for p in PRODUCTOS
        if p["nombre"] in st.session_state["favoritos"]
    ]

    st.write("### Mis Favoritos")

    # Mostramos la grilla de productos favoritos.
    grid_productos(favoritos)

    footer()



# ======================================================================
# FUNCIÓN: filtro_busqueda(lista)  → Buscador por nombre
# ======================================================================
def filtro_busqueda(lista):
    """
    Esta función implementa un buscador simple por nombre de producto.

    - Recibe una lista de productos (por ejemplo, ya filtrados por categoría).
    - Muestra una caja de texto donde el usuario puede escribir.
    - Devuelve solo aquellos productos cuyo nombre contiene el texto escrito.

    Esto permite que el usuario busque algo como "Para", "Amoxi", etc.
    """

    # Mostramos un campo de texto para buscar.
    # Cada vez que el usuario escribe, Streamlit recarga la app y actualiza el valor de 'q'.
    q = st.text_input("🔎 Buscar...", "")

    # Convertimos tanto el nombre del producto como la búsqueda a minúsculas
    # para que la comparación no distinga entre mayúsculas y minúsculas.
    return [p for p in lista if q.lower() in p["nombre"].lower()]



# ======================================================================
# ROUTER PRINCIPAL  → Decide qué pantalla mostrar
# ======================================================================
# Este bloque es el "cerebro de la navegación".
# Siempre revisa el valor de st.session_state["page"] y, según eso,
# llama a una u otra función de página.
#
# La idea es:
# - Cada vez que un botón cambia st.session_state["page"],
#   Streamlit vuelve a ejecutar el script.
# - Al llegar a este punto, el router decide qué mostrar
#   en función del valor actual de "page".
if st.session_state["page"] == "home":
    # Si la página actual es "home", mostramos la pantalla principal.

    topbar()

    st.write("### Categorías")

    # Radio button para seleccionar categoría:
    # Cuando el usuario selecciona una categoría, el valor se guarda
    # automáticamente en st.session_state["categoria"].
    st.session_state["categoria"] = st.radio(
        "", CATEGORIAS, horizontal=True
    )

    # FILTRADO POR CATEGORÍA:
    # Si la categoría es "Todos":
    #   → mostramos todos los productos.
    # Si no:
    #   → mostramos solo los productos cuya "categoria" coincide
    #     con st.session_state["categoria"].
    productos_categoria = [
        p for p in PRODUCTOS
        if st.session_state["categoria"] == "Todos"
        or p["categoria"] == st.session_state["categoria"]
    ]

    # APLICAMOS EL BUSCADOR SOBRE LOS PRODUCTOS FILTRADOS:
    productos_finales = filtro_busqueda(productos_categoria)

    st.write("### Productos")

    # Mostramos la grilla de productos final (filtrados por categoría y búsqueda).
    grid_productos(productos_finales)

    footer()

elif st.session_state["page"] == "detalle":
    # Si la página actual es "detalle", llamamos a la función que muestra
    # el detalle del producto seleccionado.
    page_detalle()

elif st.session_state["page"] == "favoritos":
    # Si la página actual es "favoritos", mostramos esa pantalla.
    page_favoritos()

else:
    # Cualquier otro valor (por ejemplo "menu") llevará a la pantalla de menú.
    page_menu()