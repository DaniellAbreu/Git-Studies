#include <Arduino.h>

long readUltrassonicDistance(int trigPin, int echoPin){
    pinMode(trigPin, OUTPUT);
    digitalWrite(trigPin, LOW);
    delayMicroseconds(2);
    digitalWrite(trigPin, HIGH);
    delayMicroseconds(10);
    digitalWrite(trigPin, LOW);
    pinMode(echoPin, INPUT);

    return (pulseIn(echoPin, HIGH) * 0.017);
}

const int trigPin = 7;
const int echoPin = 8;
const int ledPin = 10;

void setup(){
    Serial.begin(9600);
    pinMode(ledPin, OUTPUT);
    digitalWrite(10, LOW);
}

void loop(){
  long distance = readUltrassonicDistance(7, 8);
    
    Serial.print("Distance: ");
    Serial.println(distance);
    
    if(distance < 20){
      digitalWrite(10, HIGH);
    }
    else{
      digitalWrite(10, LOW);
    }

    delay(60);
}