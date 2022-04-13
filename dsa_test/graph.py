import networkx as nx
import pandas as pd
from pyvis.network import Network

class Course:
    def __init__(self, name, is_prerequisite_of=['optional']):
        self.name = name
        self.is_prerequisite_of = is_prerequisite_of
    
career = nx.DiGraph()
data = pd.read_csv('data/data.csv')
sources = data['Course_from']
targets = data['Course_to']
weights = data['is_prerequisite_of']

# creating graph
G = nx.DiGraph()
edge_data = zip(sources, targets, weights)

for e in edge_data:
    src = Course(e[0], e[2])
    dst = Course(e[1], e[2])
    G.add_edge(src.name, dst.name)

print(G.nodes)
net = Network()
# i = 0
# for node in G.nodes:
#     net.add_node(i, label=node)
#     i += 1

net.from_nx(G)
net.show('output.html')