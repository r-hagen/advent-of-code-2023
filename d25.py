import networkx as nx
import matplotlib.pyplot as plt

graph = nx.Graph()

for line in open("in").read().splitlines():
    left, right = line.split(": ")
    right = right.split()
    for node in right:
        graph.add_edge(left, node)

print(graph)
# nx.draw_networkx(graph)
# plt.show()

graph.remove_edges_from(nx.minimum_edge_cut(graph))
print(graph)

a, b = nx.connected_components(graph)
print("part1", len(a) * len(b))
