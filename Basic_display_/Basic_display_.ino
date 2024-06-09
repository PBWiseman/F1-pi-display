#include <Wire.h>
#include <LiquidCrystal_I2C.h>

// Set the LCD address to 0x3F for a 16 chars and 2 line display
LiquidCrystal_I2C lcd(0x27, 16, 2);

class Driver {
  public:
  String code;
  String firstName;
  String lastName;
  String number;
  String team;
  String teamCode;
};

Driver drivers[20];

void setup()
{
  drivers[0] = {"VER", "Max", "Verstappen", "1", "Red Bull", "RBR "};
  drivers[1] = {"NOR", "Lando", "Norris", "4", "McLaren", "MCL "};
  drivers[2] = {"HAM", "Lewis", "Hamilton", "44", "Mercedes", "MERC"};
  lcd.begin();
  lcd.backlight();
}

void loop()
{
  lcd.setCursor(0,0);
  printDriver("1", drivers[0]);
  lcd.setCursor(0,1);
  printDriver("2", drivers[1]);
  delay(4000);
  lcd.setCursor(0,0);
  printDriver("2", drivers[1]);
  lcd.setCursor(0,1);
  printDriver("3", drivers[2]);
  delay(4000);
  lcd.setCursor(0,0);
  printDriver("3", drivers[2]);
  lcd.setCursor(0,1);
  printDriver("1", drivers[0]);
  delay(4000);
}

void printDriver(String place, Driver driver)
{
  lcd.print("P" + place + " - " + driver.teamCode + " - " + driver.code);
}