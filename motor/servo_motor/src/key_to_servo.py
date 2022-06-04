#!/usr/bin/env python3
import rospy
from std_msgs.msg import String
from std_msgs.msg import UInt16

key_mapping = { 'z': 0, 'x': 90, 'a': 180 }

def keysCB(msg, twist_pub):
    if len(msg.data) == 0 or not key_mapping.has_key(msg.data):
        return # unknown key.
    vels = key_mapping[msg.data]

    t = UInt16()
    t = vels
    publisher.publish(t)

if __name__ == '__main__':
    #keys_to_servoノード作成
    rospy.init_node('keys_to_servo')
    #servoトピックにUInt16型のメッセージを送る
    publisher = rospy.Publisher('servo', UInt16, queue_size=1)
    rospy.Subscriber('keys', String, keysCB, publisher)
    rospy.spin()

