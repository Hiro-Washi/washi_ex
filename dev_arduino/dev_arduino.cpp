#include "dev_arduino.h"
#include "./ui_dev_arduino.h"

dev_arduino::dev_arduino(QWidget *parent)
    : QWidget(parent)
    , ui(new Ui::dev_arduino)
{
    ui->setupUi(this);
}

dev_arduino::~dev_arduino()
{
    delete ui;
}

