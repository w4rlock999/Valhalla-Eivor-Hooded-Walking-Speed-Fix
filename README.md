# Valhalla Eivor Hooded Walking Speed Fix

If you play Assassin's Creed Valhalla in PC with mouse and keyboard you must already know that Eivor walking speed when hooded is annoyingly slow.


This project allows you to control a virtual joystick using mouse scroll events and button clicks. The virtual joystick's speed can be adjusted by scrolling up and down, and you can toggle between a specific speed value and a stop value using the 5th mouse button.

## Prerequisites

Before running the script, make sure you have the following software installed on your Windows system:

1. **Python**: Python is the programming language used to run the script. If you don't have Python installed, follow these steps:

   - Download the latest Python installer from the official website: https://www.python.org/downloads/windows/
   - Run the installer and select the option to add Python to your system's PATH during installation.
   - Restart your computer after installing Python.

2. **pynput**: The `pynput` library is required to capture mouse events. To install it, open your command prompt (CMD) and enter the following command:

    `pip install pynput`

3. **vgamepad**: The `vgamepad` library is necessary to control the virtual joystick. To install it, open your command prompt (CMD) and enter the following command:

    `pip install vgamepad`


## Usage

1. Clone or download this repository to your local machine.

2. Open a command prompt (CMD) or terminal and navigate to the folder where you cloned or downloaded the project.

3. Run the script using the following command:
   
    `python mouseCtrlEmu.py`

5. The script will start running and will display the following message:

6. Now you can interact with the virtual joystick using your mouse:

- Scroll up: The virtual joystick's speed will increase between 0.7 and 1.0.
- Scroll down: The virtual joystick's speed will decrease between 0.7 and 1.0.
- Mouse Button 5 (X2): Clicking this button will toggle between the current speed and the stop value.

6. To stop the script, press `Ctrl+C` in the command prompt.
