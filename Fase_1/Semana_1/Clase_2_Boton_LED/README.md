# Proyecto: LED controlado por botón (Clase 2)

Este es el segundo proyecto de la Ruta de Aprendizaje de Inteligencia Artificial + Robótica sin hardware.

## 🎯 Objetivo
Encender un LED al presionar un botón, aplicando condicionales y lectura digital.

## 🔧 Herramientas utilizadas
- Wokwi (https://wokwi.com)
- Arduino UNO (simulado)
- LED
- Botón (Pushbutton)
- Resistencia de 220Ω (LED)
- Resistencia de 10kΩ (pull-down del botón)

## 🧠 Lógica del código

```cpp
int ledPin = 13;
int botonPin = 2;

void setup() {
  pinMode(ledPin, OUTPUT);
  pinMode(botonPin, INPUT);
}

void loop() {
  int estado = digitalRead(botonPin);
  if (estado == HIGH) {
    digitalWrite(ledPin, HIGH);
  } else {
    digitalWrite(ledPin, LOW);
  }
}
```

## 🖼️ Diagrama del circuito
- LED conectado al pin 13
- Botón conectado al pin 2 y GND, con resistencia pull-down de 10kΩ

## 📎 Enlace al proyecto
[Ver en Wokwi](https://wokwi.com/projects/435013526778060801)