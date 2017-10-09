<h2 align="center">ROBOT Gym: Day 1</h2>
<h3 align="center">Getting Started </h3>
<p align="center">A quick look into ROS and installation </p>
<p align="center">May the fork be with you</p>
<p align="center">༼ つ ◕_◕ ༽つ</p>

# Table of Contents
- [Overview](#overview)
- [Installation](#installation)

## Overview
Lorem Ipsum

## Installation
You can find more detailed instruction in the ROS Kinetic - Ubuntu installation [page](http://wiki.ros.org/kinetic/Installation/Ubuntu). 

### Configure your Ubuntu repositories
```
sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list'
```

### Set up your keys
```
sudo apt-key adv --keyserver hkp://ha.pool.sks-keyservers.net:80 --recv-key 421C365BD9FF1F717815A3895523BAEEB01FA116
```

### Make sure your packages are up-to-date
```
sudo apt-get update
```

### Desktop-Full installation
```
sudo apt-get install ros-kinetic-desktop-full
```

### Initialize rosdep
```
sudo rosdep init

rosdep update
```

### Environment setup
Add the ROS environment variable to your bash session
```
echo "source /opt/ros/kinetic/setup.bash" >> ~/.bashrc
```
Source the bash file
```
source ~/.bashrc
```

### Add dependencies for building packages
```
sudo apt-get install python-rosinstall python-rosinstall-generator python-wstool build-essential
```

### Installing individual packages
```
sudo apt install ros-kinetic-PACKAGE-NAME
```
