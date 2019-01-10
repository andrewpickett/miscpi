import RPi.GPIO as GPIO
import time

MORSE = {
        "A" : [1, 3],
        "B" : [3, 1, 1, 1],
        "C" : [3, 1, 3, 1],
        "D" : [3, 1, 1],
        "E" : [1],
        "F" : [1, 1, 3, 1],
        "G" : [3, 3, 1],
        "H" : [1, 1, 1, 1],
        "I" : [1, 1],
        "J" : [1, 3, 3, 3],
        "K" : [3, 1, 3],
        "L" : [1, 3, 1, 1],
        "M" : [3, 3],
        "N" : [3, 1],
        "O" : [3, 3, 3],
        "P" : [1, 3, 3, 1],
        "Q" : [3, 3, 1, 3],
        "R" : [1, 3, 1],
        "S" : [1, 1, 1],
        "T" : [3],
        "U" : [1, 1, 3],
        "V" : [1, 1, 1, 3],
        "W" : [1, 3, 3],
        "X" : [3, 1, 1, 3],
        "Y" : [3, 1, 3, 3],
        "Z" : [3, 3, 1, 1],
        "1" : [1, 3, 3, 3, 3],
        "2" : [1, 1, 3, 3, 3],
        "3" : [1, 1, 1, 3, 3],
        "4" : [1, 1, 1, 1, 3],
        "5" : [1, 1, 1, 1, 1],
        "6" : [3, 1, 1, 1, 1],
        "7" : [3, 3, 1, 1, 1],
        "8" : [3, 3, 3, 1, 1],
        "9" : [3, 3, 3, 3, 1],
        "0" : [3, 3, 3, 3, 3],
	"." : [1, 3, 1, 3, 1, 3],
	"," : [3, 3, 1, 1, 3, 3],
	"?" : [1, 1, 3, 3, 1, 1],
	"'" : [1, 3, 3, 3, 3, 1],
	"!" : [3, 1, 3, 1, 3, 3],
	"/" : [3, 1, 1, 3, 1],
	"(" : [3, 1, 3, 3, 1],
	")" : [3, 1, 3, 3, 1, 3],
	"&" : [1, 3, 1, 1, 1],
	":" : [3, 3, 3, 1, 1, 1],
	";" : [3, 1, 3, 1, 3, 1],
	"=" : [3, 1, 1, 1, 3],
	"+" : [1, 3, 1, 3, 1],
	"-" : [3, 1, 1, 1, 1, 3],
	"_" : [1, 1, 3, 3, 1, 3],
	"\"" : [1, 3, 1, 1, 3, 1],
	"$" : [1, 1, 1, 3, 1, 1, 3],
	"@" : [1, 3, 3, 1, 3, 1]
}

str = raw_input(">> ")

MORSE_UNIT_TIME = 0.1

def tapLetter(letter, pin, timeout):
        outputVal = ""

        if letter == " ":
                time.sleep(timeout * 7)
                outputVal += "       "
        else:
                m = MORSE[letter.upper()]
                for sig in m:
                        if sig == 1:
                                outputVal += "."
                        elif sig == 3:
                                outputVal += "_"

                        GPIO.output(pin, GPIO.HIGH)
                        time.sleep(timeout * sig)
                        GPIO.output(pin, GPIO.LOW)
                        time.sleep(timeout)
                outputVal += " "
        print outputVal,

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)

for letter in str:
	tapLetter(letter, 11, MORSE_UNIT_TIME)
	time.sleep(MORSE_UNIT_TIME * 3)

GPIO.cleanup()
