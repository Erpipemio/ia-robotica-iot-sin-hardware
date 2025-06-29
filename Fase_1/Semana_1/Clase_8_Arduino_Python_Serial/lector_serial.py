import serial
import time

puerto = "COM3"  # ⚠ Cambiar por el puerto correcto
baudrate = 9600

ser = serial.Serial(puerto, baudrate, timeout=1)
time.sleep(2)  # Espera inicial

print("Conectado. Leyendo datos...\n")

with open("datos_ambientales.csv", "w") as f:
    f.write("Temperatura,Humedad\n")
    while True:
        linea = ser.readline().decode().strip()
        if "Temperatura" in linea:
            try:
                temp = linea.split(",")[0].split(":")[1]
                hum = linea.split(",")[1].split(":")[1]
                print(f"Temperatura: {temp} °C | Humedad: {hum} %")
                f.write(f"{temp},{hum}\n")
            except:
                pass
