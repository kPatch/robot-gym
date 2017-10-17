# Assignment 5

## Table of Contents

- [Overview](#overview)
- [Requirements](#requirements)
- [Grading Criteria](#grading-criteria)
- [Super Star Hall of Fame](#super-star-hall-of-fame)
- [Resources and Examples](#resources-and-examples)

## Overview 
The goal of this assignment is to design and implement the interaction between a simple conversational agent and a hardware-based system implemented using an Arduino microcontroller. The underlying communication should be handled by ROS and you are free to use any available APIs and libraries. See below for suggested resources and examples. 

You must also submit a one paragraph or 5 sentence description of your project and the source code must be made public on GitHub

## Grading Criteria

- **(10 points)** (1) Write a ROS publisher and publish any data (2) Being able to run  '''roscore''' (3) Being able to echo the data through the use of '''rostopic'''. See [day-1]() for ROS command cheatsheet
- **(10 points)** A plain vanilla implementation of an Arduino-based system. You are free to use LEDs, servos, etc
- **(20 points)** An implementation of an Arduino-based system that receives data by subscribing to the ROS publisher you wrote
- **(20 points)** An implementation of an Arduino-based system that publishes data, in addition to subscribing to the ROS publisher you wrote. 
  - The data the Arduino publishes can be as simple as an acknowledgment that it has received a message.
- **(X Points)**  


## Super Star Hall of Fame
- 20 extra credit points
- Recognition in Kent State's HRI Course Hall of Fame
- Appearance and mention in Kent State's Computer Science Department website's homepage
- A written article on Stater magazine

### Overview
Design a human-robot interaction that involves one of our Turtlebots or our SmartDesk. Team may include up to 4 students. Students who wish to pursue this challenge must write a 3 sentence pitch and have it approved by Thursday.

**Additional support will be provided to students who wish to pursue this track**.

### Requirements
- Design the [experience flow]() using a state machine 
- Design the communication flow using a state machine
- Apply at least two of the recommended APIs
- All code must be open sourced on GitHub and named "ksu-hri-<YOUR PROJECT NAME IN LOWER CASE>

## Resources and Examples

### PocketSphinx

### Google's Voice Recognition API

### Google's Text-to-Speech API

### DialogFlow (Formerly API.AI)

### Amazon Alexa 

### rosserial 




