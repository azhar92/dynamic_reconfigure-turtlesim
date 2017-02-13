#!/usr/bin/env python

PACKAGE = 'dynamic_tutorials'
import roslib;roslib.load_manifest(PACKAGE)
import rospy

import dynamic_reconfigure.client

from geometry_msgs.msg import Vector3, Twist

def callback(config):
	global pub,Zw,aw,bw,cw,dw,global_name,manual_name, parked_name, supervisory_name, autonomous_name, client
	print config
	global_name = config['bool_param']
	manual_name = config['Manual']
	parked_name = config['Parked']
	supervisory_name = config['Supervisory']
	autonomous_name = config['Autonomous']
	#global_name = not global_name
    #rospy.loginfo("Config set to {bool_param}".format(**config))
 


pub = rospy.Publisher('/turtle1/cmd_vel', Twist)    
aw = Twist(Vector3(1,0,0), Vector3(0,0,0))
bw = Twist(Vector3(-1,0,0), Vector3(0,0,0)) 
cw = Twist(Vector3(1,1,0), Vector3(0,0,1))
dw = Twist(Vector3(1,0,0), Vector3(0,0,-1))
Zw = Twist(Vector3(0,0,0), Vector3(0,0,0))


if __name__ == "__main__":
	rospy.init_node("dynamic_client")
	rospy.wait_for_service("/dynamic_tutorials/set_parameters")
	client = dynamic_reconfigure.client.Client("dynamic_tutorials", timeout=30, config_callback=callback)
	r = rospy.Rate(1)

	global_name = False
	manual_name = False
	parked_name = False
	supervisory_name = False
	autonomous_name = False
	
	#global_name = rospy.get_param("/dynamic_tutorials/bool_param") 
	#manual_name = rospy.get_param("/dynamic_tutorials/Manual")
	#parked_name = rospy.get_param("/dynamic_tutorials/Parked")
	#supervisory_name = rospy.get_param("/dynamic_tutorials/Supervisory")
	#autonomous_name = rospy.get_param("/dynamic_tutorials/Autonomous")
	
	while not rospy.is_shutdown():	     	
		if global_name == True: 
			if manual_name == True and parked_name == True and supervisory_name == True and autonomous_name == True:
				pub.publish(Zw)
			elif manual_name == True and parked_name == True and supervisory_name == True and autonomous_name == False:
				pub.publish(Zw)
			elif manual_name == True and parked_name == True and supervisory_name == False and autonomous_name == True:
				pub.publish(Zw)
			elif manual_name == True and parked_name == True and supervisory_name == False and autonomous_name == False:
				pub.publish(Zw)
			elif manual_name == True and parked_name == False and supervisory_name == True and autonomous_name == True:
				pub.publish(Zw)
			elif manual_name == True and parked_name == False and supervisory_name == True and autonomous_name == False:
				pub.publish(Zw)
			elif manual_name == True and parked_name == False and supervisory_name == False and autonomous_name == True:
				pub.publish(Zw)
			elif manual_name == True and parked_name == False and supervisory_name == False and autonomous_name == False:
				pub.publish(aw)
			elif manual_name == False and parked_name == True and supervisory_name == True and autonomous_name == True:
				pub.publish(Zw)
			elif manual_name == False and parked_name == True and supervisory_name == True and autonomous_name == False:
				pub.publish(Zw)	
			elif manual_name == False and parked_name == True and supervisory_name == False and autonomous_name == True:
				pub.publish(Zw)
			elif manual_name == False and parked_name == True and supervisory_name == False and autonomous_name == False:
				pub.publish(bw)
			elif manual_name == False and parked_name == False and supervisory_name == True and autonomous_name == True:
				pub.publish(Zw)
			elif manual_name == False and parked_name == False and supervisory_name == True and autonomous_name == False:
				pub.publish(cw)
			elif manual_name == False and parked_name == False and supervisory_name == False and autonomous_name == True:
				pub.publish(dw)
			elif manual_name == False and parked_name == False and supervisory_name == False and autonomous_name == False:
				pub.publish(Zw)	


		r.sleep()
