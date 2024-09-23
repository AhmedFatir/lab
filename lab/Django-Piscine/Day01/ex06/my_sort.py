def sort_dictionary():
	d = {
		'Hendrix' : '1942',
		'Allman' : '1946',
		'King' : '1925',
		'Clapton' : '1945',
		'Johnson' : '1911',
		'Berry' : '1926',
		'Vaughan' : '1954',
		'Cooder' : '1947',
		'Page' : '1944',
		'Richards' : '1943',
		'Hammett' : '1962',
		'Cobain' : '1967',
		'Garcia' : '1942',
		'Beck' : '1944',
		'Santana' : '1947',
		'Ramone' : '1948',
		'White' : '1975',
		'Frusciante': '1970',
		'Thompson' : '1949',
		'Burton' : '1939',
	}
	# Sort the dictionary by year (value) and then by name (key)
	sorted_items = sorted(d.items(), key=lambda x: (x[1], x[0]))

	# the sorted() function with a custom key parameter to sort the dictionary items:
	# The key function lambda x: (x[1], x[0]) tells sorted() to:
	# first sort by the year (x[1], which is the value), 
	# and then by the name (x[0], which is the key).
	
	# Extract only the names (keys) from the sorted items
	sorted_names = [item[0] for item in sorted_items]
	for name in sorted_names:
		print(name)

if __name__ == '__main__':
	sort_dictionary()