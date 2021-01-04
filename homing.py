from dorna import Dorna
import json
import time
import sys

# creat Dorna object and connect to the robot
robot = Dorna("config_1.yaml")
robot.connect()

# home all the joints
robot.home(["j0", "j1", "j2", "j3"])

"""
move to j0 = 0, ..., j4 = 0
wait for the motion to be done, timeout = 1000 seconds
"""
robot.play({"command": "move", "prm":{"path": "joint", "movement":0, "joint":[0, 0, 0, 0, 0]}})
dic = json.loads(robot.device())
while (dic['state'] !=0):
	dic = json.loads(robot.device())
print("Done\n")
time.sleep(5)

# move to rest position
rest = {"command": "move", "prm":{"path": "joint", "movement":0, "speed":1000, "joint":[0, 160, -130, 0, 0]}}
robot.play(rest)

dic = json.loads(robot.device())
while (dic['state'] !=0):
	dic = json.loads(robot.device())
print("Done\n")
time.sleep(5)

sys.exit()
