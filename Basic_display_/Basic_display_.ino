#include <Wire.h>
#include <LiquidCrystal_I2C.h>

// Set the LCD address to 0x3F for a 16 chars and 2 line display
LiquidCrystal_I2C lcd(0x27, 16, 2);
LiquidCrystal_I2C lcd2(0x26, 16, 2);

class Driver {
  public:
  String tla;
  String number;
  String teamCode;
};

Driver drivers[8];
int adjustedNum;

void setup()
{
  drivers[0] = {"VER", "1", "RBR "};
  drivers[1] = {"GAS", "10", "ALP "};
  drivers[2] = {"NOR", "4", "MCL "};
  drivers[3] = {"PIA", "81", "MCL "};
  lcd.begin();
  lcd.backlight();
  lcd.clear();
  lcd2.clear();
  lcd.setCursor(0,0);
  printDriver(1, drivers[0]);
  lcd.setCursor(0,1);
  printDriver(2, drivers[1]);
  lcd2.setCursor(0,0);
  printDriverScreen2(3, drivers[2]);
  lcd2.setCursor(0,1);
  printDriverScreen2(4, drivers[3]);
  delay(2000);
}

void loop()
{

}

void printDriver(int place, Driver driver)
{
  lcd.print("P" + String(place) + " - " + driver.teamCode + " - " + driver.tla);
}
void printDriverScreen2(int place, Driver driver)
{
  lcd2.print("P" + String(place) + " - " + driver.teamCode + " - " + driver.tla);
}
