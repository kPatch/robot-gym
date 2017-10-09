<h2 align="center">ROBOT Gym: Day 1</h2>
<h3 align="center">Getting Started </h3>
<p align="center">A quick look into ROS and installation </p>
<p align="center">May the fork be with you</p>
<p align="center">༼ つ ◕_◕ ༽つ</p>

# Table of Contents
- [Overview](#overview)
- [Installation](#installation)
- [Turtlesim Local](#turtlesim-local)
- [Turtlesim Everyone!](#turtlesim-everyone)
- [Behind the Scenes](#behind-the-scenes)
  - [List topics](#view-all-topics)
  - [Echo topics](#echo-keyboard-messages)
  - [Topic rate](#topic-rate)
- [Resources](#resources)
## Overview
Lorem Ipsum

## Installation
You can find more detailed instruction in the ROS Kinetic - Ubuntu installation [page](http://wiki.ros.org/kinetic/Installation/Ubuntu). 

### 1. Configure your Ubuntu repositories
```
sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list'
```

### 2. Set up your keys
```
sudo apt-key adv --keyserver hkp://ha.pool.sks-keyservers.net:80 --recv-key 421C365BD9FF1F717815A3895523BAEEB01FA116
```

### 3. Make sure your packages are up-to-date
```
sudo apt-get update
```

### 4. Desktop-Full installation
```
sudo apt-get install ros-kinetic-desktop-full
```

### 5. Initialize rosdep
```
sudo rosdep init

rosdep update
```

### 6. Environment setup
Add the ROS environment variable to your bash session
```
echo "source /opt/ros/kinetic/setup.bash" >> ~/.bashrc
```
Source the bash file
```
source ~/.bashrc
```

### 7. Add dependencies for building packages
```
sudo apt-get install python-rosinstall python-rosinstall-generator python-wstool build-essential
```

### Installing individual packages
```
sudo apt install ros-kinetic-PACKAGE-NAME
```
## Turtlesim Local

### Package Installation
```
sudo apt install ros-kinetic-turtlesim
```
### 1. Run roscore
```
# In a new terminal:
roscore
```
### 2. Run turtlesim node
```
# In a new terminal
rosrun turtlesim turtlesim_node
```

### 3. Keyboard teleoperation
```
# In a new terminal
rosrun turtlesim turtle_teleop_key

# You should see the following:
# [ INFO] 1254264546.878445000: Started node [/teleop_turtle], pid [5528], bound on [aqy], xmlrpc port [43918], tcpros port [55936], logging to [~/ros/ros/log/teleop_turtle_5528.log], using [real] time
# Reading from keyboard
# ---------------------------
# Use arrow keys to move the turtle. 
```
Make sure that you select the terminal window that is running ```turtle_teleop_key```

![Turtlsim](http://wiki.ros.org/ROS/Tutorials/UnderstandingTopics?action=AttachFile&do=get&target=turtle_key.png)

## Turtlesim Everyone!

### 1. Set Environment Variables
```
# Get machine's IP address
ifconfig
```

```
# Open the .bashrc file
sudo gedit ~/.bashrc
```
```
# Edit/Add the following variables
export ROS_IP=YOUR_IP # Add your IP address here
export ROS_MASTER_URI=http://10.14.90.5:11311 # Wait for Irvin's instruction
```

### 2. Run turtlesim again
```
rosrun turtlesim turtlesim_node
```
### 3. Teleoperate using keyboard
```
rosrun turtlesim turtle_teleop_key
```
## Behind the Scenes
### View all topics
```
# In a new terminal
rostopic list
```
![rostopic list](https://github.com/kPatch/robot-gym/blob/master/day-1/res/rostopic-list.png)

### Echo keyboard messages
```
# In a new terminal
rostopic echo /turtle1/pose
```
![rostopic echo](https://github.com/kPatch/robot-gym/blob/master/day-1/res/rostopic-echo-turtlesim-keyboard.png)

Use your keyboard to move around and watch the value being 'echoed' into the terminal.

### Topic rate
```
# In a new terminal
rostopic hz /turtl1/pose
```

## Resources
- [ROS Tutorials](http://wiki.ros.org/ROS/Tutorials)
- [Turtlesim Tutorial](http://wiki.ros.org/turtlesim/Tutorials)
- [Understanding ROS Topics](http://wiki.ros.org/ROS/Tutorials/UnderstandingTopics)
