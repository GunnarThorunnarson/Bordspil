int led = 2;
int takki = 4;

void setup() {                
  pinMode(led, OUTPUT);     
  pinMode(takki, INPUT_PULLUP);  // ýti á takka þá 0 annars 1 ef ekki ýti   

  Serial.begin(9600);   // til að sjá gildi á skjánum/fartölvu, debugg
}

void loop() {
  int sensorVal = digitalRead(takki);   // lesum af takka og geymum svar (0 eða 1) í breytu
  Serial.println(sensorVal);            // prentum út svar

  if (sensorVal == HIGH)   // 1, ekki ýtt á takka 
  {
     digitalWrite(led, LOW);  // slökkva á led
  } 
  else // annars
  {
     digitalWrite(led, HIGH);  // kveikja á led, ýtt er á takka og haldið
  }
          
}