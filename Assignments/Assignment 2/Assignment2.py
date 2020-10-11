# Script: Assignment2.py
# Description: This is a modification of the sparkling LED program
#		  	   found on the Raspberry Pi Foundation website. The 
#			   accelerometer and gyroscope are used to control the
#			   LED matrix array. 30 LEDs are turned on sequentially
#			   and the frequency at which LEDs are enabled is controlled
#			   by the gyroscope pitch value. The accelerometer Y and
#			   Z values control the color of the LEDs. When the
#			   acceleration in the Z direction is maximized and the
#			   value of y is minized the LEDs become blue. In the opposite
#			   case, the LEDs become red and in between the two extremes
#			   the LEDs will be some color between red and blue.
#
# Author: Kevin Rivera
# Version: 1.0
# Date: 10-04-2020
# ELE 547 Assignment 2

#---------------------------------------Libraries------------------------------------------

from random import randint		#Library that enables the ability to generate random numbers.
from sense_hat import SenseHat		#Library that enables the sense hat functionality.
import time				#Library that enable the ability to use time tools.

#---------------------------------------Variables------------------------------------------

sense = SenseHat()			#Object created from the sense hat library.
sense.clear()				#Function call to clear the sense hat matrix LED.
counter = 0				#Variable that will keep track of the number of loop cycles.

#---------------------------------------Loop-----------------------------------------------

while 1:
	
	orient = sense.get_orientation()	#Dictionary that contains the mems gyroscope data.
	accel = sense.get_accelerometer_raw()	#Dictionary that contains the mems accelerometer data.
	pitch = orient["pitch"]			#Assigning the pitch data to a variable.
	yaccel = abs(accel['y'])		#Assigning the absolute value Y acceleration data to a variable.
	zaccel = abs(accel['z'])		#Assigning the absolute value Z acceleration data to a variable.
	
	#If statement checks to make sure that reassigns accelerator values if they are greater than 1.
	if yaccel > 1:
		yaccel = 1
		
	if zaccel > 1:
		zaccel = 1
	
	
	xcoord = randint(0, 7)			#Random value between 0-7 assigned to the xcoord value.
	ycoord = randint(0, 7)			#Random value between 0-7 assigned to the ycoord value.
	r = int(255*yaccel)			#'Red' part of LED calculated. Value between 0-255.
	b = int(255*zaccel)			#'Blue' part of LED calculated. Value between 0-255.
	sense.set_pixel(xcoord, ycoord, r, 0, b)#The next LED pixel is enabled and given an xy coordinate and color between blue and red.
	counter = counter + 1			#The counter is incremented by one.
	
	#If statement that checks the value of the counter variable. If the counter value is 30 then the
	#LED matrix is cleared to prevent cluttering. The counter variable is reset as well.
	if counter == 30:
		sense.clear()			#Function call to clear the sense hat matrix LED.
		counter = 0
		
		
	time.sleep(pitch/1000)			#The raspberry pi is paused for a fraction of a second before lighting another LED.
