import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph() #cras un grafo vacio
G.add_node(1) #Añades el nodo 1
G.add_node(2, nombre = "pedro") #añades el nodo 2 y le añades uin atributo a el mismo, en este caso nombre
G.add_edge(1,2, weight= 20) #enlazas el nodo 1 con el 2
G.add_node(3, color = "negro")
G.add_edge(3,1)
G.add_edge(2,3)
G.add_node(4)
G.add_edge(4,1)
G.add_edge(4,2)
G.add_nodes_from()


nx.draw(G, with_labels = True)
plt.show()