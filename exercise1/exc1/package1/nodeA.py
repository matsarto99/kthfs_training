#!/usr/bin/env python

import rospy
from std_msgs.msg import UInt16

def talker():
    pub = rospy.Publisher('sartori',UInt16,queue_size=10)
    rospy.init_node('nodeA', anonymous=True)
    rate = rospy.Rate(20)   # Hz
    n = 4
    k = 0
    while not rospy.is_shutdown():
        k = k+4
        rospy.loginfo(k)
        pub.publish(k)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
