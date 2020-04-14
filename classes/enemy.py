class Enemy:
	def __init__(self, hp, mp, atkl, atkh):
		self.max_hp = hp
		self.hp = hp
		self.max_mp = mp
		self.mp = mp
		self.atkl = atkl
		self.atkh = atkh

	def printHp(self):
		return self.hp
