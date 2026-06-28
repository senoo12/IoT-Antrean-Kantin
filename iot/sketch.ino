#include <WiFi.h>
#include <HTTPClient.h>

const char* WIFI_SSID = "Wokwi-GUEST";
const char* WIFI_PASSWORD = "";

// URL endpoint FastAPI
const char* API_URL = "https://gscsh8qd-8000.asse.devtunnels.ms/sensor/data";

// Pin HC-SR04
const int TRIG_PIN = 5;
const int ECHO_PIN = 18;

// Device ID yang ada di database
const int DEVICE_ID = 1;

// ======================================================
// Membaca jarak sensor
// ======================================================
float readDistanceCM() {

  digitalWrite(TRIG_PIN, LOW);
  delayMicroseconds(2);

  digitalWrite(TRIG_PIN, HIGH);
  delayMicroseconds(10);

  digitalWrite(TRIG_PIN, LOW);

  long duration = pulseIn(ECHO_PIN, HIGH, 30000);

  // timeout
  if (duration == 0) {
    return -1;
  }

  return duration * 0.0343 / 2.0;
}

// ======================================================
// Setup
// ======================================================
void setup() {

  Serial.begin(115200);

  pinMode(TRIG_PIN, OUTPUT);
  pinMode(ECHO_PIN, INPUT);

  Serial.println();
  Serial.println("================================");
  Serial.println("Queue Monitoring IoT");
  Serial.println("================================");

  WiFi.begin(WIFI_SSID, WIFI_PASSWORD);

  Serial.print("Connecting WiFi");

  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }

  Serial.println();
  Serial.println("WiFi Connected");
  Serial.print("IP Address : ");
  Serial.println(WiFi.localIP());
}

// ======================================================
// Loop
// ======================================================
void loop() {

  float distance = readDistanceCM();

  if (distance < 0) {

    Serial.println("Sensor timeout!");
    delay(3000);
    return;
  }

  Serial.println("--------------------------------");
  Serial.print("Distance : ");
  Serial.print(distance);
  Serial.println(" cm");

  if (WiFi.status() != WL_CONNECTED) {

    Serial.println("WiFi Disconnected");

    WiFi.reconnect();

    delay(3000);

    return;
  }

  HTTPClient http;

  http.begin(API_URL);

  http.setTimeout(5000);

  http.addHeader("Content-Type", "application/json");

  String body =
      "{\"device_id\":" +
      String(DEVICE_ID) +
      ",\"distance_cm\":" +
      String(distance, 2) +
      "}";

  Serial.println("Sending JSON:");
  Serial.println(body);

  int httpCode = http.POST(body);

  Serial.print("HTTP Code : ");
  Serial.println(httpCode);

  if (httpCode > 0) {

    String response = http.getString();

    Serial.println("Response:");
    Serial.println(response);

  } else {

    Serial.print("POST Failed : ");
    Serial.println(http.errorToString(httpCode));

  }

  http.end();

  delay(5000);
}