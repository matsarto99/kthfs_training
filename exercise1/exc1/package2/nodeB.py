#!/usr/bin/env python

import rospy
from std_msgs.msg import Float32
from std_msgs.msg import UInt16

def write_out(msg):
    pub = rospy.Publisher('/kthfs/result', Float32, queue_size=10)
    q = 0.15
    res = msg.data/q
    pub.publish(res)

def listener():
    rospy.init_node('nodeB', anonymous=True)
    rospy.Subscriber('sartori', UInt16, write_out)
    rospy.spin()

if __name__ == '__main__':
    listener()
