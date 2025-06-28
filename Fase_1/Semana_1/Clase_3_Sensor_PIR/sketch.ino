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