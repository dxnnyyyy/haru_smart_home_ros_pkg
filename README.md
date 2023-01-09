# Haru Smart Home - ROS Package

## installation
1. clone this repo in your ```~/catkin_ws/src/``` folder
1. run ```catkin_make``` in your catkin workspace (usually this is ```~/catkin_ws```)

## starting
1. open up a terminal make sure that it is sourced with the ros stuff (if not, run ```source ~/catkin_ws/devel/setup.bash```)
1. start roscore by running ```roscore```
1. open up second terminal (make sure it's sourced)
1. in the second terminal run ```rosrun haru_smart_home learning_server.py```
1. open up third terminal (make sure it's sourced)
1. in the third terminal you can now run either ```rosrun haru_smart_home learning_client.py on``` to activate the learning environment or ```rosrun haru_smart_home learning_client.py off``` to deactivate it
