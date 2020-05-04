#include <Adafruit_Sensor.h>


/* 
 *************************************************************************************************************************
 * Occupod.ino - Arduino code for the bathroom sensor
 * Date: 27th April 2020
 * Written by: Daniel Ackuaku, for CS 300 Final Project 
 * Institution: Calvin University 
 * Professor : Dereck Schuurman 
 * 
 * Problem: After some reseash it became aparent that students at Calvin University who lived on campus
 * had no way to determine if their housemates/roomates were in the bathroom or not. In order to avoid being walked 
 * in on some students result to running the tap/shower to provide auditory feedback of their presence in the bathroom.
 * While effective this leads to gallons of water being wastedeach day.
 * 
 * Solution: A simple in-obtrusive systems on sensors that can adequately detect the presons of a person in the bathroom &
 * descretely displays this occupancy on an LCD screen outside the door. The sensor stored on a webserver and uploaded to 
 * a website for remote information access.
 * 
 * Hardware: - Arduino mega
 *           - Raspberry Pi 3 B+
 *           - LCD 16 x 2 character display
 *           - Temperature and Humidity Sensor 
 *           - Motion sensor 
 *           - Light Sensor 
 *                    
 * 
 * IoT onfrustructure: - SQLite
 *                     - Some other stuff (See lab 8).
 *                     
 **************************************************************************************************************************
 */

/**Include statements**/
#include "DHT.h" // Temperature and Humidity sensor library 


/*Constants*/
#define DHTPIN 7                   // Digital in from the temp& humid sensor pin
int buttonpin = 3;                   //define switch port 
int MOTIONSEN = 2;                 // choose the input pin (for PIR sensor)
int MOTIONSTATE = LOW;             // we start, assuming no motion detected
int VALUE = 0;                     // variable for reading the pin status
int lightSensorPin = A0;
int soundSensorPin = A2;            
int analogValueOfLights = 0;
int sensorValue = 0; // variable to store the value coming from the sensor 


/*Initialise the sensors*/
#define DHTTYPE DHT11 // Type of temperature humidity sensor in use 

// Initialize DHT sensor.
DHT TEMPHUMSENSOR(DHTPIN, DHTTYPE);


/** Function Definition **/
//int detectTemperature();
//int detectHumidity();
//unsigned char dectectMotion();
//unsigned char dectectLights();
//unsigned char detectPresence();



/** Function Declaration **/
/* 
 *  measures the temperature = in the bathroom
 * @param none
 * Return: void
 */
int detectTemperature(){
  int bathroomTemperature = TEMPHUMSENSOR.readTemperature();
//  Serial.print("Temperature: ");
  Serial.print(bathroomTemperature);
//  Serial.print("°C");
  Serial.print("\t"); 
  return bathroomTemperature;
 }


/* 
 *  measures the humidity in the bathroom
 * @param none
 * Return: void
 */
int detectHumidity(){
  int bathroomHumidity = TEMPHUMSENSOR.readHumidity();
// Serial.print("Humidity: ");
 Serial.print(bathroomHumidity);
// Serial.print(" %");
 Serial.print("\t");
// Serial.print("\n");
  return bathroomHumidity; 
 }

/* 
 * detects if motion has occured in the  bathroom
 * @param none
 * Return: void
 */
unsigned detectMotion(){
   VALUE = digitalRead(MOTIONSEN);       // read input value
  if (VALUE == MOTIONSTATE) {            // check if the input is HIGH
//     Serial.print("Motion: ");
     Serial.println(VALUE);
  } else {
//     Serial.print("Motion: ");
     Serial.println(VALUE);
  } 
  return VALUE;
 }


/* 
 * detects if motion has occured in the  bathroom
 * @param none
 * Return: void
 */
int detectLights(){
  analogValueOfLights = analogRead(lightSensorPin);
//  Serial.print("Light intensity: " );
  Serial.print(analogValueOfLights);
  Serial.print("\t");
  return analogValueOfLights;
}






/********************************* Main code ***********************************/
void setup() {
  // put your setup code here, to run once:
  TEMPHUMSENSOR.begin();
  pinMode(MOTIONSEN, INPUT);     // declare sensor as input
  pinMode(lightSensorPin, INPUT);
  pinMode(buttonpin,INPUT);//define switch as a output port 
  Serial.begin(9600);
}

void loop() {
  // Wait a few seconds between measurements.
  //delay(5000);
  int  light = detectLights();
  int temp = detectTemperature();
  int humid = detectHumidity();
  unsigned motion = detectMotion();
  // if (detectLights() >= 20 && detectHumidity() >= 50 && detectTemperature() >= 20) {
  //  Serial.println("Shower");
  // } else if (detectLights() >= 20 && detectHumidity() <= 50 && detectMotion() > 0){
  //  Serial.println("Toilet");
  // } else {
  //  Serial.println("Vaccant"); 
  // }
  delay(10000);               // 60 sec delay...
  
}
