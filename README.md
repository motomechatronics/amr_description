# amr_description
##Autonomous Mobile Robot

to download the amr:

go to catkin_ws/src
>git clone https://github.com/motomechatronics/amr_description.git

go to catkin_ws

>catkin_make

to load the amr into the environment:

>roslaunch amr_description amr_warehouse.launch  

download teleop key

>sudo apt-get install ros-melodic-teleop-twist-keyboard

open another shell

>rosrun teleop_twist_keyboard teleop_twist_keyboard.py
