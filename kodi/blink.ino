
int graenn = 2;
int raudur = 3;

void setup() {                
  pinMode(graenn, OUTPUT);     
  pinMode(raudur, OUTPUT);   
}

void loop() {
  digitalWrite(graenn, HIGH);  
  digitalWrite(raudur, HIGH);  
  delay(1000);      
  digitalWrite(graenn, LOW);   
  digitalWrite(raudur, LOW);   
  delay(1000);              
}