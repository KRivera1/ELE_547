from flask import Flask, render_template
from sense_hat import SenseHat


sense = SenseHat()
sense.clear

app = Flask(__name__)


@app.route('/')
def senseData():
	temp = sense.get_temperature()
	humidity = sense.get_humidity()
	tempStr = str(temp)
	humStr = str(humudity)
	return tempStr
	
if __name__ == '__main__':
	app.run(host = '192.168.0.13', debug = True)