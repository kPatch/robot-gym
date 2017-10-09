# ROBOT Gym
> Training to become a robot master.

Notes and resources from an applied robotics workshop based on ROS

## Table of Content
- [Overview](#overview)
- [Prerequisites](#prerequisites)
- [Development Tools](#tools)
- [Cheat Sheet](#cheat-sheet)
  - [Environment](#get-machines-ip-address)
  - [Terminator](#terminator)
  - [ROS](#ros)
- [Resources](#resources)
- [Contact](#contact)

## Overview
This is an introductory workshop on robotics and working with ROS [Kinetic](http://wiki.ros.org/kinetic/Installation/Ubuntu).
We will cover topics regarding planning, teleoperation, communication, and hardware.
For the most part, the tutorials will be based off the existing ROS Tutorial which can be found [here](http://wiki.ros.org/ROS/Tutorials/). 

## Prerequisites
This workshop assumes the following:
- Ubuntu [16.04.3](https://www.ubuntu.com/download/desktop) LTS has been installed
- Atleast 10GB of disk space is available
- Attendees have some working knowledge of C++, Java or Python 2.7
- Attendees are interested in learning about ROS and robotics

## Tools 
**Terminator**   
Allows users to have multiple terminals in one window.
```
# To install terminator, execute the following command in your terminal
# 
$ sudo apt install terminator
```
### Cheat Sheet
#### Get machine's IP address
```
$ ifconfig

# ...
# wlan0     Link encap:Ethernet  HWaddr 10:02:b5:3f:64:e3  
#           inet addr:10.14.90.5  Bcast:192.168.0.255  Mask:255.255.255.0
#           inet6 addr: fe80::8de2:cbad:43c4:fa14/64 Scope:Link
#           UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
#           RX packets:11239 errors:0 dropped:0 overruns:0 frame:0
#           TX packets:8317 errors:0 dropped:0 overruns:0 carrier:0
#           collisions:0 txqueuelen:1000 
#           RX bytes:13144484 (13.1 MB)  TX bytes:1449665 (1.4 MB)
#
# Your machine's IP address is noted after 'inet addr'
# In this case the machine's IP address is: 10.14.90.5

```

#### Set ROS variables in .bashrc file
```
$ sudo gedit ~/.bashrc
```
```
export ROS_IP=10.14.90.5 # YOUR MACHINE'S IP ADDRESS
export ROS_MASTER_URI=http://10.14.90.5:11311 # ROS MASTER IP ADDRESS, Wait for instructions
```
#### Check variables

```
# Check hostname
$ hostname
```

```
# Check ROS Hostname
$ echo $ROS_HOSTNAME
```

```
# Check ROS IP
$ echo $ROS_IP
```

```
# Check ROS_MASTER_URI
$ echo $ROS_MASTER_URI
```
**NOTE:** Make sure these variables match what is in your ```.bashrc``` file.

#### Terminator
##### Splitting Windows

| Command  | Action |
| ------------- | ------------- |
| Ctrl+Shift+E | vertical split |
| Ctrl+Shift+O | horizontal split |
| Alt+ArrowKeys | Navigate terminals |
| Ctrl+Shift+P | focus be active on the previous view |
| Ctrl+Shift+N | focus be active on the next view |
| Ctrl+Shift+W | close the view where the focus is on |
| Ctrl+Shift+Q | exit terminator |
| Ctrl+Shift+X | focus active window and enlarge it |

##### Groups

| Command  | Action |
| ------------- | ------------- |
| Ctrl+G  | Group All  |
| Ctrl+Shift+G | Ungroup All |
| Ctrl+T | Group Tab | 
| Ctrl+Shift+T | Ungroup Tab | 

##### Launcher parameters

* -m – maximize
* -b – borderless
* -T – set title


#### ROS

```
# roscore
# roscore must be running at all times for ROS node to communicate
# roscore launches the following nodes: master, parameter server, rosout
# 
$ roscore
```

```
# rosrun
# rosrun allows you to run any ROS packages without having to be in the package's working directory
# 
$ rosrun
```

```
# rostopic
# rostopic display debug information about ROS topics from publishers and subscribers
# 
$ rostopic
```
## Resources

- [About ROS](http://www.ros.org/about-ros/)
- [TurtleBot 2](http://www.turtlebot.com/turtlebot2/)
- [Ubuntu install of ROS Kinectic](http://wiki.ros.org/kinetic/Installation/Ubuntu)
- [Irvin's Awesome Developer Resources](https://github.com/kPatch/awesome-developer-resources)
- [Programming Robots with ROS: A Practical Introduction to the Robot Operating System](https://www.amazon.com/Programming-Robots-ROS-Practical-Introduction/dp/1449323898/)
- [ROS Cheat Sheet](https://mirror.umd.edu/roswiki/attachments/de/ROScheatsheet.pdf)
- [Terminator Cheat Sheet](https://github.com/spabinger/terminator-cheat-sheet)

## Contact

**Irvin Steve Cardenas**   
LinkedIn: [/in/irvinscardenas](wwww.irvincardenas.com/in)   
Twitter: [@followIrvin](wwww.twitter.com/followIrvin)   
Email: [irvin@irvincardenas.com](irvin@irvincardenas.com)   
Web: [www.irvincardenas.com](www.irvincardenas.com)   
