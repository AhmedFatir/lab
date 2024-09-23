import random
from beverages import HotBeverage, Coffee, Tea, Chocolate, Cappuccino

class CoffeeMachine:
	def __init__(self):
		self.drinks_served = 0
		self.broken = False

	class EmptyCup(HotBeverage):
		def __init__(self):
			self.name = "empty cup"
			self.price = 0.90

		def description(self):
			return "An empty cup?! Gimme my money back!"

	class BrokenMachineException(Exception):
		def __init__(self):
			super().__init__("This coffee machine has to be repaired.")

	def repair(self):
		self.broken = False
		self.drinks_served = 0

	def serve(self, beverage_class):
		if self.broken:
			raise CoffeeMachine.BrokenMachineException()

		if random.choice([True, False]):
			drink = beverage_class()
		else:
			drink = self.EmptyCup()

		self.drinks_served += 1

		if self.drinks_served >= 10:
			self.broken = True

		return drink

def Test():
	machine = CoffeeMachine()

	beverages = [Coffee, Tea, Chocolate, Cappuccino]

	while True:
		try:
			for beverage in beverages:
				print(machine.serve(beverage))
				print()  # Add a line break between drinks
		except CoffeeMachine.BrokenMachineException as e:
			print(e)
			print("Repairing the machine...")
			machine.repair()
			
			print("--------------Machine repaired!--------------")
			print(machine.serve(beverage))

if __name__ == "__main__":
	Test()