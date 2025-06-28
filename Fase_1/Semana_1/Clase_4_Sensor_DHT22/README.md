# Proyecto: Sensor DHT22 que activa LED por temperatura (Clase 4)

Este es el cuarto proyecto de la Ruta de Aprendizaje de Inteligencia Artificial + Robótica sin hardware.

## 🎯 Objetivo
Leer temperatura y humedad usando un sensor DHT22 y encender un LED si la temperatura supera los 30°C.

## 🔧 Herramientas utilizadas
- Wokwi (https://wokwi.com)
- Arduino UNO (simulado)
- Sensor DHT22
- LED
- Resistencia de 220Ω (LED)
- Resistencia de 10kΩ (pull-up entre pines 1 y 2 del sensor)

## 🧠 Lógica del código

```cpp
#include "DHT.h"

#define DHTPIN 2
#define DHTTYPE DHT22

DHT dht(DHTPIN, DHTTYPE);

int pinLED = 13;

void setup() {
  Serial.begin(9600);
  dht.begin();
  pinMode(pinLED, OUTPUT);
}

void loop() {
  float h = dht.readHumidity();
  float t = dht.readTemperature();

  if (isnan(h) || isnan(t)) {
    Serial.println("Error al leer del sensor DHT22");
    return;
  }

  Serial.print("Humedad: ");
  Serial.print(h);
  Serial.print(" %  |  Temperatura: ");
  Serial.print(t);
  Serial.println(" °C");

  if (t > 30) {
    digitalWrite(pinLED, HIGH);
  } else {
    digitalWrite(pinLED, LOW);
  }

  delay(2000);
}
```

## 🖼️ Diagrama del circuito
- DHT22:
  - Pin 1 → 5V
  - Pin 2 → Pin 2 del Arduino
  - Pin 4 → GND
  - Entre Pin 1 y Pin 2 → Resistencia de 10kΩ
- LED con resistencia de 220Ω → Pin 13

## 📎 Enlace al proyecto
[Ver en Wokwi](https://wokwi.com/projects/435036338599831553)