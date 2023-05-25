#importing the networkx library
import networkx as nx

import matplotlib.pyplot as plt

G_er = nx.erdos_renyi_graph(30,0.3)
G_ws = nx.watts_strogatz_graph(30, 3, 0.7)




plt.figure(figsize=(10,10), dpi=100)

nx.draw_networkx(G_ws, with_labels=False, style='--', node_size=100, node_color='r', alpha=0.8, width=0.5, edge_color='b')

plt.show()
