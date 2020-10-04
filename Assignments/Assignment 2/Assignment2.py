from random import randint
from sense_hat import SenseHat
import time
  
sense = SenseHat() 
sense.clear()
a = 1
counter = 0

while a:
	
	orient = sense.get_orientation()
	accel = sense.get_accelerometer_raw()
	pitch = orient["pitch"]
	roll = orient["roll"]
	yaw = orient["yaw"]
	xaccel = accel['x']
	yaccel = abs(accel['y'])
	zaccel = abs(accel['z'])
	if yaccel > 1:
		yaccel = 1
	if zaccel > 1:
		zaccel = 1
	xcoord = randint(0, 7)
	ycoord = randint(0, 7)
	#r = randint(0, 100)
	#g = randint(0, 100)
	#b = randint(0, 100)
	r = int(255*yaccel)
	b = int(255*zaccel)
	#sense.set_pixel(xcoord, ycoord, r, g, b)
	sense.set_pixel(xcoord, ycoord, r, 0, b)
	counter = counter + 1
	if counter == 30:
		#a = 0
		sense.clear()
		counter = 0
	time.sleep(pitch/1000)
	print(pitch)

sense.clear()
