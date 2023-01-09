#!/usr/bin/env python

import sys
import rospy
from haru_smart_home.srv import Learning

def learning_client(desired_state):
    rospy.wait_for_service('learning')

    try:
        learning = rospy.ServiceProxy('learning',  Learning)
        res = learning(desired_state)
        return res
    except rospy.ServiceException as e:
        print('Service called failed: ', e)

if __name__ == '__main__':
    if len(sys.argv) == 2:
        if sys.argv[1] ==  'on':
            learning_client('on')
        elif sys.argv[1] ==  'off':
            learning_client('off')
        else:
            print('You have to use either "on" or "off" as state.')
    else:
        print("Usage: rosrun haru_smart_home learning.py <on> | <off>")
        sys.exit(1)

    
    
