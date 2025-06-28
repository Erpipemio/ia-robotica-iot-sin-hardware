# Proyecto: Parpadeo de LED (Clase 1)

Este es el primer proyecto de la Ruta de Aprendizaje de Inteligencia Artificial + Robótica sin hardware.

## 🎯 Objetivo
Simular el encendido y apagado de un LED usando el pin 13 del Arduino UNO en Wokwi, para entender la lógica de control digital básica.

## 🔧 Herramientas utilizadas
- Wokwi (https://wokwi.com)
- Arduino UNO (simulado)
- LED
- Resistencia de 220Ω

## 🧠 Lógica del código

```cpp
void setup() {
  pinMode(13, OUTPUT);
}

void loop() {
  digitalWrite(13, HIGH); // Enciende el LED
  delay(1000);            // Espera 1 segundo
  digitalWrite(13, LOW);  // Apaga el LED
  delay(1000);            // Espera 1 segundo
}
```

## 🖼️ Diagrama del circuito
LED conectado al pin 13 mediante una resistencia de 220Ω.

## 📎 Enlace al proyecto
[Ver en Wokwi](https://wokwi.com/projects/435011306258817025)