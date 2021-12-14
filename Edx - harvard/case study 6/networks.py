import networkx as nx 
import matplotlib.pyplot as plt

# G = nx.Graph()
# G.add_nodes_from(1,2,3,4)
# G.add_edges_from((1,2),(3,4))
# G.number_of_nodes(), G.number_of_edges()

G = nx.karate_club_graph()
print(G.number_of_nodes(), G.number_of_edges())

print(G.degree(0) is G.degree()[0])

D = {1:1, 2:2, 3:3}
plt.hist(D)
plt.show() 