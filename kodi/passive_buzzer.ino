int buzzerPin = 8;

void setup() {
  pinMode(buzzerPin, OUTPUT);

  tone(buzzerPin, 1000, 2000);  // 1000 hertxz í spila í 2 sekúndur í byrjun
}

void loop() {
  tone(buzzerPin, 440); // A4, 440 hertz
  delay(1000);

  tone(buzzerPin, 494); // B4
  delay(1000);

  tone(buzzerPin, 523); // C4
  delay(1000);

  tone(buzzerPin, 587); // D4
  delay(1000);

  tone(buzzerPin, 659); // E4
  delay(1000);

  tone(buzzerPin, 698); // F4
  delay(1000);

  tone(buzzerPin, 784); // G4
  delay(1000);

  noTone(buzzerPin);  // hætta í 1000 ms
  delay(1000);
}
