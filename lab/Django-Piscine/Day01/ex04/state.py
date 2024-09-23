import sys

def find_state():
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
	ct = sys.argv[1]
	abr = None
	for abrr, city in capital_cities.items():
		if city == ct:
			abr = abrr
			break
	if abr:
		for state, abrrv in states.items():
			if abrrv == abr:
				print(state)
				return
	else:
		print("Unknown capital city")

if __name__ == '__main__':
	find_state()
