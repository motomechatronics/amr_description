

<!-- GETTING STARTED -->
## amr_description

This is an example of an Autonomous Mobile Robot.

### Installation

Open a linux terminal, go to the _catkin_ws and type:

```sh 
 source devel/setup.bash  
  ```
go to the _catkin_ws/src_ directory and type as follow:

  ```sh
  git clone https://github.com/motomechatronics/amr_description.git
  git clone https://github.com/motomechatronics/aws_robomaker_small_warehouse_world.git
  
  ```
go to the _catlin_ws_ directory and type as follow:

  ```sh
  catkin_make
  
  ```
### Load the amr into the environment
In the terminal type as follow:
  ```sh
roslaunch amr_description amr_warehouse.launch  
  
  ```
to drive the robot you can open a new terminal and use the /cmd_vel topic or also run teleop_key package as:

  ```sh
rosrun teleop_twist_keyboard teleop_twist_keyboard.py

  
  ```
If you have not this package you may download it.
### download teleop_twist_keyboard package
to install _teleop_ type as follow:

  ```sh
sudo apt-get install ros-melodic-teleop-twist-keyboard
  
  ```

<p align="right">(<a href="#top">back to top</a>)</p>
