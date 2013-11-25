from liarsdice import *

SAY_AGAIN_PROMPTS = ["que?", "como?", "no entiendo", "que dijistes?", "como es?", "no escuche, que dijistes?"]
DICE_PER_PLAYER = 5


def main():
	print "Welcome!"
	say("Hola Putas");
#	num_players = ask("Cuantas personas van a jugar?", int);
	num_players = 6
	say("Cuuuuuuul. Yo empiezo...")
#	perudo = Player(DICE_PER_PLAYER*num_players, DICE_PER_PLAYER)
	g = Game(DICE_PER_PLAYER*num_players, num_players)
	g.play()

	
# === CALL MAIN	
main()
# === END PROGRAM


