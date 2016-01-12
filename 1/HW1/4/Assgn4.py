import networkx as nx
import pygraphviz as pgv
import matplotlib.pyplot as plt
print "processing"
G=nx.read_edgelist('roadNet-TX.txt',comments='#')
print "read"
hist = nx.degree_histogram(G)
print "creating hist"
print nx.is_connected(G)



    
