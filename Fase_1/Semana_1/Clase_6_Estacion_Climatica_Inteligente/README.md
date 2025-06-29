# Proyecto: Mini Estación Ambiental Inteligente (Clase 6)

Este es el sexto proyecto de la Ruta de Aprendizaje de Inteligencia Artificial + Robótica sin hardware.

## 🎯 Objetivo
Crear un sistema que lea temperatura y humedad del ambiente y active alarmas visuales y sonoras si se superan ciertos límites.

## 🧠 Funcionalidad
- Muestra temperatura y humedad en una pantalla LCD
- Enciende un LED si la temperatura supera 30 °C
- Activa un buzzer si supera 35 °C
- Muestra alerta en pantalla si hay calor extremo

## 🔧 Componentes utilizados
- Arduino UNO
- Sensor DHT22
- Pantalla LCD 16x2
- Potenciómetro 10kΩ (para contraste del LCD)
- LED rojo
- Buzzer
- Resistencia 10kΩ (DHT22)
- Resistencia 220Ω (LED)

## 🔌 Conexiones

### Sensor DHT22:
- DATA → Pin 7
- VCC → 5V
- GND → GND
- Resistencia de 10kΩ entre VCC y DATA

### Pantalla LCD 16x2:
- RS → 12, E → 11
- D4 → 5, D5 → 4, D6 → 3, D7 → 2
- VO → Centro del potenciómetro (entre GND y 5V)

### LED rojo:
- Ánodo → Pin 8 (con resistencia 220Ω)
- Cátodo → GND

### Buzzer:
- Positivo → Pin 9
- Negativo → GND

## 📎 Enlace al proyecto
[Ver en Wokwi](https://wokwi.com/projects/435053114821314561)