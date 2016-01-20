from tools.uniquelist import UniqueList
import node
import numpy as np

import pudb

class Arc(object):
	def __init__(self, parent, child):
		assert type(parent) != node.OutputNode
		assert type(child) != node.InputNode
		assert type(child) != node.BiasNode

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

def makeArc(parent, child):
	Arc(parent, child)