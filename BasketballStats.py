from Player import Player

"""
player=Player("Read")
player.shoot(3, True)
player.shoot(2, False)
player.shoot(2, False)
player.shoot(2, True)
player.rebound(False, 2)
player.rebound(True, 1)
player.print_stats()
"""

user_input = "";
player_list = [];

def help_me():
	#list commands here 
	print "\n \nList of commands: \n1) EXIT: exits the program \n2) DONE: finishes adding players \n3) ADDPLAYER: allows adding players"

def str2bool(v):
  return v.lower() in ("true")





while(user_input != "EXIT"):
	user_input = raw_input("Enter a command (HELP for list of commands):  ").upper()
	print user_input

	#lists the commands
	if(user_input == "HELP"):
		help_me()

	# input the players on the team
	if(user_input == "ADDPLAYER"):
		while(user_input != "DONE"):
			user_input = raw_input("Enter a player: ").upper()
			if(user_input == "DONE"):
				break
			player = Player(user_input)
			player_list.append(player)

	# command to print stats of all players
	if(user_input == "PRINT"):
		print "entered print"
		for p in player_list:
			p.print_stats()


	# command to shoot the ball
	if(user_input.find("SHOOT") != -1):
		#splits at all the spaces
		if not player_list: 
			print "No players added in list"
			break;
		#"user_input formatting example: shoot leo 1 true"
		#"values example: [shoot, leo, 1, true]"
		try:
			values = user_input.split();
			shot_type = int(values[2])
			make = str2bool(values[3])
			for p in player_list:
				if(p.name == values[1]):
					p.shoot(shot_type, make)
					print "shot recorded"
		except:
			print "invalid input, use the format 'shoot [name] [shot type] [true or false]'"


	# command to add rebounds 
	if(user_input.find("REBOUND") != -1):
		#splits at all the spaces
		if not player_list: 
			print "No players added in list"
			break;
		#"user_input formatting example: rebound read true 1"
		#"values example: [rebound, leo, true, 1]"
		try:
			values = user_input.split();
			offensive = str2bool(values[2])
			amount = int(values[3])
			for p in player_list:
				if(p.name == values[1]):
					p.rebound(offensive, amount)
					print "rebound recorded"

		except:
			print "invalid input, use the format 'rebound [name] [offensive true or false] [amount]'"

	# command to add assists
	if(user_input.find("ASSIST") != -1):
		#splits at all the spaces
		if not player_list: 
			print "No players added in list"
			break;
		#"user_input formatting example: assist leo 1"
		#"values example: [assist, leo, 1]"
		try:
			values = user_input.split();
			amount = int(values[2])
			for p in player_list:
				if(p.name == values[1]):
					p.assist(amount)
					print "assist recorded"
		except:
			print "invalid input, use the format 'assist [name] [amount]'"

	# command to add steals
	if(user_input.find("STEAL") != -1):
		#splits at all the spaces
		if not player_list: 
			print "No players added in list"
			break;
		#"user_input formatting example: steal leo 1"
		#"values example: [steal, leo, 1]"
		try:
			values = user_input.split();
			amount = int(values[2])
			for p in player_list:
				if(p.name == values[1]):
					p.steal(amount)
					print "steal recorded"
		except:
			print "invalid input, use the format 'steal [name] [amount]'"

	# command to add blocks
	if(user_input.find("BLOCK") != -1):
		#splits at all the spaces
		if not player_list: 
			print "No players added in list"
			break;
		#"user_input formatting example: block leo 1"
		#"values example: [block, leo, 1]"
		try:
			values = user_input.split();
			amount = int(values[2])
			for p in player_list:
				if(p.name == values[1]):
					p.block(amount)
					print "block recorded"
		except:
			print "invalid input, use the format 'block [name] [amount]'"

	# command to add turnover
	if(user_input.find("TURNOVER") != -1):
		#splits at all the spaces
		if not player_list: 
			print "No players added in list"
			break;
		#"user_input formatting example: turnover leo 1"
		#"values example: [turnover, leo, 1]"
		try:
			values = user_input.split();
			amount = int(values[2])
			for p in player_list:
				if(p.name == values[1]):
					p.turnover(amount)
					print "turnover recorded"
		except:
			print "invalid input, use the format 'turnover [name] [amount]'"

	# command to add fouls
	if(user_input.find("FOUL") != -1):
		#splits at all the spaces
		if not player_list: 
			print "No players added in list"
			break;
		#"user_input formatting example: foul leo 1"
		#"values example: [foul, leo, 1]"
		try:
			values = user_input.split();
			amount = int(values[2])
			for p in player_list:
				if(p.name == values[1]):
					p.foul(amount)
					print "foul recorded"
		except:
			print "invalid input, use the format 'foul [name] [amount]'"


		








