import random

class Game(object):
	
	def __init__(self, dice_count, num_players):
		# Total number of dice in play.
		self.dice_count = dice_count
		# self.players indexes the players
		self.current = None
		self.players = [Player() for i in range(num_players)]
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
			pass
		else:
			if dice_dist[current[1] - 1] < current[0]:
			#TODO
			# players[self.position].
			pass
	
	def play(self):
		# self.speak()
		while self.players > 1:
			self.ronda()

	def ronda(self):
		current = None
		self.players[0].roll()
		if self.position  == 0:
			decision = self.players[0].decide(current)
			# self.say(decision)
			# self.position += 1
		# self.listen()
			


class Player(object):
	
	def __init__(self, dice_count, own_dice):
		self.outer_dice = self.dice_count - self.own_dice
		self.own_dice = own_dice

	
	def outer_expected(self, number):
		n = self.outer_dice/6
		r = self.outer_dice % 2
		if number == 1:		
			if r >3:
				return n + 1
			else: 
				return n
		else:
			if 1 < r < 5:
				return 2n + 1
			elif r == 5:
				return 2n + 2
			
			else:
				return 2n
	
	def expected(self, number):
			return self.outer_expected(number, self.outer_dice) + self.own_dice[number - 1]
		

	def decide(self, current):

		n = random.randint(1,6)
		if current == None:
			return self.exptected(n)
		else:
			current = amount, number
		
			if self.expected(number) > amount:
				return "subo"

			elif self.expected(number) == amount:
				return "calzo"

			else:
				return "bullshit"

	def roll(self, n):
		#TODO
		pass

	def print_hand(self):
		#TODO
		pass
		
		
			
		
			
