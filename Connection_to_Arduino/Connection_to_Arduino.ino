
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

String message = "";

void loop() {
  while(Serial.available() > 0)
  {
    char receivedChar = Serial.read();
    message = message + receivedChar;
  }
  if (message != "" && Serial.available() == 0)
  {
      Serial.println("Message:" + message);
  }
  lcd.setCursor(0,0);
  lcd.print(message);
}
