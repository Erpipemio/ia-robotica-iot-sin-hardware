# Proyecto: LCD 16x2 con Sensor DHT22 (Clase 5)

Este es el quinto proyecto de la Ruta de Aprendizaje de Inteligencia Artificial + Robótica sin hardware.

## 🎯 Objetivo
Leer temperatura y humedad con un sensor DHT22 y mostrar los valores en una pantalla LCD 16x2 usando Arduino UNO.

## 🔧 Herramientas utilizadas
- Wokwi (https://wokwi.com)
- Arduino UNO
- Sensor DHT22
- Pantalla LCD 16x2
- Potenciómetro 10kΩ (para contraste del LCD)
- Resistencia 10kΩ (para el sensor)
- Librerías: DHT.h y LiquidCrystal.h

## 📋 Lógica del código

```cpp
#include <DHT.h>
#include <LiquidCrystal.h>

#define DHTPIN 7
#define DHTTYPE DHT22
DHT dht(DHTPIN, DHTTYPE);

LiquidCrystal lcd(12, 11, 5, 4, 3, 2);

void setup() {
  lcd.begin(16, 2);
  dht.begin();
  lcd.print("Iniciando...");
  delay(2000);
  lcd.clear();
}

void loop() {
  float h = dht.readHumidity();
  float t = dht.readTemperature();

  if (isnan(h) || isnan(t)) {
    lcd.setCursor(0, 0);
    lcd.print("Error sensor");
    return;
  }

  lcd.setCursor(0, 0);
  lcd.print("Temp: ");
  lcd.print(t);
  lcd.print((char)223);
  lcd.print("C");

  lcd.setCursor(0, 1);
  lcd.print("Humedad: ");
  lcd.print(h);
  lcd.print(" %");

  delay(2000);
}
```

## 🖼️ Conexiones del circuito

### Sensor DHT22:
- VCC → 5V
- DATA → Pin 7
- GND → GND
- Resistencia de 10kΩ entre VCC y DATA

### LCD 16x2 (modo paralelo):
- RS → Pin 12
- E  → Pin 11
- D4 → Pin 5
- D5 → Pin 4
- D6 → Pin 3
- D7 → Pin 2
- VO → Centro del potenciómetro (entre GND y 5V)

## 📎 Enlace al proyecto
[Ver en Wokwi](https://wokwi.com/projects/435049492778627073)