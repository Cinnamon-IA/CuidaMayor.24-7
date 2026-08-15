import streamlit as st

# ==========================================
# CONFIGURACIÓN DE LA PÁGINA
# ==========================================

st.set_page_config(
    page_title="CuidaMayor 24/7",
    page_icon="🧓",
    layout="centered"
)

# ==========================================
# TÍTULO
# ==========================================

st.title("🧓 CuidaMayor 24/7")

st.write(
    "Asistente educativo para apoyar el cuidado "
    "domiciliario del adulto mayor y su cuidador."
)

st.warning(
    "⚠️ Este chatbot brinda orientación educativa. "
    "No reemplaza la valoración ni las indicaciones "
    "de un profesional de salud."
)

# ==========================================
# BASE DE CONOCIMIENTOS
# ==========================================

respuestas = {

    "caidas": """
### ⚠️ Prevención de caídas

Para reducir el riesgo de caídas:

- Mantén los espacios despejados.
- Retira objetos que puedan provocar tropiezos.
- Mantén una buena iluminación.
- Utiliza los apoyos indicados para la movilidad.
- Acompaña al adulto mayor cuando necesite ayuda para movilizarse.

Si ocurre una caída, especialmente si hay golpe, dolor intenso,
pérdida de conciencia o deterioro repentino, busca atención
profesional oportunamente.
""",

    "ulceras": """
### 🛏️ Prevención de úlceras por presión

Para ayudar a prevenir lesiones por presión:

- Observa periódicamente el estado de la piel.
- Mantén la piel limpia y seca.
- Realiza cambios de posición de acuerdo con las necesidades
  del adulto mayor.
- Evita mantener presión prolongada sobre una misma zona.
- Comunica cualquier cambio importante en la piel al profesional
  de salud.
""",

    "movilizacion": """
### 🦽 Movilización segura

Antes de movilizar al adulto mayor:

1. Explica qué vas a realizar.
2. Asegura que el entorno esté despejado.
3. Verifica que la persona esté preparada para el movimiento.
4. Utiliza una técnica segura.
5. Evita realizar movimientos bruscos.

La movilización debe proteger tanto al adulto mayor como al cuidador.
""",

    "medicamentos": """
### 💊 Medicamentos

Los medicamentos deben utilizarse siguiendo las indicaciones
del profesional de salud.

No debes:

- Cambiar la dosis por cuenta propia.
- Suspender un medicamento sin indicación profesional.
- Compartir medicamentos.
- Modificar los horarios prescritos sin orientación.

Si existe una duda sobre un medicamento específico, consulta
al profesional que lo indicó.
""",

    "cuidador": """
### ❤️ Autocuidado del cuidador

El cuidador también necesita cuidarse.

Algunas estrategias pueden ser:

- Realizar pausas durante el día.
- Dormir y descansar cuando sea posible.
- Solicitar apoyo a familiares o personas de confianza.
- Reconocer señales de agotamiento.
- Buscar orientación profesional cuando la carga del cuidado
  sea difícil de manejar.

Cuidar a otra persona no significa dejar de cuidar de ti mismo.
""",

    "signos": """
### 🚨 Signos de alarma

Si el adulto mayor presenta un cambio repentino o importante
en su estado de salud, es recomendable buscar valoración
profesional oportunamente.

Ante una situación que parezca una emergencia, utiliza los
servicios de emergencia disponibles en tu localidad.
"""
}


# ==========================================
# FUNCIÓN DEL CHATBOT
# ==========================================

def responder(pregunta):

    pregunta = pregunta.lower()

    # Prevención de caídas
    if any(palabra in pregunta for palabra in [
        "caída",
        "caidas",
        "caídas",
        "tropezar",
        "tropezones"
    ]):
        return respuestas["caidas"]

    # Úlceras por presión
    elif any(palabra in pregunta for palabra in [
        "úlcera",
        "ulcera",
        "úlceras",
        "ulceras",
        "presión",
        "llaga",
        "herida"
    ]):
        return respuestas["ulceras"]

    # Movilización
    elif any(palabra in pregunta for palabra in [
        "movilizar",
        "movilización",
        "movilizacion",
        "transferir",
        "levantar",
        "mover"
    ]):
        return respuestas["movilizacion"]

    # Medicamentos
    elif any(palabra in pregunta for palabra in [
        "medicamento",
        "medicamentos",
        "pastilla",
        "pastillas",
        "medicina",
        "dosis"
    ]):
        return respuestas["medicamentos"]

    # Cuidador
    elif any(palabra in pregunta for palabra in [
        "cuidador",
        "agotado",
        "agotamiento",
        "cansancio",
        "estrés",
        "estres",
        "descanso"
    ]):
        return respuestas["cuidador"]

    # Signos de alarma
    elif any(palabra in pregunta for palabra in [
        "alarma",
        "emergencia",
        "urgencia",
        "grave",
        "repentino"
    ]):
        return respuestas["signos"]

    # Saludo
    elif any(palabra in pregunta for palabra in [
        "hola",
        "buenos días",
        "buenos dias",
        "buenas tardes",
        "buenas noches"
    ]):
        return """
### 👋 ¡Hola!

Soy **CuidaMayor 24/7**.

Puedo orientarte sobre:

🦽 Movilización segura  
⚠️ Prevención de caídas  
🛏️ Prevención de úlceras por presión  
💊 Medicamentos  
❤️ Autocuidado del cuidador  
🚨 Signos de alarma  

¿Sobre qué tema necesitas orientación?
"""

    # Si no reconoce la pregunta
    else:
        return """
### 🤔 No encontré una respuesta específica

Puedes preguntarme sobre:

- Prevención de caídas
- Úlceras por presión
- Movilización segura
- Medicamentos
- Autocuidado del cuidador
- Signos de alarma

Por ejemplo:

**¿Cómo puedo prevenir una caída?**
"""


# ==========================================
# HISTORIAL DEL CHAT
# ==========================================

if "mensajes" not in st.session_state:
    st.session_state.mensajes = []


# Mostrar mensajes anteriores
for mensaje in st.session_state.mensajes:

    with st.chat_message(mensaje["rol"]):
        st.markdown(mensaje["texto"])


# ==========================================
# CAJA PARA ESCRIBIR
# ==========================================

pregunta = st.chat_input(
    "Escribe aquí tu pregunta..."
)


# ==========================================
# PROCESAR PREGUNTA
# ==========================================

if pregunta:

    # Guardar pregunta
    st.session_state.mensajes.append({
        "rol": "user",
        "texto": pregunta
    })

    # Generar respuesta
    respuesta = responder(pregunta)

    # Guardar respuesta
    st.session_state.mensajes.append({
        "rol": "assistant",
        "texto": respuesta
    })

    # Actualizar el chatbot
    st.rerun()
