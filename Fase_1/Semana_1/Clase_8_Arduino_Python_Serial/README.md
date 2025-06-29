# Clase 8 – Comunicación Serial Arduino ↔ Python

Este proyecto demuestra cómo conectar Arduino con Python a través del puerto serial, enviando datos ambientales para almacenarlos o analizarlos.

## 🔧 Componentes usados
- Arduino UNO (simulado o físico)
- Sensor DHT22
- Conexión USB (cuando se use físico)

## 💻 Funcionalidad
- Arduino mide temperatura y humedad
- Imprime datos en formato:
- Python recibe esos datos, los guarda en un `.csv` y los muestra en consola

## 📦 Archivos incluidos
- `sketch.ino`: Código Arduino
- `lector_serial.py`: Script Python para recibir los datos
- `datos_ambientales.csv`: Archivo que se genera automáticamente

## 📎 Simulación
[Ver en Wokwi](https://wokwi.com/projects/435123903434376193)

⚠ Nota: Wokwi no permite conexión serial con Python real, pero el sistema está listo para funcionar con Arduino físico.

## 🧠 Qué aprendiste
- Comunicación Serial
- Envío de datos estructurados
- Integración Arduino ↔ Python
- Preparación para aplicaciones de IA y Big Data
