#!/usr/bin/env python3
import rospy
from rtcm_msgs.msg import Message

def rtcm_callback(msg):
    pub_f9k.publish(msg)
    pub_f9p.publish(msg)

if __name__ == '__main__':
    rospy.init_node('rtcm_multiplexer')


    pub_f9k = rospy.Publisher('/ublox_f9k/ublox_gps/rtcm', Message, queue_size=10)
    pub_f9p = rospy.Publisher('/ublox_f9p/ublox_gps/rtcm', Message, queue_size=10)

    rospy.Subscriber("/rtcm", Message, rtcm_callback)

    rospy.spin()
