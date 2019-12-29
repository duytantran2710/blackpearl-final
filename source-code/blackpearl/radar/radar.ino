// Sweep
// by BARRAGAN <http://barraganstudio.com> 

#include <Servo.h> 
#define trigPin 10
#define echoPin 11

Servo myservo;  // create servo object to control a servo 
                // a maximum of eight servo objects can be created 
 
int pos = 0;    // variable to store the servo position 

void setup() { 
  Serial.begin(9600);
  myservo.attach(9);  // attaches the servo on pin 9 to the servo object 
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
} 
 
 
void loop() { 
    rotateServo();
} 

void rotateServo() {
  int distance;
  myservo.write(15);

  for(pos = 15; pos < 165; pos++) {
    myservo.write(pos); 
    distance = getDistance();
    print(distance,pos);
    delay(30);
  }
  for(pos = 165; pos >= 15; pos--) {
    myservo.write(pos);
    distance = getDistance();
    print(distance,pos);
    delay(30);
  } 
}

int getDistance() {
  int duration, distance;
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(1000);
  digitalWrite(trigPin, LOW);
  duration = pulseIn(echoPin, HIGH);
  
  distance = (duration/2) / 29.1;
  
  return distance;
}

void print(int distance, int pos) {
  Serial.print(distance);
  Serial.print(",");
  Serial.println(pos);
}
