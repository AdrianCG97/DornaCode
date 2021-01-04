from dorna import Dorna
import json
import time
import Move
from Move import Station
from Move import Position
import sys

# creat Dorna object and connect to the robot
robot = Dorna("config_1.yaml")
robot.connect()

"""
WHAT CODE WILL DO:
	1) Start with arm in resting position
	2) Extend to get cup from dispenser
	3) Go to next station to fill cup with tea
	4) Go to final station and place cup 
	5) Return to rest position
"""

start = Station([Position([0, 110, -110, 0, 0],1,1000)])

cupDispenser = Station([Position([ 0, 110, -110, 0, 0],5,1000),Position([ 0, 30, -70, 40, 0],0,1000),Position([ 0, 0, 0, 0, 0],1,1000),Position([ 0, 30, -70, 40, 0],0,1000),Position([ 0, 110, -110, 0, 0],0,1000)])

iceDispenser = Station([Position([90, 110, -110, 0, 0],0,1000),Position([90, 30, -70, 40, 0],0,1000),Position([90, 0, 0, 0, 0],1,1000),Position([90, 30, -70, 40, 0],0,1000),Position([90, 110, -110, 0, 0],0,1000)])

teaDispenser = Station([Position([180, 110, -110, 0, 0],0,1000),Position([180, 30, -70, 40, 0],0,1000),Position([180, 0, 0, 0, 0],1,1000)]) 

#Lower cup to ground and move arm back

#waitForTea  = Station([Position([180, 110, -110, 0, 0],0,10000)])

#Lower to grab cup with tea # grabTea     = Station([Position([180, 30, -70, 40, 0],0,1000), *******,[Position([180, 30, -70, 40, 0],0,1000),[Position([180, 110, -110, 0, 0],0,1000)])

#deliverCup  = Station([Position([270, 110, -110, 0, 0],0,1000),Position([270, 30, -70, 40, 0],0,1000),Position([270, 0, 0, 0, 0],1,1000),Position([270, 30, -70, 40, 0],0,1000),Position([270, 110, -110, 0, 0],0,1000)])

end = Station([Position([0, 160, -130, 0, 0],1,1000)])

####### START MAIN #######

###check if robot is homed
homed = robot.homed()
if(homed != "{\"j0\": 1, \"j1\": 1, \"j2\": 1, \"j3\": 1, \"j4\": 1}"):
	print("Robot not homed\n")
	print("Starting homing process\n")
	robot.home(["j0", "j1", "j2", "j3"])
	print("Robot is now homed\n")
else:
	print("Robot is homed\n")

##Erase later

rest = {"command": "move", "prm":{"path": "joint", "movement":0, "speed":1000, "joint":[0, 160, -130, 0, 0]}}
robot.play(rest)

dic = json.loads(robot.device())
while (dic['state'] !=0):
	dic = json.loads(robot.device())
print("Done reseting\n")


### Start executing commands
start.doStation(robot)
print("Start done\n")

#cupDispenser.doStation(robot)
print("Cup dispenser done\n")

#iceDispenser.doStation(robot)
print("Ice dispenser done\n")

#teaDispenser.doStation(robot)
print("Tea dispenser done\n")

end.doStation(robot)
print("End done\n")


robot.terminate()
