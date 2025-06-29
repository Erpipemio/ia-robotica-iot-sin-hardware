import random
import time
from datetime import datetime
import platform

if platform.system() == "Windows":
    import winsound

UMBRAL_TEMP = 32.0
UMBRAL_HUM = 65.0
TIEMPO_ENTRE_DATOS = 2

def leer_sensor():
    temp = round(random.uniform(24, 38), 1)
    hum = round(random.uniform(40, 75), 1)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return timestamp, temp, hum

def evaluar_alertas(timestamp, temp, hum):
    alertas = []
    if temp > UMBRAL_TEMP:
        alertas.append(f"🔥 ALERTA: Temp alta ({temp} °C)")
        if platform.system() == "Windows":
            winsound.Beep(1000, 300)
    if hum > UMBRAL_HUM:
        alertas.append(f"💧 ALERTA: Humedad alta ({hum} %)")
    return alertas

def main():
    print("🛡️ Sistema de Alertas Inteligentes iniciado...\n")
    while True:
        ts, temp, hum = leer_sensor()
        alertas = evaluar_alertas(ts, temp, hum)

        print(f"{ts} → Temp: {temp} °C | Hum: {hum} %")
        if alertas:
            for alerta in alertas:
                print(alerta)
        print("-" * 40)
        time.sleep(TIEMPO_ENTRE_DATOS)

if __name__ == "__main__":
    main()