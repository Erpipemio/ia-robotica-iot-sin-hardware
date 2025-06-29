import streamlit as st
import random
import time

st.set_page_config(page_title="Dashboard Sensorial", layout="centered")

st.title("🌡️ Dashboard Ambiental en Tiempo Real")
st.subheader("Monitoreo de Temperatura y Humedad")

# Configura umbrales
temp_max = st.slider("⚙️ Umbral de temperatura máxima (°C)", 25.0, 45.0, 32.0)
hum_max = st.slider("⚙️ Umbral de humedad máxima (%)", 40.0, 90.0, 65.0)

# Contenedor para lecturas
temp_chart = st.line_chart()
hum_chart = st.line_chart()
log_area = st.empty()

# Simular datos
temperaturas = []
humedades = []

for i in range(30):
    temp = round(random.uniform(24, 38), 1)
    hum = round(random.uniform(40, 75), 1)

    temperaturas.append(temp)
    humedades.append(hum)

    temp_chart.line_chart(temperaturas)
    hum_chart.line_chart(humedades)

    msg = f"🌡️ Temp: {temp} °C | 💧 Hum: {hum} %"
    if temp > temp_max:
        msg += f" ⚠️ ¡Alerta de temperatura!"
    if hum > hum_max:
        msg += f" ⚠️ ¡Alerta de humedad!"

    log_area.write(msg)
    time.sleep(1)