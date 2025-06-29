#include <Servo.h>

Servo servo;
int pirPin = 2;
int ledPin = 8;

void setup() {
  pinMode(pirPin, INPUT);
  pinMode(ledPin, OUTPUT);
  servo.attach(9);
  servo.write(0); // Posición inicial (cerrado)
  Serial.begin(9600);
}

void loop() {
  int movimiento = digitalRead(pirPin);

  if (movimiento == HIGH) {
    digitalWrite(ledPin, HIGH);
    servo.write(90); // Abrir puerta
    Serial.println("Movimiento detectado: ABRIENDO");
    delay(2000); // Mantener abierto 2 segundos
  } else {
    digitalWrite(ledPin, LOW);
    servo.write(0); // Cerrar puerta
    Serial.println("Sin movimiento: CERRANDO");
  }

  delay(100);
}
