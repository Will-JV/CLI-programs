import csv

class Item:
	payrate = 0.8
	all = []																	#List to contain all the items instantiated
	def __init__(self,name: str,price: float,quantity=0):
		assert price >= 0, f"Price {price} is not greater than or equal to 0!!"
		assert quantity >=0, f"Quantity {quantity} is not greater or equal to 0!!"
		
		self.name = name
		self.price = price
		self.quantity = quantity
		
		Item.all.append(self)												#Appending list
		
	def total(self):
		return self.price*self.quantity
	
	def apply_discount(self):
		return self.price*self.payrate
		
	@classmethod
	def instantiate_from_csv(cls):											#instantiating data from csv file
		with open('item.csv','r') as f:
			reader = csv.DictReader(f)
			items = list(reader)
		for item in items:
			Item(
				name = item.get('name'),
				price = float(item.get('price')),
				quantity = int(item.get('quantity'))
				)
		
	@staticmethod	
	def is_integer(n):											#n = number
		if isinstance(n,float):
			return n.is_integer()
		elif isinstance(n,int):
			return True
		else:
			return False
			
	def __repr__(self):
		return f"Item('{self.name}',{self.price},{self.quantity})"
