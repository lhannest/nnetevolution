from node import Node
from arc import Arc
from evolution import getParent

a = Node()
b = Node()
c = Node()
Arc(a, b)
Arc(b, c)

print a, b, c