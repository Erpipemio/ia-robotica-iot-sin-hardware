#include <DHT.h>

#define DHTPIN 7
#define DHTTYPE DHT22
DHT dht(DHTPIN, DHTTYPE);

void setup() {
  Serial.begin(9600);
  dht.begin();
}

void loop() {
  float t = dht.readTemperature();
  float h = dht.readHumidity();

  if (!isnan(t) && !isnan(h)) {
    Serial.print("Temperatura:");
    Serial.print(t);
    Serial.print(",Humedad:");
    Serial.println(h);
  } else {
    Serial.println("Error de lectura");
  }

  delay(2000);
}
