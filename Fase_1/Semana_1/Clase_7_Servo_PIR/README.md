# Clase 7 – Sistema de Movimiento con Sensor PIR y Servo Motor

Este es el séptimo proyecto de la Ruta de Inteligencia Artificial + Robótica sin hardware. Simula una puerta automática o mecanismo de acceso activado por presencia.

## 🎯 Objetivo
Detectar movimiento con un sensor PIR y accionar un servo motor que simula una puerta, compuerta o mecanismo físico.

## 🔧 Componentes
- Arduino UNO
- Sensor PIR
- Servo Motor
- LED (opcional)
- Resistencia 220Ω (para el LED)

## 🔌 Conexiones

### Sensor PIR
- VCC → 5V
- GND → GND
- OUT → D2

### Servo Motor
- Señal (amarillo) → D9
- VCC (rojo) → 5V
- GND (negro) → GND

### LED (opcional)
- Ánodo → D8 (con resistencia de 220Ω)
- Cátodo → GND

## 💻 Código

Incluido en el archivo `sketch.ino`. Usa la librería `Servo.h`.

## 🔁 Lógica
- Si se detecta movimiento:
  - Se enciende el LED
  - El servo se mueve a 90° (abrir)
- Si no hay movimiento:
  - El LED se apaga
  - El servo vuelve a 0° (cerrar)

## 📎 Simulación Wokwi
[Ver proyecto](https://wokwi.com/projects/435055127436123137)
