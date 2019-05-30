def convert_grade_to_num(grade):
	if(grade == 'F'):
		return 0.15
	elif(grade == 'E'):
		return 0.30
	elif(grade == 'D'):
		return 0.45
	elif(grade == 'C'):
		return 0.60
	elif(grade == 'B'):
		return 0.75
	elif(grade == 'A'):
		return 0.9
	elif(grade == "S"):
		return 1.0
	elif(grade == "SS"):
		return 2.0
def convert_num_to_grade(num):
	if(num >= 0 and num <= 0.15):
		return 'F'
	elif(num > 0.15 and num <= 0.30):
		return 'E'
	elif(num > 0.30 and num <= 0.45):
		return 'D'
	elif(num > 0.45 and num <= 0.60):
		return 'C'
	elif(num > 0.60 and num <= 0.75):
		return 'B'
	elif(num > 0.75 and num <= 0.90):
		return 'A'
	elif(num > 0.90 and num <= 1.0):
		return "S"
	elif(num > 1.0):
		return "SS"

def remove_commas(string):
	element_list = []
	current_element = ""

	for c in string:
		if(c != ','):
			current_element += c 
		else:
			element_list.append(current_element)
			current_element = ""
	element_list.append(current_element)
	print(element_list)
	return element_list

def concat_list(list):
	s = ""
	for elem in list:
		s += elem + ' '
	return s

class Pais:
	
	def __init__(self, name):
		self.name 			= name
		self.population 	= 0
		self.attack_power 	= 0.0
		self.defense_power 	= 0.0
		self.fertility 		= 0.0
		#self.charisma 		= 0.0

		self.relations = {}

	def attack(self, enemy):
		effective_power = self.attack_power  - enemy.defense_power
		battle_loss 	= self.defense_power - enemy.defense_power
		
		enemy.lose_pop(effective_power * self.population)
		self.lose_pop(battle_loss * enemy.population)

	def lose_pop(self, amount):
		self.population -= amount

	def update(self):
		self.population += fertility * self.population

	def get_relations(self, pais):
		return self.relations[pais][1]

	def is_ally(self, pais):
		return self.relations[pais][0]

	def get_allies(self):
		allies = []
		for p in self.relations:
			if(self.relations[p][0] == True):
				allies.append(p.name)
		return allies

	def get_good_rel(self):
		good = []
		for p in self.relations:
			if(self.relations[p][1] >= 0.5):
				good.append(p.name)
		return good

	def get_bad_rel(self):
		bad = []
		for p in self.relations:
			if(self.relations[p][1] <= -0.5):
				bad.append(p.name)
		return bad

	def print_status(self):
		print("Name       : " + self.name)
		print("Population : " + str(self.population))
		print("Atk Pwr    : " + convert_num_to_grade(self.attack_power))
		print("Def Pwr    : " + convert_num_to_grade(self.defense_power))
		print("Fertility  : " + convert_num_to_grade(self.fertility))
		#print("Charisma   : " + convert_num_to_grade(self.charisma))
		print("Allies     : " + concat_list(self.get_allies()))
		print("Good Rel   : " + concat_list(self.get_good_rel()))	
		print("Bad Rel    : " + concat_list(self.get_bad_rel()))

class World:
	
	def __init__(self):
		self.countries = []

		with open("def_inst.txt", 'r') as state_file:
			for l in state_file:
				if(l[0] == '#'):
					continue
				
				line_split = l.split()
				print(line_split)
				
				new_country = Pais(line_split[0])

				new_country.population = int(line_split[1])
				new_country.attack_power = convert_grade_to_num(line_split[2])
				new_country.defense_power = convert_grade_to_num(line_split[3])
				new_country.fertility = convert_grade_to_num(line_split[4])
				#new_country.charisma = convert_grade_to_num(line_split[5])

				self.countries.append(new_country)

		for country0 in self.countries:
			for country1 in self.countries:
				if(country1 != country0):
					country0.relations[country1] = [False, 0]

		with open("def_rel.txt", 'r') as relation_file:
			for l in relation_file:
				if(l[0] == '#'):
					continue

				line_split = l.split()

				current_country = self.get_country_by_name(line_split[0])

				print(line_split)

				for country in remove_commas(line_split[1]):
					if(country != '0'):
						current_country.relations[self.get_country_by_name(country)][0] = True

				for country in remove_commas(line_split[2]):
					if(country != '0'):
						current_country.relations[self.get_country_by_name(country)][1] = 1.0

				for country in remove_commas(line_split[3]):
					if(country != '0'):
						current_country.relations[self.get_country_by_name(country)][1] = -1.0

	def get_country_by_name(self, string):

		for country in self.countries:
			if(country.name == string):
				return country
		return self.countries[-1]


world = World()







