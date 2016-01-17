def getUniqueItems(items):
	result = []
	for item in items:
		if item not in result:
			result.append(item)
	return result

class UniqueList(list):
	def __init__(self, items=[]):
		list.__init__(self, getUniqueItems(items))

	def append(self, item):
		if item not in self:
			list.append(self, item)