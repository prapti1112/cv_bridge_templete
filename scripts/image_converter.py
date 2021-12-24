#!/usr/bin/env python

import rospy
import cv2
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
# from cv_bridge.boost.cv_bridge_boost import getCvType

class ImageConverter():
    def __init__(self, nodeType='both'):
        self.bridge = CvBridge()
        if nodeType == 'pub' or nodeType == 'both':
            self.img_pub = rospy.Publisher('camera_image/raw', Image, queue_size=10)
        if nodeType == 'sub' or nodeType == 'both':
            self.img_sub = rospy.Subscriber('camera_image/raw', Image, self.callback)
    
    def callback(self, data):
        try:
            cv_img = self.bridge.imgmsg_to_cv2(data)
            cv2.imshow("Live Stream in subscriber", cv_img)
            cv2.waitKey(1)
        except CvBridgeError as err:
            print("Error occured in converting image to cv2 format - " + str(err))

    def publish(self, cv_img):
        # rospy.loginfo(f"Image recieved: {cv_img}")
        # cv2.imshow("Image recevied in publisher", cv_img)
        try:
            self.img_pub.publish(self.bridge.cv2_to_imgmsg(cv_img))
        except CvBridgeError as err:
            print("Error occured in converting image from cv2 to Image format - " + str(err))
        except:
            print("Error occured in publishing image")