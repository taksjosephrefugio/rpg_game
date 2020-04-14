import random

playerhp = 260
enemyatkl = 60
enemyatkh = 80


while playerhp > 0:
	dmg = random.randrange(enemyatkl, enemyatkh)
	playerhp -= dmg

	playerhp = 0 if playerhp <= 0 else playerhp

	print("Enemy has dealt {dmg} points of damage." 
		  "Current HP is {currhp}.".format(dmg=dmg, currhp=playerhp))

	if playerhp == 0:
		print("You have died.")