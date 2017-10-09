<h2 align="center">ROBOT Gym: Day 1</h2>
<h3 align="center">Getting Started </h3>
<p align="center">A quick look into ROS and installation </p>
<p align="center">May the fork be with you</p>
<p align="center">༼ つ ◕_◕ ༽つ</p>

# Table of Contents
- [Overview](#overview)
- [Installation](#installation)
- [Turtlesim](#turtlesim)
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
## Turtlesim

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
