#! /bin/sh
#start alarm clock

#must change to AlarmClock directory to get SevenSegment package
#start clock display service
cd /home/pi/AlarmClock/ && python AlarmClock_WeatherButton.py&

#start Alexa
#cd ~/Desktop/alexa-avs-sample-app/samples/companionService && npm start&
#cd ~/Desktop/alexa-avs-sample-app/samples/javaclient && mvn exec:exec&

echo "Alarm Clock Started" > /tmp/AlarmClockStart.txt
