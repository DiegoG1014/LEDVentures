controls = {
	"inBattle":{
		(0,0,0):(0,0),#attack high, defend high
		(1,0,0):(1,0),#attack low, defend high
		(0,1,0):(0,1),#attack high, defend low
		(1,1,0):(1,1) #attack low, defend low
	},
	"overworld":{
		(0,0,0):(0,-1),#down
		(1,1,1):(0,1),#up
		(1,0,0):(-1,0),#left
		(0,0,1):(1,0)#right
	}
}

cooldown = 1
def update(dt):
	cooldown = cooldown-dt
	if cooldown <= 0 and GPIO.input(game_in["act"]):
		inputdat = GPIO.input(game_in["actsetting"][0]),GPIO.input(game_in["actsetting"][1]),GPIO.input(game_in["actsetting"][2])
		if game.status["mode"]:
			game.act(controls["inBattle"][inputdat])
		else:
			game.move(controls["overworld"][inputdat])
		cooldown = 1
