#include <LiquidCrystal.h>
LiquidCrystal lcd(4, 5, 10, 11, 12, 13); 

const int numRows = 2;
const int numCols = 16;

int col = 0;
int row = 0;

char ch;

void setup() {
  lcd.begin(numCols, numRows);
  lcd.clear();
  Serial.begin(9600);
}


void loop() {
  lcd.setCursor(col, row);  
  
  if (Serial.available()) {
    ch = Serial.read();
    if(!isSpecialCharacter(ch)) {
      lcd.write(ch);
      calcColRow();
      
      lcd.setCursor(col, 0);  
    } 
  }
  
  delay(500);

}

// check if character is special
boolean isSpecialCharacter(char ch) {
  return (ch==0x0a)||(ch==0x0d);
}

// where to move cursor
void calcColRow() {
  col++;
  if (col>15) {
    if ((row==0)) {
      col = 0;
      row = 1;
    } else {
      col = 0;
      row = 0;
      lcd.clear();
    } 
  }
}
