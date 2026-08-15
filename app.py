import streamlit as st
import unicodedata

# ==========================================================
# CONFIGURACIÓN
# ==========================================================

st.set_page_config(
    page_title="CuidaMayor 24/7",
    page_icon="🧓",
    layout="centered"
)

st.title("🧓 CuidaMayor 24/7")
st.caption("Asistente educativo para el cuidado del adulto mayor")

st.warning(
    "⚠️ Este chatbot brinda orientación educativa. "
    "No reemplaza la valoración, diagnóstico ni indicaciones "
    "de un profesional de salud."
)


# ==========================================================
# FUNCIONES AUXILIARES
# ==========================================================

def limpiar_texto(texto):
    """
    Convierte el texto a minúsculas y elimina tildes.
    Esto permite reconocer:
    'úlcera', 'ulcera' y 'ÚLCERA'
    como la misma palabra.
    """

    texto = texto.lower()

    texto = unicodedata.normalize(
        "NFD",
        texto
    )

    texto = "".join(
        caracter
        for caracter in texto
        if unicodedata.category(caracter) != "Mn"
    )

    return texto


def contiene(texto, palabras):
    """
    Comprueba si alguna palabra o frase aparece
    dentro de la pregunta.
    """

    return any(
        palabra in texto
        for palabra in palabras
    )


# ==========================================================
# RESPUESTAS GENERALES
# ==========================================================

def respuesta_saludo():

    return """
### 👋 ¡Hola!

Soy **CuidaMayor 24/7**, tu asistente educativo para el
cuidado del adulto mayor.

Puedo conversar contigo sobre:

🛏️ Úlceras por presión  
⚠️ Prevención de caídas  
🦽 Movilización segura  
💊 Medicamentos  
❤️ Autocuidado del cuidador  
🚨 Signos de alarma

También puedes hacer preguntas de seguimiento.

Por ejemplo:

**"¿Cómo se limpia una úlcera por presión?"**

y después puedes preguntarme:

**"¿Qué materiales necesito?"**

o:

**"¿Y qué hago después?"**
"""


# ==========================================================
# ÚLCERAS POR PRESIÓN
# ==========================================================

def respuesta_ulcera():

    return """
### 🛏️ Cuidado de una úlcera por presión

Si estás preguntando por la limpieza de una lesión por presión,
es importante saber que el cuidado depende de las características
de la herida y del plan indicado por el profesional de salud.

Como orientación educativa general:

**Paso 1. Higiene de manos**

Lávate las manos antes de realizar el cuidado de la herida.

**Paso 2. Preparar el material**

Ten preparado el material indicado por el profesional, evitando
improvisar productos o medicamentos.

**Paso 3. Retirar el apósito**

Si existe un apósito, retíralo con cuidado. Si está adherido,
no lo arranques bruscamente.

**Paso 4. Limpiar**

La limpieza debe realizarse suavemente utilizando el producto
indicado para esa herida, sin frotar agresivamente el tejido.

**Paso 5. Observar**

Presta atención a cambios como aumento del enrojecimiento,
dolor, secreción, mal olor, sangrado o cambios en la piel.

**Paso 6. Proteger**

Coloca el apósito o tratamiento indicado por el profesional.

**Paso 7. Registrar y vigilar**

Observa la evolución de la lesión y comunica cambios importantes
al equipo de salud.

⚠️ No se recomienda improvisar sustancias como alcohol, agua
oxigenada u otros productos sobre una herida sin indicación
profesional.
"""

# ==========================================================
# PREGUNTAS DE SEGUIMIENTO SOBRE ÚLCERAS
# ==========================================================

def materiales_ulcera():

    return """
### 🧴 ¿Qué materiales se pueden necesitar?

El material depende del tipo y características de la lesión y
del plan de cuidado indicado.

De manera general, pueden utilizarse:

- Guantes limpios o según el procedimiento indicado.
- Solución de limpieza indicada.
- Gasas limpias.
- Apósito seleccionado según la indicación profesional.
- Bolsa para desechar el material utilizado.

⚠️ No todas las úlceras necesitan el mismo apósito ni el mismo
tratamiento. La selección debe realizarse de acuerdo con la
valoración de la lesión.
"""


def productos_ulcera():

    return """
### 🚫 ¿Qué productos debo evitar?

No improvises productos sobre una úlcera por presión.

En particular, no utilices alcohol, agua oxigenada,
antisépticos u otros productos dentro de la herida
a menos que hayan sido indicados específicamente.

La limpieza debe ser suave y seguir el plan establecido
por el profesional de salud.
"""


def signos_infeccion():

    return """
### 🚨 ¿Qué debo vigilar?

Durante el cuidado de una úlcera presta atención a:

- Aumento del dolor.
- Enrojecimiento o cambios alrededor de la lesión.
- Aumento de la secreción.
- Secreción con aspecto purulento.
- Mal olor.
- Sangrado importante.
- Fiebre.
- Deterioro general del adulto mayor.

Si aparecen signos preocupantes o un deterioro rápido,
se debe buscar valoración profesional oportunamente.
"""


