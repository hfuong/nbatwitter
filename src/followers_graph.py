# Import necessary packages
import csv
import networkx as nx
import matplotlib.pyplot as plt

# Read data
with open('data/currenttwitter_updated.csv', 'r') as nodecsv:
    nodereader = csv.reader(nodecsv)
    # Read data as list of nodes without header row
    nodes = [n for n in nodereader][1:]

nodeNames = [n[0] for n in nodes]

with open('data/followers_edgelist.csv', 'r') as edgecsv:
    edgereader = csv.reader(edgecsv)
    # Read data as tuples of edges without header row
    edges = [tuple(e) for e in edgereader][1:]

# Create directed graph
g = nx.DiGraph()

# Add nodes and edges
g.add_nodes_from(nodeNames)
g.add_edges_from(edges)

# Print graph info
print(nx.info(g))

# Plot graph - force layout to spread before drawing
plt.figure(figsize = (10, 10))

nx.spring_layout(g)
nx.draw_networkx(g)

plt.savefig('figs/followers_graph.png', format = 'png', dpi = 500)
plt.show()
