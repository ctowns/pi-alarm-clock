# pi-alarm-clock
Raspberry Pi-powered Alarm Clock with Alexa Integration

# **Materials:**

1 - Raspberry Pi 3 Model B

1 - Adafruit 0.56" 4-Digit 7-Segment Display w/I2C Backpack (any color)

1 - USB Microphone (very small so it can fit within alarm clock box):
  https://www.amazon.com/gp/product/B00IR8R7WQ/ref=oh_aui_search_detailpage?ie=UTF8&psc=1
  
1 - Speaker so Alexa can talk back to you! Any speaker with a 3.5mm audio jack output will do, I use this:
  808 CANZ Bluetooth Wireless Speaker - Silver 
  (https://www.amazon.com/808-CANZ-Bluetooth-Wireless-Speaker/dp/B00EFS120A)
  
2 - Push buttons, 1 for displaying temperature on 7-segment display, 1 for activating Alexa. I used these:
  https://www.amazon.com/gp/product/B0094GP7SQ/ref=oh_aui_search_detailpage?ie=UTF8&psc=1
  
Also, a soldering iron, some solder, and some wires will be needed for setting up the 7-segment display and soldering the buttons.
If a soldering iron is unavailable, my mixtape is a viable alternative for producing the high tempertures needed to solder.

--------------------------------------------------------------------------------------------------------------------------------------

I use VNC Viewer and Server to connect to and work on my Raspberry Pi (so I don't need a mouse, keyboard, or monitor to get work done!)
VNC Connect (Viewer and Server) come pre-installed on the Raspbian OS, so you only need to download VNC Connect/Viewer for your computer if you want to control your Pi this way! Download available here: 
https://www.realvnc.com/en/raspberrypi/ 


The Alexa client can be downloaded and installed by following the steps here:
https://github.com/alexa/alexa-avs-sample-app 
I have it running on a Raspberry Pi 3 Model B with the wake word engine off. 
You will need to create an Amazon Developer account to get authorization to use Amazon Voice Services for Alexa.


# **To get 7-Segment Display to work:**

The python library for controlling the 7-segment display can be found here:
https://github.com/adafruit/Adafruit_Python_LED_Backpack
This library must be in the same folder as the script that runs the 7-Segment Display in order for it to work.


The 7-segment display used is a Adafruit 0.56" 4-Digit 7-Segment Display w/I2C Backpack - Yellow (any color will work obviously)
This can be found here (or from nearly any electronics dealer): 
https://www.adafruit.com/product/879


# **To run at startup:**

/etc/rc.local has command to run AlarmClockStartup.sh which starts the clock display (and eventually Alexa also, but this is currently not working...if only someone with a bunch of Linux experience could help me...*cough cough* Andy...)


Inspiration and a lot of helpful information for this project came from  Nick Triantafillou's guide to building an Alexa powered alarm clock, which can be found here: 
https://www.hackster.io/xelfer/time-machine-a079fa?ref=user&ref_id=42755&offset=0

More files and info to come...
