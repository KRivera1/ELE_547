from flask import Flask, render_template
from sense_hat import SenseHat


sense = SenseHat()
sense.clear

app = Flask(__name__)


@app.route('/')
def senseData():
	temp = str(sense.get_temperature())
	humidity = str(sense.get_humidity())
	#tempStr = str(temp)
	#humStr = str(humudity)
	Data = {'temp':temp, 'humidity':humidity}
	return render_template('senseData.html',**Data)
	
if __name__ == '__main__':
	app.run(host = '192.168.0.13', debug = True)