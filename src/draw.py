import networkx as nx
import matplotlib.pyplot as plt
from neuralnetwork import makeNNet

def makeTuple(arc):
	return (str(arc.parent.innovation_number), str(arc.child.innovation_number))

def draw(nnet):
	G = nx.DiGraph()
	arcs = []
	for n in nnet.nodes:
		for a in n.incoming:
			arcs.append(makeTuple(a))
	G.add_edges_from(arcs)

	pos = nx.spring_layout(G)
	nx.draw(G, pos)
	nx.draw_networkx_labels(G, pos)
	plt.show()