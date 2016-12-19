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

def shoot(type, make):
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

	if(type==1)
		this.free_throw_attempts+=1
		if(make)
			this.free_throw_made+=1
			this.points+=1
	if(type==2)
		this.field_goal_attempts+=1
		if(make)
			this.field_goal_made+=1
			this.points+=2
	if(type==3)
		this.three_point_attempts+=1
		this.field_goal_made+=1
		if(make)
			this.three_point_made+=1
			this.field_goal_made+=1
			this.points+=3
	if(type==-1)
		this.free_throw_attempts-=1
		if(make)
			this.free_throw_made-=1
			this.points-=1
	if(type==-2)
		this.field_goal_attempts-=1
		if(make)
			this.field_goal_made-=1
			this.points-=2
	if(type==-3)
		this.three_point_attempts-=1
		this.field_goal_made-=1
		if(make)
			this.three_point_made-=1
			this.field_goal_made-=1
			this.points-=3



def rebound(offensive, num_rebounds):

	"""updates the amount of offensive and defensive rebounds

		off = type of rebound
			true = offensive
			false = defensive
	"""

	if(offensive)
		this.off_rebounds+=num_rebounds
	else
		this.def_rebounds+=num_rebounds

def assist(amount):
	
	"""updates the amount of assists by one
	"""

	this.assists+=amount

def steal(amount):
	"""updates the amount of steals
	"""

	this.steals+=amount

def block(amount):
	"""updates the amount of blocks
	"""

	this.blocks+=amount

def turnover(amount):
	"""updates the amount of turnovers
	"""

	this.turnovers+=amount

def foul(amount):
	"""updates the amount of fouls
	"""

	this.fouls+=amount

def print_stats():
	"""
		print out all stats for this player while calculating shooting percentage
	"""

	print "points: "+this.points
	print "shooting %: "+(this.field_goal_made/this.field_goal_attempts)*100
	print this.three_point_made+" - "+this.three_point_attempts
	print this.free_throw_made+" - "+this.free_throw_attempts
	print "total rebounds: "+this.off_rebounds+this.def_rebounds
	print "offensive rebounds: "+this.off_rebounds
	print "defensive rebounds: "+this.def_rebounds
	print "assists: "+this.assists
	print "steals: "+this.steals
	print "turnovers: "+this.turnovers
	print "blocks: "+this.blocks
	print "fouls: "+this.fouls


























