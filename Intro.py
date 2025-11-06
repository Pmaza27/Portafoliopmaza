import streamlit as st

# --- Configuración de la Página ---
st.set_page_config(
    page_title="Portafolio IA",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- CSS Personalizado para Tema Oscuro Moderno y Tarjetas ---
custom_css = """
<style>
/* 1. Estilo General - Tema Oscuro Minimalista */
.stApp {
    background-color: #1e1e1e; /* Fondo oscuro */
    color: #f0f0f0; /* Texto claro */
}

/* 2. Encabezado Principal */
h1 {
    color: #4CAF50; /* Color de acento para el título principal */
    text-align: center;
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    font-weight: 700;
    padding-bottom: 20px;
    border-bottom: 2px solid #333333;
}

/* 3. Estilo de la Tarjeta de Aplicación (El corazón del diseño) */
.app-card {
    background-color: #2c2c2c; /* Fondo de la tarjeta un poco más claro que el fondo principal */
    border-radius: 12px; /* Bordes redondeados */
    padding: 20px;
    margin-bottom: 20px;
    box-shadow: 0 4px 10px rgba(0, 0, 0, 0.5); /* Sombra sutil */
    transition: all 0.3s ease-in-out; /* Transición para el efecto hover */
    height: 100%; /* Asegura que todas las tarjetas sean del mismo tamaño verticalmente */
    display: flex;
    flex-direction: column;
}

/* Efecto Hover para la Tarjeta */
.app-card:hover {
    transform: translateY(-5px); /* Animación ligera al pasar el mouse */
    box-shadow: 0 8px 20px rgba(0, 0, 0, 0.7); /* Sombra más pronunciada al hacer hover */
    border: 1px solid #4CAF50; /* Borde de acento */
}

/* Estilo para la imagen dentro de la tarjeta */
.app-card img {
    border-radius: 8px;
    margin-bottom: 15px;
    height: 150px; /* Altura fija para la imagen */
    object-fit: cover; /* Ajuste para cubrir el área sin deformar */
}

/* Estilo para el botón dentro de la tarjeta */
.stButton>button {
    width: 100%;
    border-radius: 8px;
    background-color: #4CAF50;
    color: white;
    font-weight: bold;
    margin-top: auto; /* Empuja el botón hacia la parte inferior de la tarjeta */
}

/* 4. Estilo de la Barra Lateral */
.stSidebar {
    background-color: #121212 !important; /* Sidebar más oscuro */
    border-right: 1px solid #333333;
    padding: 20px;
}

/* 5. Footer Discreto */
.footer {
    position: fixed;
    left: 0;
    bottom: 0;
    width: 100%;
    background-color: #1e1e1e;
    color: #555555;
    text-align: center;
    padding: 10px;
    font-size: 0.8em;
    border-top: 1px solid #333333;
}
</style>
"""
st.markdown(custom_css, unsafe_allow_html=True)


# --- 📌 Definición de las Aplicaciones ---
# Usamos un diccionario para mantener la información limpia y escalable
APPLICATIONS = [
    {
        "title": "Intro",
        "icon": "👀",
        "description": "Primera app.",
        "image": "images/text_to_speech.png",
        "link": "https://intropmaza.streamlit.app/"
    },
    {
        "title": "Conversión de Texto a Voz (TTS)",
        "icon": "🎙️",
        "description": "Transforma cualquier texto escrito en un audio de voz natural y realista.",
        "image": "images/text_to_speech.png",
        "link": "https://texttoaudiopjmu.streamlit.app/"
    },
    {
        "title": "Conversión de Voz a Texto (STT)",
        "icon": "📝",
        "description": "Convierte archivos de audio o voz en tiempo real a texto editable con alta precisión.",
        "image": "images/speech_to_text.png",
        "link": "https://traductorpjmu.streamlit.app/"
    },
    {
        "title": "Interfaz OCR",
        "icon": "📹",
        "description": "Digitaliza documentos e imágenes instantáneamente. Esta aplicación utiliza visión por computadora y modelos de IA para extraer texto editable de cualquier imagen o PDF con precisión. Ideal para automatizar la entrada de datos y convertir archivos estáticos en información dinámica.",
        "image": "images/object_recognition.png",
        "link": "https://ficticio.app/objetos"
    },
    {
        "title": "Análisis de Sentimiento",
        "icon": "📊",
        "description": "Descubre patrones ocultos y genera visualizaciones interactivas a partir de tus datasets.",
        "image": "images/data_analysis.png",
        "link": "https://ficticio.app/analisis"
    },
    {
        "title": "Analisis de texto inglés)",
        "icon": "📚",
        "description": ".",
        "image": "images/rag.png",
        "link": "https://ficticio.app/rag"
    },
    {
        "title": "Analisis de texto español",
        "icon": "🎬",
        "description": ".",
        "image": "images/video_audio_transcriber.png",
        "link": "https://ficticio.app/transcriptor"
    },
    {
        "title": "Reconocimiento de gestos (Yolo",
        "icon": "🖼️",
        "description": "Clasifica, segmenta y extrae información valiosa de cualquier archivo de imagen.",
        "image": "images/image_analysis.png",
        "link": "https://ficticio.app/analisis_img"
    },
    {
        "title": "Reconocimiento de objetos",
        "icon": "🧠",
        "description": "",
        "image": "images/model_training.png",
        "link": "https://ficticio.app/entrenamiento"
    },
    {
        "title": "Chat PDF",
        "icon": "🏭",
        "description": ".",
        "image": "images/cyberphysical_system.png",
        "link": "https://ficticio.app/cps"
    },   
    {
        "title": "Imagen to text",
        "icon": "🏭",
        "description": ".",
        "image": "images/cyberphysical_system.png",
        "link": "https://imgtotextpmu.streamlit.app/"
    },
    {
        "title": "Reconomiento de Tablero ",
        "icon": "🏭",
        "description": ".",
        "image": "images/cyberphysical_system.png",
        "link": "https://tableropjmu.streamlit.app/"
    },
    {
        "title": "Apliación Tablero ",
        "icon": "🏭",
        "description": ".",
        "image": "images/cyberphysical_system.png",
        "link": "https://tablerointeligente-w9afexj9dbqdpqf92qef7m.streamlit.app/"
    },  
    {
        "title": "Control MQTT ",
        "icon": "🏭",
        "description": ".",
        "image": "images/cyberphysical_system.png",
        "link": "https://ficticio.app/cps"
    }, 
    {
        "title": "Control Voz MQTT ",
        "icon": "🎙️",
        "description": ".",
        "image": "images/cyberphysical_system.png",
        "link": "https://ctrlvoicepmaza.streamlit.app/"
    }
    
]


# --- 💡 Menú Lateral (Sidebar) ---
with st.sidebar:
    st.image("https://upload.wikimedia.org/wikipedia/commons/e/e0/Ai_icon.svg", width=150) # Icono de IA (usando URL pública como ejemplo)
    st.markdown("---")
    st.subheader("🤖 ¿Qué es la Inteligencia Artificial?")
    st.markdown("""
        La **Inteligencia Artificial (IA)** es un campo de la informática que se enfoca en crear **sistemas capaces de razonar, aprender y actuar** de forma autónoma.
        
        Implica la construcción de **algoritmos** y modelos que permiten a las máquinas realizar tareas que normalmente requieren inteligencia humana, desde el reconocimiento de patrones hasta la toma de decisiones complejas.
        
        Explora nuestro catálogo de aplicaciones basadas en IA.
    """)
    st.markdown("---")
    st.info("💡 **Tip:** Usa `st.columns` para una disposición visualmente atractiva.")


# --- 🌐 Contenido Principal ---

st.title("Aplicaciones de Inteligencia Artificial")

# 1. Función para crear la tarjeta de aplicación
def create_app_card(app):
    """Crea una tarjeta de aplicación con la estructura HTML/CSS personalizada."""
    # Usamos st.markdown para inyectar la estructura HTML de la tarjeta
    card_html = f"""
    <div class="app-card">
        <img src="{app['image']}" alt="{app['title']}" />
        <h3 style="color: #f0f0f0; margin-top: 0px;">{app['icon']} {app['title']}</h3>
        <p style="color: #cccccc;">{app['description']}</p>
        <a href="{app['link']}" target="_blank" style="text-decoration: none; margin-top: auto;">
            <button style="
                width: 100%; 
                padding: 10px; 
                border-radius: 8px; 
                border: none; 
                background-color: #4CAF50; 
                color: white; 
                font-weight: bold;
                cursor: pointer;
            ">
                Explorar Aplicación
            </button>
        </a>
    </div>
    """
    st.markdown(card_html, unsafe_allow_html=True)


# 2. Creación de las tarjetas usando Columnas (3 por fila)
N_COLUMNS = 3
cols = st.columns(N_COLUMNS)
col_index = 0

for app in APPLICATIONS:
    # Usar el índice de columna actual
    with cols[col_index]:
        # Dentro de cada columna, renderizar la tarjeta
        create_app_card(app)
    
    # Avanzar al siguiente índice (ciclo 0, 1, 2, 0, 1, 2...)
    col_index = (col_index + 1) % N_COLUMNS


# --- 🦶 Footer Discreto ---
st.markdown("""
    <div class="footer">
        Creado con ❤️ usando Streamlit
    </div>
""", unsafe_allow_html=True)
