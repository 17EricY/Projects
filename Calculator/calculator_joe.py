import re

class Calculator:

    def __init__(self):
        """
        Function to initialise calculator object

        Parameters:
        ----------
        None

        Returns:
        ----------
        None
        """
        self.__counts = {
            "+" : 0,
            "-" : 0,
            "*" : 0,
            "/" : 0,
            "^" : 0
        }
        self.__history = []

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

        if expression is None or len(expression) != 3:
            print('Please input a valid expression.')

        pattern = r'(?P<num1>-?\d+(?:\.\d+)?)\s*(?P<operator>[+\-*/%])\s*(?P<num2>-?\d+(?:\.\d+)?)'
        match = re.match(pattern, expression)
        if not match:
            raise ValueError('Could not match pattern')
        
        num1 = float(match.group("num1"))
        operator = match.group('operator')
        num2 = float(match.group('num2'))

        if operator == '+':
            return self.__add(num1, num2)
        elif operator =='-':
            return self.__minus(num1, num2)
        elif operator == '*':
            return self.__multiply(num1, num2)
        elif operator == '/':
            return self.__divide(num1, num2)
        elif operator == '^':
            return self.__power(num1, num2)
        
        print('Could not work out operator type')
        return None

    # private member methods
    def __add(self, num1: int, num2: int) -> float:
        self.__counts["+"] += 1
        return num1 + num2
    
    def __minus(self, num1: int, num2: int) -> float:
        self.__counts["-"] += 1
        return num1 - num2
    
    def __multiply(self, num1: int, num2: int) -> float:
        self.__counts["*"] += 1
        return num1 * num2
    
    def __divide(self, num1: int, num2: int) -> float:
        if num2 == 0:
            raise ValueError(F"Divisor must not be zero. got num2 [{num2}]")
        self.__counts["/"] += 1
        return num1 / num2
    
    def __power(self, num1: int, num2: int) -> float:
        self.__counts["^"] += 1
        return pow(num1, num2)
    
"""
Control loop for interacting with Calculator class
"""
calc = Calculator()
while True:

    expression = input("Input some expression in form [a + b]...")
    try:
        res = calc.compute(expression)
        print(res)
    except Exception as e:
        print(f"Error calculating expression: {e}")
