int lightSensorPin = A0;
int analogValue = 0;

void setup() {
  pinMode(lightSensorPin, INPUT);
  
  Serial.begin(9600);
}

void loop(){
  analogValue = analogRead(lightSensorPin);
  if(analogValue < 20){            
    Serial.print("Lights off");
  }
  else if(analogValue >= 20 && analogValue <= 100){
    Serial.print("Lights on");
  }
  else{
    Serial.print("Lights off");
  }
  delay(5000);

}
