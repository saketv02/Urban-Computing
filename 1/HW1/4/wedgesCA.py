import networkx as nx
import pygraphviz as pgv
import matplotlib.pyplot as plt
import itertools




print "processing"
traingle=0
wedge=0
wedgenode=0
G=nx.read_edgelist('roadNet-CA.txt',comments='#')
print "read"
for node in G.nodes_iter():
    neigh=G.neighbors(node)
    if len(neigh)>1:
        wedgenode=wedgenode+1
        for pair in itertools.combinations(neigh,2):
                if G.has_edge(pair[0],pair[1]):
                    traingle=traingle+1
                else:
                    wedge=wedge+1

ratio= float(wedgenode)/float(nx.number_of_nodes(G))
print "traingle=",traingle/3,"wedges=",wedge+traingle,"ratio=",ratio
