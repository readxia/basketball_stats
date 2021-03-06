class Player(object):
	name=""
	points=0
	field_goal_attempts=0
	field_goal_made=0
	three_point_attempts=0
	three_point_made=0
	free_throw_attempts=0
	free_throw_made=0
	off_rebounds=0
	def_rebounds=0
	assists=0
	steals=0
	blocks=0
	turnovers=0
	fouls=0

	def __init__(self, name):
		self.name = name

	def shoot(self, type, make):
		"""edits data for shooting percentage and calculates
		points

		type: type of shot 
			1 = free throw
			2 = field goal
			3 = three points
			-1 = undo free throw
			-2 = undo field goal
			-3 = undo three point
		make: boolean for made or missed shot
		"""

		if(type==1):
			self.free_throw_attempts+=1
			if(make):
				self.free_throw_made+=1
				self.points+=1
		if(type==2):
			self.field_goal_attempts+=1
			if(make):
				self.field_goal_made+=1
				self.points+=2
		if(type==3):
			self.three_point_attempts+=1
			self.field_goal_attempts+=1
			if(make):
				self.three_point_made+=1
				self.field_goal_made+=1
				self.points+=3
		if(type==-1):
			self.free_throw_attempts-=1
			if(make):
				self.free_throw_made-=1
				self.points-=1
		if(type==-2):
			self.field_goal_attempts-=1
			if(make):
				self.field_goal_made-=1
				self.points-=2
		if(type==-3):
			self.three_point_attempts-=1
			self.field_goal_attempts-=1
			if(make):
				self.three_point_made-=1
				self.field_goal_made-=1
				self.points-=3



	def rebound(self, offensive, num_rebounds):

		"""updates the amount of offensive and defensive rebounds

			off = type of rebound
				true = offensive
				false = defensive
		"""

		if(offensive):
			self.off_rebounds+=num_rebounds
		else:
			self.def_rebounds+=num_rebounds

	def assist(self, amount):
	
		"""updates the amount of assists by one
		"""

		self.assists+=amount

	def steal(self, amount):
		"""updates the amount of steals
		"""

		self.steals+=amount

	def block(self, amount):
		"""updates the amount of blocks
		"""

		self.blocks+=amount

	def turnover(self, amount):
		"""updates the amount of turnovers
		"""

		self.turnovers+=amount

	def foul(self, amount):
		"""updates the amount of fouls
		"""

		self.fouls+=amount

	def print_stats(self):
		"""
			print out all stats for self player while calculating shooting percentage
		"""

		print self.name
		print "points: "+ str(self.points)
		if(self.field_goal_attempts==0):
			print "shooting %: 0"
		else:
			print "shooting %: "+str((float(self.field_goal_made)/self.field_goal_attempts)*100)
		print "field goals: "+str(self.field_goal_made)+" - "+str(self.field_goal_attempts)
		print "three points: "+str(self.three_point_made)+" - "+str(self.three_point_attempts)
		print "free throws: "+str(self.free_throw_made)+" - "+str(self.free_throw_attempts)
		print "total rebounds: "+str(self.off_rebounds+self.def_rebounds)
		print "offensive rebounds: "+str(self.off_rebounds)
		print "defensive rebounds: "+str(self.def_rebounds)
		print "assists: "+str(self.assists)
		print "steals: "+str(self.steals)
		print "turnovers: "+str(self.turnovers)
		print "blocks: "+str(self.blocks)
		print "fouls: "+str(self.fouls)

	def write_stats(self, stat_sheet):
		"""
			print out all stats for self player while calculating shooting percentage
		"""

		stat_sheet.write(self.name+"\n")
		stat_sheet.write("points: "+ str(self.points)+"\n")
		if(self.field_goal_attempts==0):
			stat_sheet.write("shooting %: 0\n")
		else:
			stat_sheet.write("shooting %: "+str((float(self.field_goal_made)/self.field_goal_attempts)*100)+"\n")
		stat_sheet.write("field goals: "+str(self.field_goal_made)+" - "+str(self.field_goal_attempts)+"\n")
		stat_sheet.write("three points: "+str(self.three_point_made)+" - "+str(self.three_point_attempts)+"\n")
		stat_sheet.write("free throws: "+str(self.free_throw_made)+" - "+str(self.free_throw_attempts)+"\n")
		stat_sheet.write("total rebounds: "+str(self.off_rebounds+self.def_rebounds)+"\n")
		stat_sheet.write("offensive rebounds: "+str(self.off_rebounds)+"\n")
		stat_sheet.write("defensive rebounds: "+str(self.def_rebounds)+"\n")
		stat_sheet.write("assists: "+str(self.assists)+"\n")
		stat_sheet.write("steals: "+str(self.steals)+"\n")
		stat_sheet.write("turnovers: "+str(self.turnovers)+"\n")
		stat_sheet.write("blocks: "+str(self.blocks)+"\n")
		stat_sheet.write("fouls: "+str(self.fouls)+"\n")
		stat_sheet.write("-------------------------------------\n")
		stat_sheet.write("\n")


























