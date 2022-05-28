from sense_hat import SenseHat

mySense = SenseHat()
mySense.low_light = True
mySense.set_pixel(0, 0, 255, 0, 0)
mySense.set_pixel(0, 7, 0, 255, 0)
mySense.set_pixel(7, 0, 0, 0, 255)
mySense.set_pixel(7, 7, 255, 0, 255)
