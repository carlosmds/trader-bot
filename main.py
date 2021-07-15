# main file for the robot
from dotenv import dotenv_values
import logging
import sys

sys.path.append('./app')

# logging.disable(level=(logging.DEBUG))

from robot import Robot

config = dotenv_values(".env")

userInfo = {
    'username': config["USERNAME"],
    'password': config["PASSWORD"]
}

robot = Robot(userInfo, mode = "PRACTICE")

robot.work()