import random
import time
from rents import property_hash, board_functions, display_property_hash
from real_estate import Property, ColoredProperty
import pprint
pp = pprint.PrettyPrinter(indent=2)
class Board:
	def __init__(self, players, hack=True):	
		if hack:
			self.rent_hash = dict(zip([i for i in range(40)], [2*i for i in range(40)]))
		else:
			self.property_hash = property_hash
			self.display_property_hash = display_property_hash
			self.players = players
	
	def transfer_money(self, player, int_location):
		space = self.property_hash[int_location]
		if isinstance(space, Property):
			owner = space.property_group.location_dict[int_location]
		else:	
			owner = ""	
			player.cash += board_functions[space]# TODO: need this as a function of board, everyone		
			player.net_worth += board_functions[space]
			if player.net_worth <= 0:
				return False
			while player.cash < 0:
				mortgaged = self.mortgage(player)
				if not mortgaged:
					return False
			return True			
			
		if owner == "":
			buy = raw_input("No one owns this. Do you want to buy it? (Y/n) ")
			if buy == "Y":
				self.buy(player, int_location)
				return True
			else:
				#self.auction(location) #players? does this need players as input?
				return True
		elif space.mortgaged:
			print "This space is mortgaged. No need to pay."
			return True
		else: 
			if isinstance(space, ColoredProperty):
				num_houses = space.property_group.housing_numbers[int_location]
				if num_houses == 0 and space.property_group.is_monopoly:
					rent = space.rents[0] * 2
				else:
					rent = space.rents[num_houses]
				print "You owe %s %s in rent!" % (owner.name, str(rent))
				while player.cash - rent < 0:
					print "You need to mortgage one of your properties in order to pay."
					mortgaged = self.mortgage(player)
					if not mortgaged:
						return False
				player.cash -= rent	
				player.net_worth -= rent
				owner.cash += rent
				owner.net_worth += rent
				return True
			else:
				num_owned = len(filter(lambda ownr: ownr == owner, space.property_group.location_dict.values()))
				rent = space.property_group.rent_function(num_owned)
				print "You owe %s %s in rent!" % (owner.name, str(rent))
				while player.cash - rent < 0:
					print "You need to mortgage one of your properties in order to pay."
					mortgaged = self.mortgage(player)
					if not mortgaged:
						return False
				player.cash -= rent	
				player.net_worth -= rent
				owner.cash += rent
				owner.net_worth += rent
				return True
		
	def mortgage(self, player):
		if len(player.properties) == 0:
			return False
		pp.pprint(self.display_property_hash)
		time.sleep(1)
		print "You own these:"
		prop_names = [(x.location, x.name) for x in player.properties]
		pp.pprint(prop_names) 
		mortgaged_property_loc = raw_input("Please enter the number of a property that you own: ")
		while mortgaged_property_loc not in set([str(prop.location) for prop in player.properties]):
			mortgaged_property_loc = raw_input("Please enter the number of a property that you own: ")
		mortgaged_prop = int(mortgaged_property_loc)
		self.property_hash[mortgaged_prop].mortgaged = True
		player.cash += self.property_hash[mortgaged_prop].mortgage_value
		#player.net_worth is unchanged.
		print "You have mortgaged %s" % self.property_hash[mortgaged_prop].name
		return True

	def buy(self, player, int_location):
		space = self.property_hash[int_location]			
		if isinstance(space, Property):	
			#check to see if it's owned
			owner = space.property_group.location_dict[int_location]
			if owner == "":
				#buy = raw_input("Property %s is unowned. Would you like to buy it? (Y/n) " % space.name)
				#if buy == "Y":
				if player.cash >= space.price:
					player.cash -= space.price
					player.net_worth -= space.price
					player.net_worth += space.mortgage_value
					space.property_group.location_dict[int_location] = player
					player.properties.append(space)
				elif player.cash < space.price and player.net_worth >= space.price:
					mort = raw_input("Would you like to mortgage to buy this? (Y/n) ")
					if mort == "Y":
						while player.cash < space.price:
							self.mortgage(player)
						
						player.cash -= space.price
						player.net_worth -= space.price
						player.net_worth += space.mortgage_value
						space.property_group.location_dict[int_location] = player
						player.properties.append(space)
						return
					else:
			
						self.auction(int_location)
						return
				else:
					print "You can't afford %s" % space.name
					return
				#else:
				#	self.auction(int_location)
			else:
				print "This property is owned by %s" % owner.name
				return
		else:
			print "This property is not buyable."
			return
	
	def build(self, player):
		#check to see if player has properties to build on
		#if no, say sorry
		#if yes, then take location, look up property, property group in board hash. build.
		if len(player.properties) == 0:
			print "You have nothing to build on!"
			return
		else:
			monopoly_properties = filter(lambda x: x.property_group.is_monopoly, player.properties)
			buildable_properties = filter(lambda x: hasattr(x.property_group, "build"), monopoly_properties)
			if len(buildable_properties) == 0:
				print "You have no monopolies on colored properties. You can't build yet."
				return
			property_dict = dict(zip([i for i in range(len(buildable_properties))], [prop.name for prop in buildable_properties]))
			print "You own these properties: "
			pp.pprint(property_dict)
			to_build = raw_input("Enter the digit of a property: ")
			while to_build not in set(property_dict.keys()):
				to_build = raw_input("Please enter the number of a property that you own: ")
			prop_to_build = property_dict[to_build]
			int_location = prop_to_build.location
			cost_of_house = building_costs[int_location]
			if player.net_worth < cost_of_house:
				print "You can't afford it."
				return
			while player.cash < cost_of_house:
				print "You don't have enough cash to build."
				mtg_to_build = raw_input("Would you like to mortgage a property (M) or sell a house (s)? (M/s): ")
				if mgt_to_build == "M":
					self.mortgage(player)
				else:
					print "not implemented" 
					return
					#self.sell_house(player)			
			player.cash -= cost_of_house
			player.net_worth -= cost_of_house
			prop_to_build.property_group.build(prop_to_build.location, player)
			
		building_materials={"houses": 32, "hotels": 12}

class Player:
	def __init__(self, str_name):
		self.cash = 1500
		self.location = 0
		if len(str_name) > 0:
			self.name = str_name
		else: 
			self.name = "bozo" + str(random.random())[4:]
		self.net_worth = self.cash
		self.properties = [] # tuple of location numbers


