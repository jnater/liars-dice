# coding: utf-8

import random
from getch import getch
from stt import *

# ============= HELPER FUNCTIONS
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
	
def parseBet(string):
	return (3, 4)

def parseDecision(string):
	if string == None:
		return Exception
	elif "bullshit" in string.lower():
		return "bullshit"
	elif "calzo" in string.lower():
		return "calzo"
	else:
		print string, "?"
		return None
# ================================
		
# ===================== GAME CLASS
class Game(object):
	
	def __init__(self, dice_count, num_players):
		# Total number of dice in play.
		self.dice_count = dice_count
		# self.players indexes the players
		self.current = None
		self.players = [Player(dice_count, dice_count/num_players) for i in range(num_players)]
		self.position = 0


	def delete_player(self, index):
		self.players.pop(index)

	def increase_dice(self):
		self.dice_count += 1

	def decrease_dice(self):
		self.dice_count -= 1

	def step(self):
		if self.position  == 0:
			self.players[0].decide(current)
		decision = player.decide(current)
		if decision == "subo":
			self.current[0] += 1
			self.position = (self.position + 1) % 6
			self.step()
		elif decision == "calzo":
			if dice_dist[current[1] - 1] == current[0]:
				dice_count += 1
		else:
			if dice_dist[current[1] - 1] < current[0]:
			#TODO
			# players[self.position].
				pass
	
	def play(self):
		# self.speak()
		while self.players > 1:
			self.printGameState()
			self.ronda()

	def ronda(self):
		current = None
		self.players[0].roll()
		if self.position  == 0:
			decision = self.players[0].decide(current)
			say(decision)
			self.position += 1
		self.listen()

	def listen(self):
		print "Waiting for my turn... Usage:\n\t- 'e' if the round ended\n\t- 'spacebar' if its my turn\n\t- 'y' if I start"
		x = getch()
		if x == "y":
			self.position = 0
		elif x == " ":
			# Listen and decide on previous player's bet
			play = ask(" ", parseBet)
			decision = self.players[0].decide(play)
			say(decision)
			print "Waiting for next player to decide... Press 'spacebar' for me to listen."
			x = getch()
			if x == " ":
				recorded = ask("Que es lo que crees?", parseDecision)
				if recorded == "bullshit":
					say("buuuulcheet?")
					self.endRound()
				else:
					return self.listen()
		elif x == "e":
			return self.endRound()
		elif x == "d":
			return None
		else:
			print x, "?"
			return None

	def endRound(self):
		print "=== END OF ROUND ==="
		#show hands TODO: CHANGE TO MULTIPLE PLAYERS LATER IF SIMULATING
		self.players[0].print_hand()
		print "What happened? Usage:\n\t- 'l' if someone lost a die\n\t- 'w' if someone won a die\n\t- 'y' if I lost a die."
		x = getch()
		if x == "l":
			print "Player lost a die"
			self.dice_count -= 1
		elif x == "w":
			print "Player won a die"
			self.dice_count += 1
		return None

	def printGameState(self):
		print "======================="
		print "Players left ", len(self.players)
		print "Dice left ", self.dice_count
		print "======================="
			


class Player(object):
	
	def __init__(self, dice_count, own_dice):
		self.outer_dice = dice_count - own_dice
		self.own_dice = own_dice
		self.hand = [0]*own_dice

	
	def outer_expected(self, number):
		n = self.outer_dice/6
		r = self.outer_dice % 6
		if number == 1:		
			if r > 3:
				return n + 1
			else: 
				return n
		else:
			if 1 < r < 5:
				return 2*n + 1
			elif r == 5:
				return 2*n + 2
			else:
				return 2*n
	
	def expected(self, number):
			x = self.outer_expected(number) + self.hand.count(number)
			if number != 1: x += self.hand.count(1)
			return x
		

	def decide(self, current):
		# Choose the number for which you have the most.
		dice = [(i, self.hand.count(i)) for i in range(1, 7)]
		n = sorted(dice, key=lambda x: -x[1])[0][0]
		if current == None:
			return str(self.expected(n))+" "+str(n)
		else:
			print current
			amount, number = current
		
			if self.expected(number) > amount:
				return "subo"

			elif self.expected(number) == amount:
				return "calzo"

			else:
				return "bullshit"

	def roll(self):
		random.seed() # Seeds with current time
		self.hand = []
		for i in range(self.own_dice):
			self.hand.append(random.randint(1, 6))
		print "=== Perudo Rolled Dice ==="
		return self.hand

	def print_hand(self):
		d = {1: u'⚀', 2:u'⚁', 3:u'⚂', 4:u'⚃', 5:u'⚄', 6:u'⚅'}
		hand = [d[i] for i in self.hand]
		print "====="
		print repr(hand).decode("unicode-escape")
		print "====="

		
		
			
		
			
