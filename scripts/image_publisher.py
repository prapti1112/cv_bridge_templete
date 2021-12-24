#!/usr/bin/env python

import rospy
import cv2
import image_converter

def img_publisher():
    
    ic_pub = image_converter.ImageConverter(nodeType='pub')
    rospy.init_node('img_publisher', anonymous=True)
    rate = rospy.Rate(10)

    while not rospy.is_shutdown():
        ret, frame = cap.read()
        # rospy.loginfo('Camera capture Status:' + str(ret))
        if ret and frame.data[-2:] != '\x80\x80':
            cv2.imshow("Video after starting", frame)
            ic_pub.publish(frame)
        
        cv2.waitKey(1)
        rate.sleep()
    
    try:
        cap.release()
    except:
        pass
    cv2.destroyAllWindows()

if __name__ == "__main__":
    cap = cv2.VideoCapture(0)
    try:
        img_publisher()
    except KeyboardInterrupt:
        print("Shutting down.....")
    except rospy.ROSInterruptException:
        pass