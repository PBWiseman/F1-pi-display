
#include <Wire.h>
#include <LiquidCrystal_I2C.h>

LiquidCrystal_I2C screens[3] =
{
  LiquidCrystal_I2C(0x27, 16, 2),
  LiquidCrystal_I2C(0x26, 16, 2),
  LiquidCrystal_I2C(0x25, 16, 2)
};

int buttonPins[6] = {3,4,5,6,7,8};

void setup() {
  Serial.begin(9600);
  for(int i = 0; i < 6; i++)
  {
    pinMode(buttonPins[i], INPUT_PULLUP);
  }
  for (int i = 0; i < 3; i++)
  {
    screens[i].begin();
    screens[i].backlight();
    screens[i].clear();
  }
}

void loop() {

  if(Serial.available() > 0)
  {
    input();
  }
  for(int i = 0; i < 6; i++)
  {
    if (digitalRead(buttonPins[i]) == LOW)
    {
      Serial.println(i);
    }
  } 
}

void input()
{
  String message[6];
  int i = 0;
  while(Serial.available() > 0)
  {
    char receivedChar = Serial.read();
    if(receivedChar == '&')
    {
      Serial.println("Received line: " + message[i]);
      i++;
      if(i > sizeof(message))
      {
        i == sizeof(message);
      }
    }
    else
    {
      message[i] = message[i] + receivedChar;
    }
  }
  if (Serial.available() == 0)
  {
      Serial.println("Received line: " + message[i]);
      Serial.println("Done");
  }
  printToScreen(message);
}

void printToScreen(String input[6])
{
  int line = 0;
  for (int i = 0; i < 3; i++)
  {
    screens[i].clear();
    screens[i].setCursor(0,0);
    screens[i].print(input[line]);
    line++;
    screens[i].setCursor(0,1);
    screens[i].print(input[line]);
    line++;
  }
}
