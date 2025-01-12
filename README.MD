# “blackpearl” Robot
## Overview
The “blackpearl” robot is an exploration robot created using a Raspberry Pi microcontroller, with the ability to perform simple movements, detect objects, and stream live footage from a camera. This robot is designed to be controlled remotely via a web interface, and can be accessed from both computers and smartphones using a Wi-Fi connection.

## Purpose
The goal of this project is to build a small robot that can:
*	Perform simple movements.
*	Detect objects using sensors.
*	Stream live video from a camera.

## Hardware Components
*	Raspberry Pi: The main controller for the robot, handling all hardware connections and interactions.
*	Lego Mindstorm NXT: Used as the robotic base kit, providing motors and sensors for movement and detection.
*	BrickPi: A Raspberry Pi add-on that allows control over Lego Mindstorm motors and sensors.
*	Arduino Uno 3: Used as an additional microcontroller to control the servo and ultrasonic sensors for better accuracy.
*	Camera: Used for streaming live video.
*	Power Bank: Powers the Raspberry Pi and connected components.

## Software Stack
*	Python: The main programming language used for controlling the Raspberry Pi.
*	Flask: A Python framework used to create the web interface to control the robot.
*	Ajax: Used to send requests to the server, enabling smooth communication between the web interface and the Raspberry Pi.

## Features
*	Web Interface: The robot can be controlled from a web interface, accessible via Wi-Fi on both computers and smartphones.
*	Simple Movement: The robot can move based on input from the controller.
*	Object Detection: Using sensors, the robot can detect obstacles in its path.
*	Camera Streaming: The robot streams live video from its camera for real-time observation.

## Getting Started
To set up and start using the robot, follow these instructions:

### Prerequisites
*	Raspberry Pi with Raspbian installed.
*	Lego Mindstorm NXT Kit.
*	BrickPi add-on for Raspberry Pi.
*	Arduino Uno 3 microcontroller.
*	Python installed on Raspberry Pi.
*	Flask and Ajax for web-based control.

### Setting Up the Hardware
1.	Connect the Raspberry Pi to the Lego Mindstorm NXT using the BrickPi add-on.
2.	Set up the Arduino Uno 3 to control the servo and ultrasonic sensor.
3.	Connect the camera to the Raspberry Pi for streaming.

### Setting Up the Software
1.	Install Python on the Raspberry Pi.

2.	Install the Flask framework: 

    ```pip install flask```

3.	Clone this repository to your Raspberry Pi:

    ```git clone https://github.com/tantr-us/blackpearl-final.git```

    ```cd blackpearl-final/source-code/blackpearl```

4.	Start the Flask server:

    ```python blackpearl.py```

5.	Open a web browser and navigate to ```http://<raspberry-pi-ip>:5000``` to control the robot.

## Usage
*	Control the Robot: Use the web interface to control the robot’s movement, object detection, and camera streaming.
*	Web Access: The web interface can be accessed on any device connected to the same Wi-Fi network, including both computers and smartphones.

## Conclusion
The “blackpearl” robot serves as an exploration robot controlled over Wi-Fi, with the flexibility of using both computer and smartphone for control. It combines multiple hardware components and programming techniques to create a functional and interactive robot for learning and experimentation.

## Images
<img src="/images/IMG_1047.JPG" width="650" height="490" />
<img src="/images/IMG_1048.JPG" width="650" height="490" />
<img src="/images/IMG_1064.JPG" width="650" height="490" />
<img src="/images/IMG_1065.JPG" width="650" height="490" />
<img src="/images/IMG_1067.JPG" width="650" height="490" />
<img src="/images/IMG_1072.JPG" width="650" height="490" />
<img src="/images/IMG_5969.JPG" width="650" height="490" />
