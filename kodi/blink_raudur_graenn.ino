int raudur = 4;

int graenn = 2;

void setup() {                
  pinMode(graenn, OUTPUT);     
  pinMode(raudur, OUTPUT);   
}

void loop() {
  digitalWrite(graenn, HIGH);  
  digitalWrite(raudur, HIGH);  
  delay(500);      
  digitalWrite(graenn, LOW);   
  digitalWrite(raudur, LOW);   
  delay(500);              
}