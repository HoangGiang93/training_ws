import rospy
import math
from giskardpy.python_interface import GiskardWrapper
 
# create goal joint state dictionary
goal_js = {'ur5_shoulder_pan_joint':0, 'ur5_shoulder_lift_joint':-math.pi/2, 'ur5_elbow_joint':0, 'ur5_wrist_1_joint':0, 'ur5_wrist_2_joint':0, 'ur5_wrist_3_joint':0}
 
# init ros node
rospy.init_node(u'test')
 
# create a GiskardWrapper object and execute the joint goal
giskard_wrapper = GiskardWrapper()
giskard_wrapper.set_joint_goal(goal_js)
giskard_wrapper.plan_and_execute()
