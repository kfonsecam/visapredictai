import streamlit as st
from datetime import datetime

st.set_page_config(page_title="VisaPredict AI", layout="wide")
st.title("VisaPredict AI - Estimación de Aprobación de Visas")

st.markdown("Complete el siguiente formulario para estimar el estado de una visa de trabajo basada en datos históricos.")

with st.form("visa_form"):
    case_id = st.text_input("ID del Caso *", placeholder="Ej: CASE-2025-001")

    col1, col2 = st.columns(2)
    with col1:
        country = st.selectbox("País del Empleado *", [
            "", "India", "China", "Mexico", "Canada", "Reino unido", "Alemania", "Brasil", "Japón", "Corea del Sur", "Australia"
        ])
    with col2:
        region = st.selectbox("Región de Empleo *", [
            "", "Noreste", "Sureste", "Medio oeste", "Suroeste", "Oeste"
        ])

    education = st.selectbox("Nivel de Educación *", [
        "", "Preparatoria", "Licenciatura", "Maestría", "Doctorado"
    ])

    col1, col2 = st.columns(2)
    with col1:
        has_job_experience = st.radio("¿Tiene Experiencia Laboral?", ["Sí", "No"])
    with col2:
        requires_job_training = st.radio("¿Requiere Entrenamiento?", ["Sí", "No"])

    col1, col2 = st.columns(2)
    with col1:
        company_no_of_employees = st.number_input("Número de Empleados *", min_value=1)
    with col2:
        yr_of_estab = st.number_input("Año de Establecimiento *", min_value=1900, max_value=datetime.now().year)

    col1, col2 = st.columns(2)
    with col1:
        prevailing_wage = st.number_input("Salario Prevaleciente *", min_value=0)
    with col2:
        unit_of_wage = st.selectbox("Unidad de Salario", ["Anual", "Por hora"])

    full_time_position = st.radio("¿Posición de Tiempo Completo?", ["Sí", "No"])

    submit = st.form_submit_button("Analizar con AI")

if submit:
    

    # Lógica de predicción (simulación AI)
    score = 50

    if education in ["Mestría", "Doctorado"]:
        score += 20
    elif education == "Licenciatura":
        score += 10

    if has_job_experience == "Sí":
        score += 15

    if company_no_of_employees > 1000:
        score += 10
    elif company_no_of_employees > 100:
        score += 5

    antiguedad = datetime.now().year - yr_of_estab
    if antiguedad > 10:
        score += 10
    elif antiguedad > 5:
        score += 5

    if unit_of_wage == "Anual":
        if prevailing_wage > 100000:
            score += 15
        elif prevailing_wage > 70000:
            score += 10

    if full_time_position == "Sí":
        score += 5

    if score >= 80:
        status = "Aprobada"
        confidence = min(95, score)
    elif score >= 60:
        status = "Aprobada condicionada"
        confidence = score
    elif score >= 40:
        status = "Retirada"
        confidence = score
    else:
        status = "Rechazada"
        confidence = 100 - score

    st.subheader("🧠 Resultado de la Predicción")
    st.metric("Estado Estimado", status)
    st.metric("Nivel de Confianza", f"{confidence}%")
    st.progress(min(score, 100), text=f"Puntaje total: {score}")
    st.info("Esta predicción es estimada en función de los datos proporcionados y no garantiza un resultado oficial.")

