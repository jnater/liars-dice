import random
import termios, fcntl, sys, os
from stt import *
#from liarsdice import *

SAY_AGAIN_PROMPTS = ["que?", "como?", "no entiendo", "que dijistes?", "como es?", "no escuche, que dijistes?"]

def getChar():
	fd = sys.stdin.fileno()

	oldterm = termios.tcgetattr(fd)
	newattr = termios.tcgetattr(fd)
	newattr[3] = newattr[3] & ~termios.ICANON & ~termios.ECHO
	termios.tcsetattr(fd, termios.TCSANOW, newattr)

	oldflags = fcntl.fcntl(fd, fcntl.F_GETFL)
	fcntl.fcntl(fd, fcntl.F_SETFL, oldflags | os.O_NONBLOCK)

	try:
		while 1:
		    try:
				c = sys.stdin.read(1)
				return c
		    except IOError: pass
	finally:
		termios.tcsetattr(fd, termios.TCSAFLUSH, oldterm)
		fcntl.fcntl(fd, fcntl.F_SETFL, oldflags)

class _Getch:
    """Gets a single character from standard input.  Does not echo to the
screen."""
    def __init__(self):
        try:
            self.impl = _GetchWindows()
        except ImportError:
            self.impl = _GetchUnix()

    def __call__(self): return self.impl()


class _GetchUnix:
    def __init__(self):
        import tty, sys

    def __call__(self):
        import sys, tty, termios
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch


class _GetchWindows:
    def __init__(self):
        import msvcrt

    def __call__(self):
        import msvcrt
        return msvcrt.getch()


getch = _Getch()


def ask(prompt, function):
	say(prompt)
	x = None
	while(x == None):
		sound = record()
		print sound
		try:
			x = function(sound)
			return x
		except Exception:
			i = random.randint(0, len(SAY_AGAIN_PROMPTS)-1)
			say(SAY_AGAIN_PROMPTS[i])
	
def main():
	print "Welcome!"
#	say("Hola Putas");
	x = listen()
	print x
	return
	num = ask("Cuantas personas van a jugar?", int);
	say("Cuuuuuuul. Yo empiezo...")
	say("Seis foking quinas")
#	g = Game(5*x, x, (1, 3))
	g = listen()

def getPlay(string):
	# TODO: HERLLO
	return string

def getCall(string):
	if string == None:
		return Exception
	elif "u" in string.lower():
		return "bullshit"
	elif "calzo" in string.lower():
		return "calzo"
	else:
		return string

def listen():
	print "Listening... Press 'e' if the round ended or 'spacebar' if its my turn."
	x = getch()
	if x == " ":
		# Listen
		play = None
		while (play == None):
			play = ask(" ", getPlay)
#		decision = self.players[0].decide(play)
		say("Ocho cenas")
		print "Let me know... Press 'spacebar' for me to listen."
		x = getch()
		if x == " ":
			recorded = ask("Que crees?", getCall)
			if recorded == "bullshit":
				say("buuuulcheet")
				endRound()
			else:
				return listen()
	elif x == "e":
		return endRound()
	elif x == "d":
		return None
	else:
		return listen()
		
def endRound():
	#show hand
	print "5 | 6 | 3 | 2 | 1"
	print "What happened? Press 'l' if someone lost a die, 'w' if someone won a die, 'y' if I lost a die."
	x = getch()
	if x == "l":
		print "Player lost a die"
	elif x == "w":
		print "Player won a die"
	return None
	
	
	
	

main()
