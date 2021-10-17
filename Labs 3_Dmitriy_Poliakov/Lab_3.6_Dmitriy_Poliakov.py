"""
create dict called countries with several values (say 5), where keys will
be country name and value - domain name, i.e. {Ukraine:UA}

"""
countries = {
	'Ukraine': 'UA',
	'Kongo': 'KN',
	'Zimbabve': 'ZM',
	'Sierra Leone': 'SL',
	'Somali': 'SM'
	}
"""
create another dict called capitals, where values of countries will be
keys, and values will be the capitals i.e. {'UA': 'Kiev'}

"""

capitals = {
	'UA': 'Kiev',
	'KN': 'Kinshasa',
	'ZM': 'Harare',
	'SL': 'Freetown',
	'SM': 'Mogadisho'
	}
	
countries['Kongo'] = 'KN'
capitals['KN'] = 'Kinshasa'

"""print sentence "Domain for COUNTRY is DOMAIN." for each record in
countries where DOMAIN and COUNTRY have to be replaced with
.format()
print sentence "The capital of COUNTRY is CAPITAL" for each record in
capitals where COUNTRY and CAPITAL have to be replaced with
.format()"""


for key, value in countries.items():
	print ("Domain for {} is {}.".format(key, value))

for key, value in capitals.items():
	print ("The capital of {} is {}".format(key, value))	

for key, value in countries.items():
	print ("Domain for {} is {}.The capital is {}".format(key, value, capitals[value]))
		
for key, value in countries.items():
	countries[key] = [value, 'COM', 'GOV']
	
for key, value in countries.items():
	print ("Domain for {} is {}.The capital is {}".format(key, value, capitals[value[0]]))