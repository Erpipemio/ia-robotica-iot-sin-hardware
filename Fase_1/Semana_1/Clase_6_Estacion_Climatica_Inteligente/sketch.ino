#include <DHT.h>
#include <LiquidCrystal.h>

// Sensor
#define DHTPIN 7
#define DHTTYPE DHT22
DHT dht(DHTPIN, DHTTYPE);

// LCD
LiquidCrystal lcd(12, 11, 5, 4, 3, 2);

// Actuadores
#define LEDPIN 8
#define BUZZERPIN 9

void setup() {
  lcd.begin(16, 2);
  dht.begin();
  pinMode(LEDPIN, OUTPUT);
  pinMode(BUZZERPIN, OUTPUT);
  lcd.print("Estacion Clima");
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

  // Mostrar temperatura y humedad
  lcd.setCursor(0, 0);
  lcd.print("Temp: ");
  lcd.print(t);
  lcd.print((char)223);
  lcd.print("C");

  lcd.setCursor(0, 1);
  lcd.print("Humedad: ");
  lcd.print(h);
  lcd.print(" % ");

  // Control LED
  if (t > 30) {
    digitalWrite(LEDPIN, HIGH);
  } else {
    digitalWrite(LEDPIN, LOW);
  }

  // Alerta de calor con buzzer
  if (t > 35) {
    digitalWrite(BUZZERPIN, HIGH);
    lcd.setCursor(0, 1);
    lcd.print("ALERTA DE CALOR ");
  } else {
    digitalWrite(BUZZERPIN, LOW);
  }

  delay(2000);
}