from dorna import Dorna
import json
import time


class Station:
	def __init__(self, pos):
		self.positions = pos 		#Array with positions in order

	def doStation(self,robot):
		print("0  ")
		for pos in self.positions:
			robot.play({"command": "move", "prm":{"path": "joint", "movement":0, "speed":pos.speed, "joint":[pos.j0, pos.j1, pos.j2, pos.j3, pos.j4]}})
			posIsDone(robot)
			print("1  ")
			time.sleep(pos.waitEnd)

class Position:
	def __init__(self,joints, w, s):
		self.j0 = joints[0]
		self.j1 = joints[1]
		self.j2 = joints[2]
		self.j3 = joints[3]
		self.j4 = joints[4]
		self.waitEnd = w     #Integer that indicates how long system should wait after position is achieved
		self.speed = s




#def doStation(stat):
#	for pos in stat.positions:
#		robot.play({"command": "move", "prm":{"path": "joint", "movement":0, "speed":pos.speed, "joint":[pos.j0, pos.j1, pos.j2, pos.j3, pos.j4]}})
#		time.sleep(pos.waitEnd)


def posIsDone(robot):
	dic = json.loads(robot.device())
	while (dic['state'] !=0):
		dic = json.loads(robot.device())