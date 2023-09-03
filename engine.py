

class Value:

	def __init__(self, value: float, _children=(), _op=''):
		"""
		Initialises thee Value object
		"""
		self.value = value
		self._prev = set(_children)
		self._op = _op


	def __repr__(self):
		"""
		Specifies the way the Value objects are printed
		""" 
		return f"Value(value = {self.value})"

	
	def __add__(self, other):
		"""
		Defines the addition operation between two Value objects
		"""
		return Value(self.value + other.value, _children=(self, other), _op='+'))


	def __mul__(self, other):
		"""
		Defines the multiplication operation between two Value objects
		"""
		return Value(self.value * other.value, _children=(self,other), _op='*')