# ==========================================================
# CAÍDAS
# ==========================================================

def respuesta_caidas():

    return """
### ⚠️ Prevención de caídas

Para disminuir el riesgo:

1. Mantén los espacios despejados.
2. Retira objetos con los que pueda tropezar.
3. Mantén una iluminación adecuada.
4. Utiliza los dispositivos de apoyo indicados.
5. Acompaña al adulto mayor cuando necesite ayuda.
6. Mantén los elementos de uso frecuente al alcance.

Si quieres, también puedo explicarte **qué hacer después
de una caída**.
"""


def despues_caida():

    return """
### ⚠️ Después de una caída

Primero verifica cómo se encuentra el adulto mayor.

Evita levantarlo inmediatamente si presenta:

- Dolor intenso.
- Golpe importante.
- Sangrado.
- Pérdida de conciencia.
- Confusión nueva.
- Dificultad para mover una extremidad.
- Dificultad para respirar.

En estas situaciones se debe buscar valoración profesional
o atención de emergencia según la gravedad.

Si no hay signos de alarma, igualmente conviene informar
la caída al profesional que realiza el seguimiento.
"""


# ==========================================================
# MOVILIZACIÓN
# ==========================================================

def respuesta_movilizacion():

    return """
### 🦽 Movilización segura

Antes de movilizar al adulto mayor:

**1. Explica lo que vas a hacer.**

**2. Asegura el entorno.**

Retira obstáculos y verifica que exista espacio suficiente.

**3. Comprueba que la persona esté preparada.**

Permite que participe según sus capacidades.

**4. Realiza el movimiento de manera controlada.**

Evita movimientos bruscos y protege tu propia espalda.

**5. Solicita ayuda si es necesario.**

Si la persona requiere más apoyo del que puedes proporcionar,
no intentes movilizarla solo.

Si quieres, puedo explicarte una movilización específica,
por ejemplo:

**"¿Cómo pasar de la cama a una silla?"**
"""


def cama_silla():

    return """
### 🛏️➡️🪑 De la cama a una silla

De forma educativa:

1. Explica el procedimiento al adulto mayor.
2. Coloca la silla en una posición segura y adecuada.
3. Asegura los frenos cuando corresponda.
4. Ayuda a la persona a incorporarse progresivamente.
5. Comprueba que esté estable antes de iniciar el traslado.
6. Realiza el traslado de forma controlada.
7. Asegúrate de que quede correctamente sentado.

⚠️ La técnica exacta depende de la movilidad, fuerza,
equilibrio y condición clínica de la persona.

Si existe dependencia importante, utiliza la ayuda técnica
y el método enseñado por el profesional.
"""


# ==========================================================
# MEDICAMENTOS
# ==========================================================

def respuesta_medicamentos():

    return """
### 💊 Medicamentos

Para favorecer la adherencia:

- Mantén un horario organizado.
- Utiliza un registro o recordatorio.
- Verifica el medicamento antes de administrarlo.
- Sigue exactamente la prescripción.
- No cambies la dosis por cuenta propia.
- No suspendas el tratamiento sin indicación profesional.

Si existe una duda específica sobre un medicamento,
consulta al profesional que lo formuló.
"""


# ==========================================================
# AUTOCUIDADO
# ==========================================================

def respuesta_cuidador():

    return """
### ❤️ Autocuidado del cuidador

Cuidar a otra persona puede generar cansancio físico y emocional.

Algunas medidas útiles son:

- Realizar pausas.
- Dormir y descansar cuando sea posible.
- Pedir ayuda a familiares o personas de confianza.
- Compartir las tareas de cuidado.
- Reconocer señales de agotamiento.
- Buscar orientación profesional cuando sea necesario.

Recuerda:

**Cuidar al cuidador también es parte del cuidado.**
"""


# ==========================================================
# SIGNOS DE ALARMA
# ==========================================================

def respuesta_alarma():

    return """
### 🚨 Signos de alarma

Busca valoración profesional oportunamente ante cambios
importantes o repentinos en el estado del adulto mayor.

Especialmente si aparecen:

- Dificultad para respirar.
- Pérdida de conciencia.
- Confusión repentina.
- Dolor intenso.
- Sangrado importante.
- Deterioro rápido del estado general.
- Fiebre acompañada de empeoramiento de una herida.

Ante una emergencia, utiliza los servicios de emergencia
disponibles en tu localidad.
"""


# ==========================================================
# MOTOR CONVERSACIONAL
# ==========================================================

