import networkx as nx
import matplotlib.pyplot as plt

G = nx.petersen_graph()

subax1 = plt.subplot(121)

nx.draw_networkx(G, ax=subax1)

subax2 = plt.subplot(122)

nx.draw_networkx(G, ax=subax2)

plt.show()