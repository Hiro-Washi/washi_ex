float p = 3.1415926;
void testlines(uint16_t color); 
void testdrawtext(char *text, uint16_t color); 
void testfastlines(uint16_t color1, uint16_t color2);
void testdrawrects(uint16_t color);
void testfillrects(uint16_t color1, uint16_t color2);
void testfillcircles(uint8_t radius, uint16_t color);
void testdrawcircles(uint8_t radius, uint16_t color);
void testtriangles();
void testroundrects();
void tftPrintTest();
void mediabuttons();
#include <ros.h>
#include <std_msgs/String.h>
#include <Adafruit_GFX.h>
#include <Adafruit_ST7735.h>
#include <SPI.h>
#define TFT_CS     6
#define TFT_RST    5
#define TFT_DC     7
#define TFT_SCLK 13
#define TFT_MOSI 11
#define display_width 160
#define display_height 80
Adafruit_ST7735 tft = Adafruit_ST7735(TFT_CS,  TFT_DC, TFT_RST);
int display_pixel_x, display_pixel_y,Offset_pixel=40;

ros::NodeHandle nh;
//std_msgs::String msg;
#define ROS_INFO_STREAM
//#define loginfo

// after receive chatter
void arduinoCB(const std_msgs::String& eye) {
    ROS_INFO_STREAM(eye.data);
    
    if (eye.data == "true") {
      Emoji("(^ ▽ ^)☆", ST7735_YELLOW);
    }
    else if (eye.data == "false") {
      Emoji("(x  o  x)", ST7735_BLUE);
    }
    else {
      void(0); //pass
    }
    delay(100);
}

ros::Subscriber<std_msgs::String> sub("eye", &arduinoCB );

void setup(void) {
    nh.initNode();
    nh.subscribe(sub);
    
    Serial.begin(9600);
    tft.initR(INITR_MINI160x80);
    //tft.setRotation(3);
    tft.fillScreen(ST7735_BLACK);
    
    Emoji("( o  _  o )", ST7735_WHITE);
    delay(1000);

    Serial.println(F("Initialized"));
    uint16_t time = millis();
    time = millis() - time;
    Serial.println(time, DEC);
    delay(500);
    tftPrintTest();
    delay(4000);
    tft.drawPixel(tft.width()/2, tft.height()/2, ST7735_GREEN);
    delay(500);
    testlines(ST7735_YELLOW);
    delay(500);
    testfastlines(ST7735_RED, ST7735_BLUE);
    delay(500);
    testdrawrects(ST7735_GREEN);
    delay(500);
    testfillrects(ST7735_YELLOW, ST7735_MAGENTA);
    delay(500);
    tft.fillScreen(ST7735_BLACK);
    testfillcircles(10, ST7735_BLUE);
    testdrawcircles(10, ST7735_WHITE);
    delay(500);
    testroundrects();
    delay(500);
    testtriangles();
    delay(500);
    mediabuttons();
    delay(500);
    Serial.println("done");
    delay(1000);
    
    tft.setTextSize(4);
    tft.print("ST7735");
    delay(500);
    }

void loop(void) {
    Emoji("( o  _  o )", ST7735_RED);
    Serial.print("Waiting for message...");
    nh.spinOnce();
    delay(100);
}

void Emoji(char *text, int16_t *color) {
    tft.setCursor(0, 0);
    tft.setTextSize(8);
    tft.setTextColor(color);
    tft.setTextWrap(true);
    tft.print(text);
}
