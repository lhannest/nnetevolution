from tools.uniquelist import UniqueList

class Arc(object):
	def __init__(self, parent, child):
		self.parent = parent
		self.child = child

		self.parent.outgoing.append(self)
		self.child.incoming.append(self)

	def __eq__(self, other):
		if isinstance(other, Arc):
			return self.parent == other.parent and self.child == other.child