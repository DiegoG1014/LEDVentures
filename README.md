A simple Python game, using the GPIO pins to access LEDs and buttons to serve as the only form of input and output

Mechanics:
	Essentially, the game has two modes: Overworld and in-battle.
	While in battle, the in-battle LED blinks (the faster it blinks, the greater the enemy threat); and a turn-based battle starts
	The player has to choose where to attack and where to defend, by switching inputs on and off (preferably with a single block of three switches)
	
	While in the overworld, the player is inside a randomly generated maze, and has to walk out of it, each step they take (or each room they walk into) they're presented with the threat of confronting an enemy (random chance of a random enemy appearing, kinda like Pokemon)
	If a player is in a new room, the new room LED lights up
	There are four "directional" LEDs that light up individually depending on whether or not the player can walk in that specific direction.
	
Player HP:
	The player has 3 LEDs representing their health (preferably, Red, Green and Blue)
	When their HP drops below a 2 thirds of his health, LED 3 turns off, when it drops below a third, LED 2 turns off, and when it reaches 0, all of the LEDs are off. The closer an LED is to turning off, the faster it blinks
	
Enemy HP:
	Basically the same as Player HP, but with separate LEDs and thus separate pinouts. (Preferably, said LEDs should be Red, Red and Yellow)
	
All of the inputs should low-voltage-drop LEDs that signals whether an input is on or off
These don't necessarily have to be on separate outputs, since they can be powered by the input's power source.