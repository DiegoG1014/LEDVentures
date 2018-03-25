import time
import RPi.GPIO as GPIO
import game
import gameutils
from random import *

def printout(whois,msg):
	print("["+whois	+"]","("+str(msg)+")")

printout("Main","Starting LEDVentures")
printout("Main","Loading required libraries and modules")
printout("Main","Loading GPIO library")
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
allChannels = (3,5,7,8,10,11,12,13,15,16,18,19,21,22,23,24,26,29,31,32,33,35,36,37,38,40)
GPIO.setup(allChannels,GPIO.IN)

printout("Main","Defining GPIO channels")
printout("Main","Defining output channels")
game_out = {
	"hp":(
		(7,8,10), #player
		(11,12,13) #enemy
	),
	"inbattle":15,
	"invalidact":16,
	"validact":18,
	"nosuccess":37,
	"success":21,
	"newroom":22,
	"moves":{"bottom":31,"left":32, "right":33, "top":35},
	"alive":36,
	"allpins":(7,8,10,11,12,13,15,16,18,37,21,22,31,32,33,35,36),
	"status":{
		7:True,
		8:True,
		10:True,
		11:True,
		12:True,
		13:True,
		15:True,
		16:True,
		18:True,
		37:True,
		21:True,
		22:True,
		31:True,
		32:True,
		33:True,
		35:True,
		36:True
	}
}
GPIO.setup(game_out["allpins"],GPIO.OUT)
GPIO.output(game_out["allpins"],True)
printout("Main","Succesfully defined output channels")
printout("Main","Defining input channels")
game_in = {
	"act":23,
	"actsetting":(24,26,29),
	"restart":40,
	"allpins":(23,24,26,29,40)
}
GPIO.setup(game_in["allpins"],GPIO.IN)
printout("Main","Succesfully defined output channels")

printout("Main","Loading process complete")

def update(dt):
	gameutils.blink_update(dt)

def run():
	print("----------")
	dt = time.time()/1000
	prevTime = dt
	while 1:
		dt = time.time()/1000 - prevTime
		prevTime = time.time()/1000
		update(dt)

if 1:
	run()
