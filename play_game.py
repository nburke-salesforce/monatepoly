from board import Player, Board
import random
import time
import pprint
pp = pprint.PrettyPrinter(indent=2)
def get_num_players():
	num_players = raw_input("Please enter the number of players (2-8): ")
	return num_players	

def cycle(iterable):
	while True:
		for it in iterable:
			yield it

def roll_dice():
	print "rolling dice"
	raw_input("Hit any key to roll the dice")
	d1 = random.randint(1, 6) 
	d2 = random.randint(1, 6)
	roll = d1 + d2
	is_doubles = (d1 == d2)
	return (roll, is_doubles)
	# testing return (roll, is_doubles)

def advance(int_cur_location, roll):	
	next_location = (int_cur_location + roll) % 40
	return next_location

def trade(player, sucker, deed=False, cash=False):
	pass
def auction(location):
	pass


def take_turn(player, board, doubles_count = 0):
	print "Player: ", player.name
	print "money: ", player.cash
	print "Player's properties: ", [x.name for x in player.properties]
	if doubles_count == 3:
		print "You rolled doubles three times! Go to jail!"
		player.location = 10
		return player.net_worth > 0
	print "It is now %s's turn" % player.name
	roll, is_dubbs = roll_dice()
	
	player.location = advance(player.location, roll)
	print "advancing you to space %s" % str(player.location)
	ok = board.transfer_money(player, player.location)
	if not ok:
		return False
#	#check to see if it is a property:
#		if type(board.property_hash[player.location]) is str:
#			print "you landed on %s" % board.property_hash[player.location]
#			return True
#		#TODO: FIX THE BELOW ABOMINATION
#		else:
#			print board.property_hash[player.location].property_group.location_dict[player.location].name
#			if board.property_hash[player.location].property_group.location_dict[player.location] == "":	
#				buy_yes = raw_input("Would you like to buy %s (Y/n)?" % board.property_hash[player.location].name)
#				if buy_yes == 'Y':
#					board.buy(player, player.location)
#					return True
#				else:
#					return True
#			else:
#				print "Property %s is owned. You can't buy it." % board.property_hash[player.location].name
#				return True
		#board.build(player) #TODO: this is next on my list
		#other shit: mortgage at will, buy houses, etc.
	else:
	
		if is_dubbs:
			doubles_count += 1
			print "You rolled doubles! Roll again, son!"
			take_turn(player, board, doubles_count)
		return player.net_worth > 0
	 

def main():
	print "Hello and welcome to Monopoly. Follow the directions. ctrl-C to exit." 
	num_players = get_num_players()
	while num_players not in set(str(i) for i in range(2,9)):
		print "Please try again."
		num_players = get_num_players()
	num_players = int(num_players)
	players = []
	roll_order = []
	for i in range(num_players):
		name = raw_input("Please enter the name of Player %s: " % str(i + 1))
		player = Player(name)
		order = random.random()
		roll_order.append((player, order))
	print"Randomly determining the order of play (please wait---this is technology at work!)"
	roll_order.sort(key=lambda x: x[1])
	for it in roll_order:
		 players.append(it[0])
	the_board = Board(players, hack=False)
	print "The order of play will be: "
	pp.pprint([it.name for it in players])
	print "LETS PLAY!!!"
	player_group = cycle(players)
	while len(filter(lambda player: player.net_worth > 0, players)) > 1:
		curr_player = player_group.next()
		still_playing = take_turn(curr_player, the_board)
		if not still_playing:
			print "Sorry, %s, you're out." % curr_player.name
			del(players[players.index(curr_player)])
	print players[0].name, "is the winner. Congratulations, you jerk."
		
		
	
if __name__ == '__main__':
	main()
	
		
