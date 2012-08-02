import time
class Property:
	def __init__(self, str_name, int_location, int_price, int_mortgage_value, property_group):
		self.name = str_name
		self.location = int_location
		self.price = int_price
		self.mortgage_value = int_mortgage_value
		self.property_group = property_group
		self.mortgaged = False
	

class ColoredProperty(Property):
	def __init__(self
			, str_name
			, int_location
			, int_price
			, int_mortgage_value
			, tpl_rents
			, colored_property_group
			):
		Property.__init__(self, str_name, int_location, int_price, int_mortgage_value, colored_property_group)
		self.rents = tpl_rents
		self.mortgaged = False

#put the logic of ownership and rent payment into the propertygroup, so that
#each propterty can have its property group to look up rent

class PropertyGroup:
	def __init__(self, tpl_int_locations):
		self.locations = tpl_int_locations
		self.initial_owners = ["" for loc in self.locations]
		if len(self.locations) != len(self.initial_owners):
			print "You can't have more owners than properties in a group!"
			raise 
		self.location_dict = dict(zip(self.locations, self.initial_owners))
	
	def is_monopoly(self):
		self.owners = self.location_dict.values()
		an_owner = self.owners[0]
		for owner in self.owners:
			if owner == "":
				return False
		for owner in self.owners:
			if owner != an_owner:
				return False
		return True
	def rent_function(self, num_owned):
		return 
class ColoredPropertyGroup(PropertyGroup):
	def __init__(self
			, tpl_int_locations
			, str_color
			):
		PropertyGroup.__init__(self, tpl_int_locations)
		self.housing_list = [0 for location in self.locations]
		self.housing_numbers = dict(zip(self.locations, self.housing_list))

	def build(self, location, prospector, board):
		#TODO: check to see if location is in the locations for the group
		if self.is_monopoly() is False:
			msg = "You can't build here because you don't have a monopoly! See if someone wants to help you out..."
			return [False, msg]
		if prospector not in self.location_dict.values():
			msg =  "You don't own this property."
			return [False, msg]
		else:	
			num_houses_on_location = self.housing_numbers[location]
			build_on_this_number = min(self.housing_numbers.values)
			if num_houses_on_location > 4:
				msg = "You've maxxed out your development! You already have a hotel here!"
				return [False, msg]
			elif num_houses_on_location != build_on_this_number:
				msg = "You must build evenly."
				valid_locations = filter(lambda key: self.housing_numbers[key] == build_on_this_number,
								self.housing_numbers.keys()
								)
				return [False, msg, valid_locations]
			elif num_houses_on_location == 4 and board.building_materials["hotels"] == 0:
				msg = "Housing shortage--no more hotels! 'Sorry!'"
				return [False, msg]
			elif num_houses_on_location < 4 and board.building_materials["houses"] == 0:
				msg = "Housing shortage--no more houses! 'Sorry!'"
				return [False, msg]
			elif num_houses_on_location == 4:
				self.housing_numbers[location] += 1
				# update building materials globally via board
				return [True, "hotel", location]
			else:
				self.housing_numbers[location] += 1
				# update building materials globally via board
				return [True, "house", location]

class UtilityPropertyGroup(PropertyGroup):
	def rent_function(self, num_owned):
		if num_owned == 1:
			print "Rolling dice!" 
			roll = random.randint() + random.randint()
			time.sleep(1)
			return 4 * roll
		elif num_owned == 2:
			print "Rolling dice!" 
			roll = random.randint() + random.randint()
			time.sleep(1)
			return 10 * roll

class RailroadPropertyGroup(PropertyGroup):
	def rent_function(self, num_owned):
		if num_owned == 1:
			return 25
		if num_owned == 1:
			return 50
		if num_owned == 1:
			return 100
		if num_owned == 1:
			return 200
