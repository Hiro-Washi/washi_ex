:motor_right.py
#!/usr/vin/env python
# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO 
import rospy, time
from std_msgs.msg import Int64

class motor_command():
    def __init__(self):
        self.RotationDirect = True # Forward
        self.Stop = False          # Forward
        self.Enable = True
        self.pin_num_PWM = 18      # pin name
        self.pin_num_RotatetionDirect = 15
        self.pin_num_Enable = 14
        self.pin_num_Stop = 23
        self.freq = 50              # Hz (PWM のパルスを一秒間に 50 個生成)
        #ノード立ち上げ（ROS）
        rospy.init_node('maxon_test')
        rospy.Subscriber('right_motor/cmd_vel', Int64, self.callback)
        rospy.loginfo('Ready to receive motor command')

        GPIO.setmode(GPIO.BCM) # inicialize GPIO
        # setup for GPIL. set GPIO to desital output
        GPIO.setup(self.pin_num_PWM, GPIO.OUT)
        GPIO.setup(self.pin_num_RotatetionDirect, GPIO.OUT)
        GPIO.setup(self.pin_num_Enable, GPIO.OUT)
        GPIO.setup(self.pin_num_Stop, GPIO.OUT)

        GPIO.output(self.pin_num_RotatetionDirect,GPIO.LOW)
        GPIO.output(self.pin_num_Enable, GPIO.LOW)
        GPIO.output(self.pin_num_Stop, GPIO.HIGH)
        self.pwm = GPIO.PWM(self.pin_num_PWM, self.freq)
        duty = 0.0
        self.pwm.start(duty)

    def motor_main(self):
        rospy.spin()
        # cleanup
        GPIO.cleanup()
        rospy.loginfo('finish rotate')
        self.pwm.stop()

    def callback(self, data):
        self.rpm_cdatammand = data.t
        GPIO.cleanup() #片付け
        rospy.loginfo('回転終了')
        self.pwm.stop() #終了

    def callback(self, data):
        self.rpm_command = data.data #rpmで取得
        rospy.loginfo(self.rpm_command)
        duty_command = self.rpm2duty(self.rpm_command) #rpm→duty比へ（制約考慮）
        rospy.loginfo('motor command is '+ str(duty_command))
        #PINいじり
        if duty_command >= 0: #正逆回転
            self.RotationDirect = True
        else:
            self.RotationDirect = False #逆回転
            rospy.loginfo('Reverse')
            duty_command = -duty_command

        if self.RotationDirect:
            GPIO.output(self.pin_num_RotationDirect,GPIO.HIGH)
        else:
            GPIO.output(self.pin_num_RotationDirect,GPIO.LOW)

        if self.Stop:
            GPIO.output(self.pin_num_Stop, GPIO.HIGH)
        else:
            GPIO.output(self.pin_num_Stop, GPIO.LOW)

        if self.Enable:
            GPIO.output(self.pin_num_Enable, GPIO.HIGH)
        else:
            GPIO.output(self.pin_num_Enable, GPIO.LOW)

        rospy.loginfo('Change Command')

        self.pwm.ChangeDutyCycle(duty_command) #回転量を変える

    def rpm2duty(self, rpm):
        max_rpm = 6000  #規定値90%
        max_duty = 90
        min_rpm = 0  #規定値10%
        min_duty = 10
        rpm_rate = (max_rpm-min_rpm)/(max_duty-min_duty) #1%に対するrpm
        if rpm >= 0:
            duty = rpm / rpm_rate + min_duty
        else:
            duty = rpm / rpm_rate - min_duty  
        #速度制約
        if duty > 90:
            rospy.loginfo('Speed limit!!')
            duty = 90
        elif duty < -90:
            rospy.loginfo('Speed limit!!')
            duty = -90
        return duty

if __name__ == '__main__': #これがメイン実行file
    Motor_Command = motor_command()
    Motor_Command.motor_main()
        #pubする場合の参考
        #rostopic pub right_motor/cmd_vel std_msgs/Int64 "data: 10

