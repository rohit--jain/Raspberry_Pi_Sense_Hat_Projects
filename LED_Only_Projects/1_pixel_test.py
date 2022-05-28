from  sense_hat import SenseHat

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
				if loopCount > maxRange:
					loopCount = 0
					runway = True
				p1x += 1
				p2y -= 1
				p3y += 1
				p4x -= 1

				loopCount += 1
			else:
				if loopCount > maxRange:
					loopCount = 0
					runway = False
				p1x -= 1
				p2y += 1
				p3y -= 1
				p4x += 1
				
			
			# Display New Pixels
			mySense.set_pixel(p1x, p1y, 255, 0, 0)
			mySense.set_pixel(p2x, p2y, 0, 255, 0)
			mySense.set_pixel(p3x, p3y, 0, 0, 255)
			mySense.set_pixel(p4x, p4y, 255, 0, 255)

	except KeyboardInterrupt:
		mySense.clear()
    	print('Execution Finished!')


def main():
	mySense.show_message("X")
if __name__ == "__main__":main()
	
