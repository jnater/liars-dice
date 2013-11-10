class Game(object):
	
	def __init__(self, dice_count, players, current):
		self.dice_count = dice_count
		self.players = players
		#self.current is a tuple. e.g. (27,5) = 27 quinas
		self.current = current
		self.position = 0

	
	def step(self):
		player = Player(sum(dice_count) - len(players[self.position]), players[self.position])
		decision = player.decide(current)
		if decision == "subo":
			self.current[0] += 1
			self.position = (self.position + 1) % 6
			self.step()
		elif decision == "calzo":
			if dice_count[current[1] - 1] == current[0]:
			#TODO
			pass
		else:
			if dice_count[current[1] - 1] < current[0]:
			#TODO
			pass
			


class Player(object):
	
	def __init__(self, outer_dice, own_dice):
		self.outer_dice = outer_dice
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
		

	def decide(current):
		current = amount, number
		
		if self.expected(number) > amount:
			return "subo"

		elif self.expected(number) == amount:
			return "calzo"

		else:
			return "bullshit"
		
		
			
		
			
