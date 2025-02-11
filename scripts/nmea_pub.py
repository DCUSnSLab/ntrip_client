#!/usr/bin/env python3
import rospy
from nmea_msgs.msg import Sentence

def nmea_publisher():
    # ROS 노드 초기화
    rospy.init_node('nmea_publisher_node', anonymous=True)
    
    # 발행자 설정, 'nmea_sentence' 토픽에 nmea_msgs/Sentence 메시지 타입을 사용
    pub = rospy.Publisher('ntrip_client/nmea', Sentence, queue_size=10)
    
    # 주기 설정
    rate = rospy.Rate(1)  # 1Hz

    while not rospy.is_shutdown():
        # NMEA 문장 생성
        nmea_sentence = Sentence()
        nmea_sentence.header.stamp = rospy.Time.now()
        nmea_sentence.header.frame_id = ""
        # nmea_sentence.sentence = "$GPGGA,085723.919,3554.842,N,12848.203,E,1,12,1.0,0.0,M,0.0,M,,*6B\r\n" # 대가대
        nmea_sentence.sentence = "$GPGGA,065201.798,3717.326,N,12706.431,E,1,12,1.0,0.0,M,0.0,M,,*69\r\n" # 용인운전면허시험장
        # nmea_sentence.sentence = "$GPGGA,121305.984,3314.565,N,12625.487,E,1,12,1.0,0.0,M,0.0,M,,*65\r\n" # 제주도
        
        # 문장 발행
        pub.publish(nmea_sentence)
        rospy.loginfo("Published NMEA Sentence: %s" % nmea_sentence.sentence)
        
        # 주기 대기
        rate.sleep()

if __name__ == '__main__':
    try:
        nmea_publisher()
    except rospy.ROSInterruptException:
        pass