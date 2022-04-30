#ifndef DEV_ARDUINO_H
#define DEV_ARDUINO_H

#include <QWidget>

QT_BEGIN_NAMESPACE
namespace Ui { class dev_arduino; }
QT_END_NAMESPACE

class dev_arduino : public QWidget
{
    Q_OBJECT

public:
    dev_arduino(QWidget *parent = nullptr);
    ~dev_arduino();

private:
    Ui::dev_arduino *ui;
};
#endif // DEV_ARDUINO_H
