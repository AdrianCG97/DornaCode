from dorna import Dorna
import json
import time
import sys

# creat Dorna object and connect to the robot
robot = Dorna("config_1.yaml")
robot.connect()

#check if robot is homed
h = json.loads(robot.homed())

if(h['j0'] == 0 or  h['j1'] == 0 or h['j2'] == 0 or h['j3'] == 0 or h['j4'] == 0):
	print("Robot not homed\n")
	print("Starting homing process\n")
	robot.home(["j0", "j1", "j2", "j3"])
	print("Robot is now homed\n")
else:
	print("Robot is homed\n")
rest = {"command": "move", "prm":{"path": "joint", "movement":0, "speed":1000, "joint":[0, 160, -130, 0, 0]}}


extend1 = {"command": "move", "prm":{"path": "joint", "movement":0, "speed":2500, "joint":[0, 0, 0, 0, 0]}}
down1 = {"command": "move", "prm":{"path": "joint", "movement":0, "speed":2500, "joint":[0, 30, -70, 40, 0]}}
back1 = {"command": "move", "prm":{"path": "joint", "movement":0, "speed":2500, "joint":[0, 110, -110, 0, 0]}}

extend2 = {"command": "move", "prm":{"path": "joint", "movement":0, "speed":2500, "joint":[-90, 0, 0, 0, 0]}}
down2 = {"command": "move", "prm":{"path": "joint", "movement":0, "speed":2500, "joint":[-90, 30, -70, 40, 0]}}
back2 = {"command": "move", "prm":{"path": "joint", "movement":0, "speed":2500, "joint":[-90, 110, -110, 0, 0]}}


grab1 = {"command": "move", "prm":{"path": "joint", "movement":0, "speed":2500, "joint":[0, 0, -90, 90, 0]}}
grab2 = {"command": "move", "prm":{"path": "line", "movement":1, "speed":2500, "x": 2}}



# home all the joints
#robot.home(["j0", "j1", "j2", "j3"])

"""
move to j0 = 0, ..., j4 = 0
wait for the motion to be done, timeout = 1000 seconds
"""
#result = robot.play({"command": "move", "prm":{"path": "joint", "movement":0, "joint":[0, 0, 0, 0, 0]}})
#result = json.loads(result)		 # translate the json file into a python dictionary
#print(result)

#wait = robot._wait_for_command(result, time.time()+1000)


# move in cartesian space, -10 inches toward X direction
#robot.play({"command": "move", "prm":{"path": "line", "movement":1, "x":-10}})
#robot.play({"command": "move", "prm":{"path": "joint", "movement":0, "joint":[90, 90, 0, 0, 0]}})

robot.play(rest)
robot.play(back1)
robot.play(down1)
robot.play(extend1)
robot.play(down1)
robot.play(back1)

robot.play(back2)
robot.play(down2)
robot.play(extend2)
robot.play(down2)
robot.play(back2)

robot.play(back1)
robot.play(rest)

robot.terminate()
