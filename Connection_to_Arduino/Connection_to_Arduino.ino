
#include <Wire.h>
#include <LiquidCrystal_I2C.h>

// Set the LCD address to 0x3F for a 16 chars and 2 line display
LiquidCrystal_I2C lcd(0x27, 16, 2);

void setup() {
  Serial.begin(9600);
  lcd.begin();
  lcd.backlight();
  lcd.clear();
}

void loop() {

  if(Serial.available() > 0)
  {
    input();
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
  for(int i = 0; i < 5; i++)
  {
    if(input[i] != "")
    {
      lcd.clear();
      lcd.setCursor(0,0); 
      lcd.print(input[i]);
      lcd.setCursor(0,1);
      lcd.print(input[i+1]);
      delay(400);
    }
  }
}
