import java.util.ArrayList;
import ketai.sensors.*;
import java.net.*;

KetaiSensor sensor;

float accelX, accelY, accelZ;
int sent = 0;
boolean didFlush;
int timer;

void setup() {
  size(1440, 2560);
  frameRate(60);
  sensor = new KetaiSensor(this);
  sensor.start();
  orientation(PORTRAIT);

  rectMode(CENTER);
  textFont(createFont("Arial", 96));
  textAlign(CENTER);
}

void draw() {
  background(0);
  text("x: " + accelX, width/2, height/5);
  text("y: " + accelY, width/2, 2*height/5);
  text("z: " + accelZ, width/2, height*3/5);
  text("sent: " + sent, width/2, height*4/5);
  
  timer--;
  
  if (didFlush && timer < 0) {
    sendFlush();
    timer = 180;
    didFlush = false;
  }
}

void onAccelerometerEvent(float x, float y, float z)
{
  accelX = -y;
  accelY = x;
  accelZ = z;
  if (abs(accelX) > 2.0) {
    didFlush = true;
  }
}

void sendFlush() {
  URL url;
  HttpURLConnection connection;
  String message = "";
  try {
    url = new URL("http", "flush-counter.herokuapp.com", 80, "do-flush-2");
    connection = (HttpURLConnection) url.openConnection();
    connection.setRequestMethod("GET");
    connection.connect();
    message = connection.getResponseMessage();
  } catch (Exception e) {
    System.out.println(e);
  }
  
  sent += 1;
}