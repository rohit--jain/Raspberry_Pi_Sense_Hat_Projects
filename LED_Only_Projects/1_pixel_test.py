# Pixels Runner version 1.0
# Author: Rohit Jain 
# Email: rohit.jain.010@gmail.com
# Programmed to run with Raspberry Pi Official Sense Hat

from  sense_hat import SenseHat
from time import sleep

mySense = SenseHat()
mySense.low_light = True
maxRange = 7

p1x = 0
p1y = 0

p2x = 0
p2y = maxRange

p3x = maxRange
p3y = 0

p4x = maxRange
p4y = maxRange

runway = False

def runner():
	global p1x, p1y, p2x, p2y, p3x, p3y, p4x, p4y, maxRange, runway
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
			mySense.set_pixel(p1x, p1y, 255, 0, 0)   
			mySense.set_pixel(p2x, p2y, 0, 255, 0)
			mySense.set_pixel(p3x, p3y, 0, 0, 255)
			mySense.set_pixel(p4x, p4y, 255, 0, 255)

			# Debug Info
			pixels = "P1(" + str(p1x) + "," + str(p1y) + ")"
			pixels += " P2(" + str(p2x) + "," + str(p2y) + ")"
			pixels += " P3(" + str(p3x) + "," + str(p3y) + ")"
			pixels += " P4(" + str(p4x) + "," + str(p4y) + ")"
			pixels += "loopCount: " + str(loopCount) + " runway: " + str(runway)
			print(pixels)

			sleep(1)

	except KeyboardInterrupt:
		mySense.clear()
		print('Execution Finished!')

def main():
	mySense.show_message("X")
	sleep(1)
	runner()

if __name__ == "__main__":main()
	
