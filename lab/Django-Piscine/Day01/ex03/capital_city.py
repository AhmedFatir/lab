import sys

def find_capital_city():
	states = {
		"Oregon": "OR",
		"Alabama": "AL",
		"New Jersey": "NJ",
		"Colorado": "CO"
	}

	capital_cities = {
		"OR": "Salem",
		"AL": "Montgomery",
		"NJ": "Trenton",
		"CO": "Denver"
	}
	if len(sys.argv) != 2:
		return
	st_name = sys.argv[1]
	st_abb = states.get(st_name)
	if st_abb:
		capital = capital_cities.get(st_abb)
		if capital:
			print(capital)
		else:
			print("Unknown state")
	else:
		print("Unknown state")

if __name__ == '__main__':
	find_capital_city()
