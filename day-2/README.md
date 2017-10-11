<h2 align="center">ROBOT Gym: Day 2</h2>
<h3 align="center">Turtlebot and MOVR</h3>
<p align="center">Teleoperation and Code Review</p>
<p align="center">May the fork be with you</p>
<p align="center">༼ つ ◕_◕ ༽つ</p>

# Table of Contents
- [Overview](#overview)
- [Installation](#installation)
- [Turtlebot](#turtlebot)
- [Resources](#resources)

## Overview

Today's session will go the basic of publishers and subscribers through the use of Turtlebot.
We will further revivew [MOVR's](https://github.com/ATR-Lab/movr_ws) source to code to understand what it takes to write a publisher and a subscriber in Python and Arduino.

## Installation 

```
# In a new terminal, run the following command:

$ sudo apt install ros-kinetic-turtlebot
```

```
# In a new terminal, run the following command:

$ sudo apt install ros-kinetic-turtlebot-teleop
```

## Turtlebot

[TurtleBot](http://wiki.ros.org/Robots/TurtleBot) is a low-cost, personal robot kit with open-source software. 
TurtleBot was created at Willow Garage by Melonee Wise and Tully Foote in November 2010. With TurtleBot, you’ll be able to build a robot that can drive around your house, see in 3D, and have enough horsepower to create exciting applications.

The TurtleBot kit consists of a mobile base, 2D/3D distance sensor, laptop computer or SBC(Single Board Computer), and the TurtleBot mounting hardware kit. In addition to the TurtleBot kit, users can download the TurtleBot SDK from the ROS wiki. TurtleBot is designed to be easy to buy, build, and assemble, using off the shelf consumer products and parts that easily can be created from standard materials. As an entry level mobile robotics platform, TurtleBot has many of the same capabilities of the company’s larger robotics platforms, like PR2.

### About
ROS follows a [peer-to-peer](https://en.wikipedia.org/wiki/Peer-to-peer) paradigm. 
It consists of small computer programs that communicate with one another through the exchange of ```messages```.
At a *high-level* theses messages travel through the internet with a central routing service.
In ROS these, small computer programs are called ```nodes```.   

As we mentioned in day 1, ROS provides us with many tools for tasks such as visualizing system interconnection, logging data and visualizing data.
ROS supports languages such as Python, C++ and MATLAB.

### 1. Run roscore

In the latter section, we mentioned that at a *high-level* these ```nodes``` communicate with each other without the need for central routing service.
But, underneath the hood ROS provides with the plumbing (software) needed to allow nodes to find each other and send messages. 
This plumbing comes in the form of the ```roscore``` service.   

Every ode connects to ```roscore``` at startup and registers the details of the message streams it needs to publish and the streams it wishes to subscribe.   

```roscore``` essentially acts as broker service that allows nodes to register and find other nodes.   
One these nodes have gone through ```roscore```, they communiate peer-to-peer.

When a ROS nodes starts up, it expects its process to have an environment variable called ```ROS_MASTER_URI```.  

```
export ROS_MASTER_URI=http://10.14.90.5:11311/
```

This indicates that ```roscore``` is running at the IP address ```10.14.90.5``` and is accessible though port 11311.   

With this information, nodes can register themselves with ```roscore``` upon startup and query ```roscore``` to find other nodes and data streams by name.   

Because our system communicates peer-2-peer, this means that we can different nodes across different computers and all we need to worry about is having ```ROS_IP``` and ```ROS_MASTER_URI``` configured.   
Hence, we can split our system in two: our **workstation** and the **robot**.

In this tutorial, we will assume that our workstation will run ```roscore``` and our robot will simply subscribe to any ```messages``` it needs.

In the case of Turtlebot, we will need to run the ```roscore``` service in our workstation and then launch the ```node``` that *bringsup* Turtlebot.

Before we begin, make sure that all terminals are closed.

```
# In a new terminal, run the following command:
# Note that roscore could be ran in the robot, or the workstation.

$ roscore
```

### 2. Bring up Turtlebot

``` 
# In a new terminal, in Turtlebot, run the following command:

$ roslaunch turtlebot_bringup minimal.launch 
```

### 3. Teleoperate Turtlebot
```
# In a new terminal, run the following command:

$ roslaunch turtlebot_teleop keyboard_teleop.launch
```
