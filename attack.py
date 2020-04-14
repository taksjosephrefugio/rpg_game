import random
from classes.enemy import Enemy

enemy = Enemy(200, 60, 45, 50)
print("Enemy HP is {enemyhp}".format(enemyhp=enemy.printHp()))

playerhp = 260
while playerhp > 0:
	dmg = random.randrange(enemy.atkl, enemy.atkh)
	playerhp -= dmg

	playerhp = 30 if playerhp <= 30 else playerhp

	print("Enemy has dealt {dmg} points of damage." 
		  "Current HP is {currhp}.".format(dmg=dmg, currhp=playerhp))

	if playerhp == 30:
		print("Your health is critically low. You've been teleported to a safe location.")
		break