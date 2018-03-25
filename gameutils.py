def showHP(hp,maxhp,ent): #perhp is a bad variable name that stands for percent of hp; and yes, I admit I used it in a dirty way
	perhp = (hp*100)/maxhp
	if perhp >= 67:
		blinkStart(game_out["hp"][ent][2],41-(40*(perhp/100)))
		blinkStop(game_out["hp"][ent][1])
		blinkStop(game_out["hp"][ent][0])
		LEDon(game_out["hp"][ent][1])
		LEDon(game_out["hp"][ent][0])
	
	elif perhp >=34:
		perhp = perhp+34
		blinkStart(game_out["hp"][ent][1],41-(40*(perhp/100)))
		blinkStop(game_out["hp"][ent][2])
		blinkStop(game_out["hp"][ent][0])
		LEDoff(game_out["hp"][ent][2])
		LEDon(game_out["hp"][ent][0])
	
	else:
		perhp = perhp+67
		blinkStart(game_out["hp"][ent][0],41-(40*(perhp/100)))
		blinkStop(game_out["hp"][ent][2])
		blinkStop(game_out["hp"][ent][1])
		LEDoff(game_out["hp"][ent][1])
		LEDoff(game_out["hp"][ent][2])

blinklist = []
blinkReg = []
def blinkStart(pin,freq): #frequency in hertz, time in seconds
	if not blinkReg[pin]:
		blinklist.append([pin,freq,0])
		blinkReg[pin] = len(blinklist)-1
	else:
		blinklist[blinkReg[pin]] = [pin,freq,0]

def blinkStop(pin):
	blinklist.remove(blinkReg[pin])
	blinkReg[pin] = None

def blink_update(dt):
	for led in blinklist:
		led[2] = led[2] + dt
		if 1/freq >= led[2]:
			led[2] = 0
			LEDtoggle(led[0])

def LEDtoggle(pin):
	if game_out.status[pin]:
		GPIO.output(pin,False)
		game_out.status[pin] = False
	else:
		GPIO.output(pin,True)
		game_out.status[pin] = True

def LEDon(pin):
	GPIO.output(pin,True)
	game_out.status[pin] = True

def LEDoff(pin):
	GPIO.output(pin,False)
	game_out.status[pin] = False
