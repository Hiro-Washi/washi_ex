#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
from std_msgs.msg import String


class eyesTestPub
    def __init__(self):
        rospy.Subscriber('/eyes/right', String, self.moveEyes)
        "self.eyes_reciever = rospy.Subscriber(''"
    
    def moveEyes(self






class MotorController(object):
    def __init__(self):

        self.motor_client = rospy.ServiceProxy('/dynamixel_workbench/dynamixel_command',DynamixelCommand)


    def degToStep(self,deg):
        return int((deg+180)/360.0*4095)

    def setPosition(self, motor_id, position_value):
        if type(position_value) == type(float()):
            rotate_value = self.degToStep(positionon_value)
        res = self.motor_client('', motor_id, 'Goal_Position', position_value)

class JointController(MotorController):
    def __init__(self):
        super(JointController,self).__init__()
        rospy.Subscriber('/servo/endeffector',Bool,self.controlEndeffector)
        rospy.Subscriber('/servo/head',Float64,self.controlHead)
        
def controlHead(self,deg):
        try:
            deg = deg.data
        except AttributeError:
            pass
        deg *= self.gear_ratio[5]
        step = self.degToStep(deg) + (self.origin_angle[5]-2048)
        self.setPosition(5, step)