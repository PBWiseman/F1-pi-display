
#include <Wire.h>
#include <LiquidCrystal_I2C.h>
#include <Adafruit_NeoPixel.h>

LiquidCrystal_I2C screens[3] =
{
  LiquidCrystal_I2C(0x27, 16, 2),
  LiquidCrystal_I2C(0x26, 16, 2),
  LiquidCrystal_I2C(0x23, 16, 2)
};

#define MATRIX_WIDTH 5
#define MATRIX_HEIGHT 6
#define MATRIX_PIN 10
#define NUM_PIXELS MATRIX_WIDTH * MATRIX_HEIGHT

Adafruit_NeoPixel matrix = Adafruit_NeoPixel(NUM_PIXELS, MATRIX_PIN, NEO_GRB + NEO_KHZ800);

bool buttonStates[6] = {false, false, false, false, false, false};

int buttonPins[6] = {3,4,5,6,7,8};

void setup() {
  Serial.begin(9600);
  matrix.begin();
  matrix.setBrightness(5);
  for (int y = 0; y < MATRIX_HEIGHT; y++)
  {
    for (int x = 0; x < MATRIX_WIDTH; x++)
    {
      int pixel = xyToPixel(x, y);
      matrix.setPixelColor(pixel, matrix.Color(0,0,0)); //Clear screen
    }
  }
  matrix.show();
  for(int i = 0; i < 6; i++)
  {
    pinMode(buttonPins[i], INPUT_PULLUP);
  }
  for (int i = 0; i < 3; i++)
  {
    screens[i].begin();
    screens[i].backlight();
    screens[i].clear();
    screens[i].setCursor(0,0);
    screens[i].print("Test");
    screens[i].setCursor(0,1);
    screens[i].print("Test");
  }
}

void loop() {

  if(Serial.available() > 0)
  {
    input();
  }
  for(int i = 0; i < 6; i++)
  {
    if (digitalRead(buttonPins[i]) == LOW && buttonStates[i] == false)
    {
      Serial.println(i);
    }
    if (digitalRead(buttonPins[i]) == LOW)
    {
      buttonStates[i] = true;
    }
    else
    {
      buttonStates[i] = false;
    }
  } 
}

void input()
{
  String message[6];
  char sectors[6][5];
  int i = 0;
  int j = 0;
  bool sectorsAssigning = false;
  while(true)
  {
    if(Serial.available() > 0)
    { 
      char receivedChar = Serial.read();
      if (receivedChar == '@')
      {
        break;
      }
      else if (receivedChar == '%')
      {
        sectorsAssigning = true;
        j = 0;
      }
      else if(receivedChar == '&')
      {
        i++;
        sectorsAssigning = false;
      }
      else
      {
        if (sectorsAssigning)
        {
          sectors[i][j] = receivedChar;
          j++;
        }
        else
        {
          message[i] = message[i] + receivedChar;
        }
      }
    }
  }
  printToScreen(message, sectors);
}

void printToScreen(String input[6], char sectors[6][5])
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
  for (int y = 0; y < 6; y++)
  {
    for (int x = 0; x < 5; x++)
    {
      int currentPixel = xyToPixel(x,y);
      switch(sectors[y][x])
      {
        case 'P':
          matrix.setPixelColor(currentPixel, matrix.Color(255,0,255));
          break;
        case 'Y':
          matrix.setPixelColor(currentPixel, matrix.Color(255,255,0));
          break;
        case 'G':
          matrix.setPixelColor(currentPixel, matrix.Color(0,255,0));
          break;
        case 'R':
          matrix.setPixelColor(currentPixel, matrix.Color(255,0,0));
          break;
        case 'B':
          matrix.setPixelColor(currentPixel, matrix.Color(0,0,255));
          break;
        case 'W':
          matrix.setPixelColor(currentPixel, matrix.Color(255,255,255));
          break;
        default:
          matrix.setPixelColor(currentPixel, matrix.Color(0,0,0));
      }
    }
  }
  matrix.show();
}

//Credit for this to Connell from our LED Project
int xyToPixel(int x, int y)
{
  if (y % 2 == 0)
  {
    //Even rows
    return y * MATRIX_WIDTH + (MATRIX_WIDTH - 1 - x);
  } else {
    //Odd rows
    return y * MATRIX_WIDTH + x;
  }
}
