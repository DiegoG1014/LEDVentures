import mapgen
import controls

status = {
	"mode":0, #0 overworld, 1 in battle
	"enemyrand":[1.0,True], #from 1.2 to 0.8, if True it goes up
	"map":mapgen.gen() #0 = newroom, 1 = oldroom, 2 = wall
}

player = [300,9,[0,0]]#hp,atk,[pos]

enemies = {
	#chance,hp,atk,danger
	#chance is represented in a base of a hundred (x in 100 chance of y)
	#danger directly represents the frequency (in hz) at what the in-battle LED will blink
	"rat":(65,10,3,3),
	"goblin":(45,20,7,6),
	"giantworm":(40,13,5,5),
	"skeleton":(30,20,9,10),
	"thief":(5,5,40,15),
	"souleater":(10,25,20,20),
	"destroyer":(7,30,30,35)
}

def update(dt):
	if status["mode"]:
		arena(dt)
	else:
		overworld(dt)
	gameutils.LEDtoggle(game_out["alive"])

def move(direction):
	playerpos = player[2][0],player[2][1]
	if not status.map[playerpos] == 2:
		player[2] + direction
	if status.map[playerpos] == 0:
		gameutils.LEDon(game_out["newroom"])
		status.map[playerpos] = 1
	else:
		gameutils.LEDoff(game_out["newroom"])
		for i,v in enemies:
			if randint(1,100) < v[0]:
				startbattle(i)
