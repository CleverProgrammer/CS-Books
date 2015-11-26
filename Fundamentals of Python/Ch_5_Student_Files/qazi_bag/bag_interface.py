__author__ = 'Rafeh'

class Bag:

	def __init__(self):
		self._bag = []
		pass
	
	def isEmpty(self):
		"""
		Checks to see if class is empty
		:return: True or False
		"""
		if len(self) == 0:
			return True
		else:
			return False

	def __len__(self):
		"""
		Check the current length of the object
		:return: number
		"""
		return len(self._bag)

	def __str__(self):
		"""
		Human readable representation of Bag object
		:return: string
		"""
		return str(self._bag)

	def __iter__(self):
		"""
		create an iterator for the queue
		:return:
		"""
		for item in self._bag:
			yield item

	def add(self, item):
		"""
		return the last obj put into the bag
		:param item: obj
		:return: last obj
		"""
		self._bag.append(item)
		pass

	def unstack(self):
		"""
		pop off the last item
		:return: last item
		"""
		self._bag.pop()
		pass

	def clear(self):
		self._bag = []
		pass

def run_bag():
	bag = Bag()
	print(bag)
	bag.add(5)
	print(bag)
	bag.unstack()
	print(bag)
	for i in range(10):
		bag.add(i+1)
	print(bag)
	for thing in range(len(bag)):
		bag.unstack()
		print(bag)

new_obj = Bag()
for i in range(5):
	new_obj.add(5)
print(new_obj)
new_obj.clear()
print(new_obj)
