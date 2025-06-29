import random
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from collections import deque

MAX_DATOS = 30
temperaturas = deque([0]*MAX_DATOS, maxlen=MAX_DATOS)
humedades = deque([0]*MAX_DATOS, maxlen=MAX_DATOS)
tiempos = deque(list(range(-MAX_DATOS+1, 1)), maxlen=MAX_DATOS)

fig, ax = plt.subplots()
linea_temp, = ax.plot([], [], label="Temperatura (°C)", color='red')
linea_hum, = ax.plot([], [], label="Humedad (%)", color='blue')

ax.set_ylim(0, 100)
ax.set_xlim(-MAX_DATOS+1, 0)
ax.set_title("Simulación de Sensor Ambiental")
ax.set_xlabel("Tiempo (s)")
ax.set_ylabel("Valor")
ax.legend(loc="upper left")
ax.grid(True)

def actualizar(frame):
    nueva_temp = round(random.uniform(24, 38), 1)
    nueva_hum = round(random.uniform(40, 70), 1)

    temperaturas.append(nueva_temp)
    humedades.append(nueva_hum)
    tiempos.append(tiempos[-1] + 1)

    linea_temp.set_data(tiempos, temperaturas)
    linea_hum.set_data(tiempos, humedades)
    ax.set_xlim(tiempos[0], tiempos[-1])

    return linea_temp, linea_hum

ani = animation.FuncAnimation(fig, actualizar, interval=1000)
plt.tight_layout()
plt.show()