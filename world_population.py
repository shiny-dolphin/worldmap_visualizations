import json
import pygal
from pygal.maps.world import COUNTRIES
from pygal.maps.world import World

def get_country_code(country_name):
	"""Return the pygal 2 digit country code for the given country"""
	for code, name in COUNTRIES.items():
		if name == country_name:
			return code
	#if country wasn't found, return none
	return None

#load the data into a list
filename = 'data\population_data.json'
with open(filename) as f:
	pop_data = json.load(f)
	
#print the 2010 populatino for each country
for pop_dict in pop_data:
	if pop_dict['Year'] == '2010':
		country_name = pop_dict['Country Name']
		#country_code = pop_dict['Country Code']
		population = int(float(pop_dict['Value']))
		#print("{}: {}".format(country_name, population))
		code = get_country_code(country_name)
		if code:
			print("{} ({}): {}".format(country_name, code, population))
		else:
			print("ERROR - " + country_name)