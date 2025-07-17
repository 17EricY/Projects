import traceback
import re

class Calculator:

	def __init__(self):
		self.__count = {
			"Addition" : 0,
			"Subtraction" : 0,
			"Multiplication" : 0, 
			"Division" : 0, 
			"Squared" : 0
			}
		self.__history = []
	
	def __get_addition_result(self, num1, num2):
		self.__count["Addition"] += 1
		return num1 + num2
	
	def __get_subtraction_result(self, num1, num2):
		self.__count["Subtraction"] += 1
		return num1 - num2

	def __get_multiplication_result(self, num1, num2):
		self.__count["Multiplication"] += 1
		return num1 * num2

	def __get_division_result(self, num1, num2):
		if num2 == 0:
			raise ValueError('Divisor cannot be 0 in a division equation')
		self.__count["Division"] += 1
		return num1 / num2

	def __get_squared_result(self, num1, num2): 
		self.__count["Squared"] += 1
		return pow(num1, num2)
	
	def compute(self, expression: str = None) -> float:
		"""
		Function to compute some expression

		Parameters:
		----------
		expression : str (default None)
			Expression string for the calculator to 

		Returns:
		----------
		Float
			Computed Expression
		"""
		pattern = r'(?P<num1>-?\d+(?:\.\d+)?)\s*(?P<operator>[+\-^*/%])\s*(?P<num2>-?\d+(?:\.\d+)?)'
		match = re.match(pattern, expression)
		if not match:
			raise ValueError('Could not match pattern')

		num1 = float(match.group("num1"))
		operator = match.group('operator')
		num2 = float(match.group('num2'))

		if operator == '+':
			res = self.__get_addition_result(num1, num2)
		elif operator == '-':
			res = self.__get_subtraction_result(num1, num2)
		elif operator == '*':
			res = self.__get_multiplication_result(num1, num2)
		elif operator == '/':
			res = self.__get_division_result(num1, num2)
		elif operator == '^':
			res = self.__get_squared_result(num1, num2) 
		else:
			print('Calculation is not possible.')
			return
		
		self.__history.append(f'{num1} {operator} {num2} = {res}')
		return res

	def display_history(self):
		"""
		Function to display the history of previous computations

		Parameters:
		----------
		None

		Returns:
		----------
		None
		"""
		print('\n--- Equation History')
		for i, equation in enumerate(self.__history):
			print(f'{i}: {equation}')

	def display_stats(self):
		"""
		Function to display statistics of previous computations

		Parameters:
		----------
		None

		Returns: 
		----------
		None
		"""
		for key, value in self.__count.items():
			print(f'{key} has count {value}')


"""
Main script for testing calculator
"""
"""
calc = Calculator()
while True:
	 
	user_input = input("Write two numbers in the form [a + b], type 'h' for history, or 's' for calculator statistics.\n--> ")
	try:
		if user_input == 'h':
			calc.display_history()
		elif user_input == 's':
			calc.display_stats()
		else:
			result = calc.compute(user_input)
			print(result)
	except Exception as e:
		print(f'User Input [{user_input}] is invalid.\n{e}')
		traceback.print_exc()
"""