/********************************************************************************
** Form generated from reading UI file 'dev_arduino.ui'
**
** Created by: Qt User Interface Compiler version 5.12.8
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_DEV_ARDUINO_H
#define UI_DEV_ARDUINO_H

#include <QtCore/QVariant>
#include <QtWidgets/QApplication>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_dev_arduino
{
public:

    void setupUi(QWidget *dev_arduino)
    {
        if (dev_arduino->objectName().isEmpty())
            dev_arduino->setObjectName(QString::fromUtf8("dev_arduino"));
        dev_arduino->resize(800, 600);

        retranslateUi(dev_arduino);

        QMetaObject::connectSlotsByName(dev_arduino);
    } // setupUi

    void retranslateUi(QWidget *dev_arduino)
    {
        dev_arduino->setWindowTitle(QApplication::translate("dev_arduino", "dev_arduino", nullptr));
    } // retranslateUi

};

namespace Ui {
    class dev_arduino: public Ui_dev_arduino {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_DEV_ARDUINO_H
