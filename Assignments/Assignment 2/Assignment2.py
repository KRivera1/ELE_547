from random import randint
from sense_hat import SenseHat
import time
  
sense = SenseHat() 
sense.clear()
a = 1
counter = 0
#sense.set_pixel(0, 0, 255, 0, 0) 
#sense.set_pixel(0, 7, 0, 255, 0) 
#sense.set_pixel(7, 0, 0, 0, 255)
#sense.set_pixel(7, 7, 255, 0, 255)
#time.sleep(2)
#sense.clear()
while a:
	#print("Hello")
	#time.sleep(1)
	x = randint(0, 7)
	y = randint(0, 7)
	r = randint(0, 100)
	g = randint(0, 100)
	b = randint(0, 100)
	sense.set_pixel(x, y, r, g, b)
	counter = counter + 1
	if counter == 15:
		a = 0
	time.sleep(1)

sense.clear()
