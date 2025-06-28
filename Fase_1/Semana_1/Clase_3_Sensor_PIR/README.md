# Proyecto: Sensor PIR que controla un LED (Clase 3)

Este es el tercer proyecto de la Ruta de Aprendizaje de Inteligencia Artificial + Robótica sin hardware.

## 🎯 Objetivo
Detectar movimiento con un sensor PIR y encender un LED si se detecta movimiento.

## 🔧 Herramientas utilizadas
- Wokwi (https://wokwi.com)
- Arduino UNO (simulado)
- Sensor PIR
- LED
- Resistencia de 220Ω

## 🧠 Lógica del código

```cpp
int pinSensor = 2;
int pinLED = 13;

void setup() {
  pinMode(pinSensor, INPUT);
  pinMode(pinLED, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  int estadoSensor = digitalRead(pinSensor);

  if (estadoSensor == HIGH) {
    digitalWrite(pinLED, HIGH);
    Serial.println("Movimiento detectado");
  } else {
    digitalWrite(pinLED, LOW);
    Serial.println("Sin movimiento");
  }

  delay(500);
}
```

## 🖼️ Diagrama del circuito
- Sensor PIR:
  - VCC → 5V
  - GND → GND
  - OUT → Pin 2
- LED con resistencia de 220Ω → Pin 13

## 📎 Enlace al proyecto
[Ver en Wokwi](https://wokwi.com/projects/435014264836170753)