int ledPin = 13;
int botonPin = 2;

void setup() {
  pinMode(ledPin, OUTPUT);
  pinMode(botonPin, INPUT); // INPUT usa resistencia externa
}

void loop() {
  int estado = digitalRead(botonPin);
  if (estado == HIGH) {
    digitalWrite(ledPin, HIGH);
  } else {
    digitalWrite(ledPin, LOW);
  }
}