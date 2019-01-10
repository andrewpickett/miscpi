import RPi.GPIO as GPIO
from time import sleep 

# Set GPIO to Broadcom system and set RGB Pin numbers
RUNNING = True
GPIO.setmode(GPIO.BCM)
red = 13
green = 19
blue = 26
 
# Set pins to output mode
GPIO.setup(red, GPIO.OUT)
GPIO.setup(green, GPIO.OUT)
GPIO.setup(blue, GPIO.OUT)
 
Freq = 100 #Hz
 
# Setup all the LED colors with an initial
# duty cycle of 0 which is off
RED = GPIO.PWM(red, Freq)
RED.start(0)
GREEN = GPIO.PWM(green, Freq)
GREEN.start(0)
BLUE = GPIO.PWM(blue, Freq)
BLUE.start(0)
 
# Define a simple function to turn on the LED colors
def color(R, G, B, on_time):
    # Color brightness range is 0-100%
    RED.ChangeDutyCycle(R)
    GREEN.ChangeDutyCycle(G/2.0)
    BLUE.ChangeDutyCycle(B/2.0)
    sleep(on_time)
 
    # Turn all LEDs off after on_time seconds
    RED.ChangeDutyCycle(0)
    GREEN.ChangeDutyCycle(0)
    BLUE.ChangeDutyCycle(0)
 
print("Light It Up!")
print("Press CTRL + C to quit.\n")
print(" R  G  B\n---------")

color(40, 100, 40, 5)

# Main loop
try:
    while RUNNING:
        for x in range(0,2):
            for y in range(0,2):
                for z in range(0,2):
                    print (x,y,z)
                    # Slowly ramp up power percentage of each active color
                    for i in range(0,101):
                        color((x*i),(y*i),(z*i), .02)
 
# If CTRL+C is pressed the main loop is broken
except KeyboardInterrupt:
    RUNNING = False
    print "\Quitting"
 
# Actions under 'finally' will always be called
# regardless of what stopped the program
finally:
    # Stop and cleanup so the pins
    # are available to be used again
    GPIO.cleanup()
##################################################################################

#PIN_RED = 13
#PIN_GREEN = 19
#PIN_BLUE = 26
#
#print 'Starting'
#GPIO.setmode(GPIO.BCM)
#GPIO.setup(PIN_RED, GPIO.OUT)
#GPIO.setup(PIN_GREEN, GPIO.OUT)
#GPIO.setup(PIN_BLUE, GPIO.OUT)
#
#str = raw_input("RGB >>> ");
#
#while (str != "000"):
#	GPIO.output(PIN_RED, int(str[0]))
#	GPIO.output(PIN_GREEN, int(str[1]))
#	GPIO.output(PIN_BLUE, int(str[2]))
#	str = raw_input("RGB >>> ")
#
#GPIO.cleanup()
#print 'Ending'
