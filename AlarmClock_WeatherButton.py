import datetime
import time
from urllib2 import Request, urlopen, URLError
import json
from Adafruit_LED_Backpack import SevenSegment
import RPi.GPIO as GPIO
weatherButton = 11
GPIO.setmode(GPIO.BOARD)
GPIO.setup(weatherButton, GPIO.IN, pull_up_down=GPIO.PUD_UP)

DIGIT_VALUES = {
    ' ': 0x00,
    '-': 0x40,
    '0': 0x3F,
    '1': 0x06,
    '2': 0x5B,
    '3': 0x4F,
    '4': 0x66,
    '5': 0x6D,
    '6': 0x7D,
    '7': 0x07,
    '8': 0x7F,
    '9': 0x6F,
    'A': 0x77,
    'B': 0x7C,
    'C': 0x39,
    'D': 0x5E,
    'E': 0x79,
    'F': 0x71
}

# Create display instance on default I2C address (0x70) and bus number.
display = SevenSegment.SevenSegment()

print('Press Ctrl-Z to quit.')

def clock():
	#display.set_brightness(10);
	colon = True
	display.clear()
	
	#for x in range(0,30):
	try:
		display.set_colon(colon)
		dt = datetime.datetime.now()
		t = time.strftime("%H%M")
		
		#put the time on the display
		display.print_number_str(t)
		display.write_display();
		#print(t);
	except:
		print("Time error")
	
	#colon = not colon
	
def weather():
	try:
		#Open Weather Map API
		#request = "http://api.openweathermap.org/data/2.5/forecast?id=524901&APPID=1a066b3ed754c3b505b8dfdf8d743bec&units=imperial"
		
		#Weather Underground API
		request = "http://api.wunderground.com/api/82e819ad30f651bd/geolookup/conditions/q/OH/Hamilton.json"
			
		response = urlopen(request)
		json_string = response.read()
		parsed_json = json.loads(json_string)
		temp_f = str(round(parsed_json['current_observation']['temp_f']))
		print(temp_f)
		display.clear()
		
		#display.set_digit_raw(0, DIGIT_VALUES.get(str(temp_f[0].upper()), 0x00))
		#display.set_digit_raw(1, DIGIT_VALUES.get(str(temp_f[1].upper()), 0x00))
		#display.set_digit_raw(2, DIGIT_VALUES.get(str(temp_f[3].upper()), 0x00))
		
		#handle negative temperatures
		if(temp_f[0]=='-'):
			#negative sign
			display.set_digit(0, str(temp_f[0].upper()))
			#first 2 digits
			display.set_digit(1, str(temp_f[1].upper()))
			display.set_digit(2, str(temp_f[2].upper()))
		else:			
			#first 2 digits of temp
			display.set_digit(0, str(temp_f[0].upper()))
			display.set_digit(1, str(temp_f[1].upper()))
			#blank
			display.set_digit(2, ' ')
		#turn on degree sign
		display.set_fixed_decimal(True)
		#F for Fahrenheit
		display.set_digit(3, "F")
		display.write_display()	


	except:
		print("URL Error")
		pass
	
	#time.sleep(10)
		
	

# Initialize the display. Must be called once before using the display.
display.begin()

while True:
	#if weatherButton is pressed, show weather
	if(GPIO.input(weatherButton) == 0):
		weather()
		time.sleep(1)
		#wait for weatherButton to be unpressed
		while(GPIO.input(weatherButton) == 0):
			#nothing
			pass
	clock()

	
	
