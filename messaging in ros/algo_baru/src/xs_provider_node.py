#!/usr/bin/env python3

import rospy
from std_msgs.msg import Int16
import random

if __name__ == '__main__':
    rospy.init_node('xs_provider_node')
    rospy.loginfo('Node xs_provider started')
    pub = rospy.Publisher('/XS', Int16, queue_size=10)
    rate = rospy.Rate(1)
    while not rospy.is_shutdown():
        data = random.randint(0, 100)
        rospy.loginfo("XS Sending data: %s" % data)
        pub.publish(data)
        rate.sleep()