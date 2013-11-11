from tts import say
from stt import listen
#from liarsdice import *

	
def main():
	print "Welcome!"
	say("Hola Putas");
	say("Cuantas personas van a jugar?");
	sound = listen()
	x = None
	while(x == None):
		print sound
		try:
			x = int(sound)
		except:
			say("Cuantas personas?");
			sound = listen()
	say("Cuuuuuuul. Yo empiezo...");
	say("Seis foking quinas");
#	g = Game(5*x, x, (1, 3))
	

main()
