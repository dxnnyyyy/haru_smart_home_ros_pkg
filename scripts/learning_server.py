#!/usr/bin/env python

import rospy
import requests
from haru_smart_home.srv import Learning, LearningResponse

base_url = "http://10.0.2.2:8123/api/services/scene/turn_on"
headers = {"Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiI1MzBiMzU1ZDA5MmM0NmJmOGEwNzdiNmRiMjdlNGJkNSIsImlhdCI6MTY3MTgwNDA0MCwiZXhwIjoxOTg3MTY0MDQwfQ.LI36cDnbbtoll_jJNSSpM5CIJ7huSx6A7DiXMpsHyak"}

def handle_learning_environment(req):
    try:
        if req.desired_state == 'on':
            data = {"entity_id": "scene.haru"}
        
        if req.desired_state == 'off':
            data = {"entity_id": "scene.haru_off"}
        
        rest_res = requests.post(base_url, headers=headers, json=data)
        print(rest_res)
        return LearningResponse('Set state to ' + req.desired_state)
    except:
        print('error')
    

def learning_server():
    rospy.init_node('learning_server')
    s = rospy.Service('learning', Learning, handle_learning_environment)
    print('Ready to handle learning environment')
    rospy.spin()

if __name__ == '__main__':
    learning_server()