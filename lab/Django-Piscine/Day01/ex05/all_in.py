import sys

def find_state(capital, capital_cities, states):
	for abbr, city in capital_cities.items():
		if city.lower() == capital.lower():
			for state, state_abbr in states.items():
				if state_abbr == abbr:
					return state, city
	return None, None

def search(query, states, capital_cities):
	for state, abbr in states.items():
		if state.lower() == query.lower():
			return f"{capital_cities[abbr]} is the capital of {state}"

	state, city = find_state(query, capital_cities, states)
	if state:
		return f"{city} is the capital of {state}"

	return f"{query} is neither a capital city nor a state"

def all_in():
	if len(sys.argv) != 2:
		return
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
	queries = sys.argv[1].split(',')
	for query in queries:
		query = query.strip()
		if query:
			print(search(query, states, capital_cities))

if __name__ == "__main__":
	all_in()