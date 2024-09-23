def read_and_write():
	try:
		with open("../dev/ex01/numbers.txt", "r") as file:
			numbers = file.read()
			numbers = numbers.split(",")
			for number in numbers:
				print(number)
	except FileNotFoundError:
		print("The file numbers.txt was not found.")

if __name__ == '__main__':
	read_and_write()