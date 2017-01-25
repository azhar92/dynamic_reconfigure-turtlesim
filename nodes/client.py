#!/usr/bin/env python

PACKAGE = 'dynamic_tutorials'
import roslib;roslib.load_manifest(PACKAGE)
import rospy

import dynamic_reconfigure.client

from geometry_msgs.msg import Vector3, Twist

def callback(config):
    rospy.loginfo("Config set to {int_param}, {double_param}, {str_param}, {bool_param}, {size}".format(**config))

if __name__ == "__main__":
    rospy.init_node("dynamic_client")
    pub = rospy.Publisher('/turtle1/cmd_vel', Twist)
    rospy.wait_for_service("/dynamic_tutorials/set_parameters")
    tw = Twist(Vector3(0.5,0,0), Vector3(0,0,0.5))
    client = dynamic_reconfigure.client.Client("dynamic_tutorials", timeout=30, config_callback=callback)

    r = rospy.Rate(1)
    x = 0
    b = False
    while not rospy.is_shutdown():
        x = x+1
        if x>5:
            pub.publish(tw) 
            #  print "rostopic pub /turtle1/cmd_vel geometry_msgs/Twist -r 1 -- '[2.0, 0.0, 0.0]' '[0.0, 0.0, 0.5]'"
            x=0

#b = not b
        client.update_configuration({"int_param":x, "double_param":(1/(x+1)), "str_param":str(rospy.get_rostime()), "bool_param":b, "size":1})
        r.sleep()
