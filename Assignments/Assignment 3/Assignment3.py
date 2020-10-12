# Script: Assignment3.py
# Description: This is a program to practice creating a webserver
#			   using the Raspberry Pi. The webserver contains a table
#			   that displays the temperature and humidity sensor data
#			   being collected from the sensehat. The webserver updates
#			   every 5 seconds to display the latest data.
#			   
# Author: Kevin Rivera
# Version: 1.0
# Date: 10-09-2020
# ELE 547 Assignment 3

#---------------------------------------Libraries------------------------------------------

from flask import Flask, render_template				#Library that provides the webserver framework
from sense_hat import SenseHat							#Library that enables the sense hat functionality.

#---------------------------------------Variables------------------------------------------

sense = SenseHat()										#Object created from the sense hat library.
sense.clear()											#Function call to clear the sense hat matrix LED.
app = Flask(__name__)									#Object created from the flask library.

#---------------------------------------Functions------------------------------------------

@app.route('/')											
def senseData():

	temp = str(round(sense.get_temperature(),2))
	humidity = str(round(sense.get_humidity(),2))
	Data = {'temp':temp, 'humidity':humidity}
	return render_template('senseData.html',**Data)
	
if __name__ == '__main__':
	app.run(host = '192.168.0.13', debug = True)		#Change the host address if necessary. Use ifconfig to 
														#determine the local IP address. This local webserver
														#can be visited by all devices connected to the same network.