from tools.uniquelist import UniqueList
import numpy as np

class Arc(object):
	def __init__(self, parent, child):
		self.parent = parent
		self.child = child
		self.weight = np.random.randn()

		self.parent.outgoing.append(self)
		self.child.incoming.append(self)

	def copy(self, parent, child):
		arc = Arc(parent, child)
		arc.weight = self.weight
		return arc

	def __eq__(self, other):
		if isinstance(other, Arc):
			return self.parent == other.parent and self.child == other.child

	def __repr__(self):
		return 'Arc[' + str(self.parent) + ', ' + str(self.child) + ']'

	def __del__(self):
		self.parent.outgoing.remove(self)
		self.child.outgoing.remove(self)