def responder(pregunta):

    texto = limpiar_texto(pregunta)

    # ------------------------------------------------------
    # SALUDOS
    # ------------------------------------------------------

    if contiene(texto, [
        "hola",
        "buenos dias",
        "buenas tardes",
        "buenas noches"
    ]):

        return respuesta_saludo()


    # ------------------------------------------------------
    # SEGUIMIENTO: "¿Y DESPUÉS?"
    # ------------------------------------------------------

    if contiene(texto, [
        "y despues",
        "despues que",
        "que sigue",
        "siguiente paso",
        "siguiente",
        "ahora que",
        "luego"
    ]):

        if st.session_state.tema == "ulcera":

            return """
### 🛏️ Después de limpiar la lesión

Después de la limpieza:

1. Observa el estado de la herida.
2. Evita frotar el tejido.
3. Protege la zona según el plan indicado.
4. Coloca el apósito indicado.
5. Desecha el material utilizado de forma adecuada.
6. Realiza nuevamente higiene de manos.

Si quieres, puedo explicarte **qué debes observar
en la herida después de la limpieza**.
"""

        if st.session_state.tema == "caidas":
            return despues_caida()

        if st.session_state.tema == "movilizacion":
            return cama_silla()


    # ------------------------------------------------------
    # ÚLCERAS: PREGUNTAS ESPECÍFICAS
    # ------------------------------------------------------

    if contiene(texto, [
        "ulcera",
        "ulceras",
        "llaga",
        "escara",
        "lesion por presion",
        "herida por presion"
    ]):

        st.session_state.tema = "ulcera"


        if contiene(texto, [
            "limpiar",
            "limpieza",
            "curar",
            "curacion",
            "como se hace"
        ]):

            return respuesta_ulcera()


        if contiene(texto, [
            "material",
            "materiales",
            "necesito",
            "que necesito"
        ]):

            return materiales_ulcera()


        if contiene(texto, [
            "alcohol",
            "agua oxigenada",
            "producto",
            "jabon",
            "antiseptico"
        ]):

            return productos_ulcera()


        if contiene(texto, [
            "infeccion",
            "infectada",
            "pus",
            "secrecion",
            "mal olor",
            "fiebre",
            "dolor"
        ]):

            return signos_infeccion()


        return respuesta_ulcera()


    # ------------------------------------------------------
    # CAÍDAS
    # ------------------------------------------------------

    if contiene(texto, [
        "caida",
        "caidas",
        "tropezar",
        "tropezon",
        "se cayo"
    ]):

        st.session_state.tema = "caidas"

        if contiene(texto, [
            "despues",
            "que hago",
            "que hacer",
            "ocurrio"
        ]):

            return despues_caida()

        return respuesta_caidas()


    # ------------------------------------------------------
    # MOVILIZACIÓN
    # ------------------------------------------------------

    if contiene(texto, [
        "movilizar",
        "movilizacion",
        "mover",
        "levantar",
        "transferir",
        "traslado"
    ]):

        st.session_state.tema = "movilizacion"

        if contiene(texto, [
            "cama",
            "silla",
            "sillon"
        ]):

            return cama_silla()

        return respuesta_movilizacion()


    # ------------------------------------------------------
    # MEDICAMENTOS
    # ------------------------------------------------------

    if contiene(texto, [
        "medicamento",
        "medicamentos",
        "pastilla",
        "pastillas",
        "medicina",
        "dosis",
        "tratamiento"
    ]):

        st.session_state.tema = "medicamentos"

        return respuesta_medicamentos()


    # ------------------------------------------------------
    # CUIDADOR
    # ------------------------------------------------------

    if contiene(texto, [
        "cuidador",
        "cansancio",
        "agotamiento",
        "estres",
        "descanso",
        "cansado"
    ]):

        st.session_state.tema = "cuidador"

        return respuesta_cuidador()


    # ------------------------------------------------------
    # SIGNOS DE ALARMA
    # ------------------------------------------------------

    if contiene(texto, [
        "alarma",
        "emergencia",
        "urgencia",
        "grave",
        "repentino"
    ]):

        return respuesta_alarma()


    # ------------------------------------------------------
    # NO ENTENDIÓ
    # ------------------------------------------------------

    return """
### 🤔 Quiero ayudarte

No estoy seguro de haber entendido tu pregunta.

Puedes explicármela de otra manera.

Por ejemplo:

- **¿Cómo se limpia una úlcera por presión?**
- **¿Qué materiales necesito?**
- **¿Y después qué hago?**
- **¿Qué signos de infección debo vigilar?**
- **¿Cómo prevenir una caída?**
- **¿Qué hago después de una caída?**
- **¿Cómo movilizo a una persona de la cama a una silla?**
- **¿Cómo puedo organizar los medicamentos?**

También puedes hacerme preguntas de seguimiento.
"""


# ==========================================================
# MEMORIA DE LA CONVERSACIÓN
# ==========================================================

if "mensajes" not in st.session_state:

    st.session_state.mensajes = []


if "tema" not in st.session_state:

    st.session_state.tema = None


# ==========================================================
# MOSTRAR HISTORIAL
# ==========================================================

for mensaje in st.session_state.mensajes:

    with st.chat_message(mensaje["rol"]):

        st.markdown(mensaje["texto"])


# ==========================================================
# ENTRADA DEL USUARIO
# ==========================================================

pregunta = st.chat_input(
    "Escribe tu pregunta..."
)


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

    # Actualizar pantalla
    st.rerun()
