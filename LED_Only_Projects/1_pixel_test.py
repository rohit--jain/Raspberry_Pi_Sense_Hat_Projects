# Pixels Runner version 1.0
# Author: Rohit Jain 
# Email: rohit.jain.010@gmail.com
# Programmed to run with Raspberry Pi Official Sense Hat

from sense_hat import SenseHat
from time import sleep
import random

mySense = SenseHat()
mySense.low_light = True
maxRange = 7
minRange = 0

p1x = minRange
p1y = minRange

p2x = minRange
p2y = maxRange

p3x = maxRange
p3y = minRange

p4x = maxRange
p4y = maxRange

runway = False

colorSeq = [ "red", "blue", "green", "yellow"]

def redLinner(xr, yr):

	mySense.set_pixel(xr, yr, 255, 0, 0)
	if xr != minRange or yr != maxRange:
		for y in range(minRange + 1, maxRange):
			mySense.set_pixel(xr, y, 255, 0, 0)

def blueLinner(xb, yb):

	mySense.set_pixel(xb, yb, 0, 0, 255)
	if yb!= minRange or yb != maxRange:
		for x in range(minRange + 1, maxRange):
			mySense.set_pixel(x, yb, 0, 0, 255)

def greenLinner(xg, yg):

	mySense.set_pixel(xg, yg, 0, 255, 0)
	if yg!= minRange or yg != maxRange :
		for x in range(minRange + 1, maxRange):
			mySense.set_pixel(x, yg, 0, 255, 0)

def yellowLinner(xy, yy):

	mySense.set_pixel(xy, yy, 255, 255, 0)
	if xy != minRange or xy != maxRange :
		for y in range(minRange + 1, maxRange):
			mySense.set_pixel(xy, y, 255, 255, 0)


def runner():
	global p1x, p1y, p2x, p2y, p3x, p3y, p4x, p4y, maxRange, runway, colorSeq
	loopCount = 0
	try:
		while True:
			
			# Clearing Previous Pixels
			mySense.set_pixel(p1x, p1y, 0, 0, 0)
			mySense.set_pixel(p2x, p2y, 0, 0, 0)
			mySense.set_pixel(p3x, p3y, 0, 0, 0)
			mySense.set_pixel(p4x, p4y, 0, 0, 0)
			
			# Mapping New Pixels
			if runway == False:
				loopCount += 1
				if loopCount > maxRange:
					loopCount = 0
					runway = True
					continue
				p1x += 1
				p2y -= 1
				p3y += 1
				p4x -= 1

			else:
				loopCount += 1
				if loopCount > maxRange:
					loopCount = 0
					runway = False
					continue
				p1x -= 1
				p2y += 1
				p3y -= 1
				p4x += 1
				
			
			# Display New Pixels
			 
#			random.shuffle(colorSeq)
#			for colorItem in colorSeq:
#				if colorItem == "red":
#					redLinner(p1x, p1y)
#				elif colorItem == "green":
#					greenLinner(p2x, p2y)
#				elif colorItem == "yellow":
#					yellowLinner(p3x, p3y)
#				else:
#					blueLinner(p4x, p4y)

			redLinner(p1x, p1y)
			yellowLinner(p3x, p3y)
			greenLinner(p2x, p2y)
			blueLinner(p4x, p4y)
			
			# Debug Info
			pixels = "P1(" + str(p1x) + "," + str(p1y) + ")"
			pixels += " P2(" + str(p2x) + "," + str(p2y) + ")"
			pixels += " P3(" + str(p3x) + "," + str(p3y) + ")"
			pixels += " P4(" + str(p4x) + "," + str(p4y) + ")"
			pixels += "loopCount: " + str(loopCount) + " runway: " + str(runway)
			print(pixels)

			sleep(0.2)

	except KeyboardInterrupt:
		mySense.clear()
		print('Execution Finished!')

def main():
#	mySense.show_message("X")
#	sleep(1)
	runner()

if __name__ == "__main__":main()
	
