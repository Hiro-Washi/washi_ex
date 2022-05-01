#include <ros.h>
#include <std_msgs/Empty.h>

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
int16_t max_result;
float pi = 3.145926;
int speed = 9600;

ros::NodeHandle nh;

void CallBack(const std_msgs::Empty& blink_msg) {
    text("^ ▽ ^", YELLOW);
    delay(100);
}

ros::Subscriber<std_msgs::Empty> s("blink_msg", CallBack );

void setup(void) {
    nh.initNode();
    nh.advertise("chatter", &) /////
    
    Serial.begin(speed);
    tft.initR(INITR_MINI160x80);
    //tft.setRotation(3);
    tft.fillScreen(ST7735_BLACK);
    
    testdrawtext("( o  _  o )", ST7735_WHITE);
    delay(1000);
    
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
    tft.text("( o  _  o )")
    Serial.printin("Waiting for message...")
    deley(500)
}

void Emoji(char *text, unit16_t *color) {
    tft.setCursor(0, 0);
    tft.setTextSize(8);
    tft.setColor(color);
    tft.setTextWrap(true);
    tft.print();
}

int16_t MaxUpdate(int16_t)
