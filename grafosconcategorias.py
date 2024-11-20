import networkx as nx
import matplotlib.pyplot as plt

ponderacion = {
    "disponibilidad": 5
}

def arbol(graph):
    return nx.is_connected(graph) and graph.number_of_edged() == graph.number_of_nodes

def calcular_peso(n1,n2):
    peso=0
    for atributo in n1[1].items():
        #print(atributo)
        for atributo2 in n2[1].items():
            if atributo == atributo2:
                if atributo[0] in ponderacion:
                    peso += ponderacion[atributo[0]]
                else:
                    peso += 1
    return

G1 = nx.Graph() #cras un grafo vacio

categorias = {
    "camisetas amarillas": {"producto": "camiseta", "color": "amarillo", "talla": "M", "precio": 19.99, "disponibilidad": True},
    "pantalones negros": {"producto": "pantalones", "color": "negro", "talla": "L", "precio": 29.99, "disponibilidad": False},
    "zapatos rojos": {"producto": "zapatos", "color": "rojo", "talla": 42, "precio": 49.99, "disponibilidad": False},
    "gorras azules": {"producto": "gorra", "color": "azul", "talla": "Única", "precio": 15.99, "disponibilidad": True},
    "chaquetas verdes": {"producto": "chaqueta", "color": "verde", "talla": "M", "precio": 59.99, "disponibilidad": True},
    "calcetines blancos": {"producto": "calcetines", "color": "blanco", "talla": "Única", "precio": 5.99, "disponibilidad": True},
    "bufandas grises": {"producto": "bufanda", "color": "gris", "talla": "Única", "precio": 12.99, "disponibilidad": True},
    "guantes negros": {"producto": "guantes", "color": "negro", "talla": "L", "precio": 9.99, "disponibilidad": False},
    "sombreros marrones": {"producto": "sombrero", "color": "marrón", "talla": "M", "precio": 22.99, "disponibilidad": True},
    "bikinis rosados": {"producto": "bikini", "color": "rosado", "talla": "S", "precio": 34.99, "disponibilidad": True},
    "botas negras": {"producto": "botas", "color": "negro", "talla": 40, "precio": 79.99, "disponibilidad": True},
    "camisas blancas": {"producto": "camisa", "color": "blanco", "talla": "L", "precio": 25.99, "disponibilidad": True}
}
#atributos desempaquetan automaticamente el diccionario y pasa 
#sus elementos con argumentos como de oalan¡bras clave a la funcion
for categoria, atributos in categorias.items():
    G1.add_node(categoria, **atributos)

G1.add_edge("camisetas amarillas","pantalones negros")
G1.add_edge("camisetas amarillas","botas negras")
G1.add_edge("bikinis rosados", "guantes negros")
G1.add_edge("bikinis rosados", "calcetines blancos")
G1.add_edge("bikinis rosados",  "zapatos rojos")
G1.add_edge("bikinis rosados",   "bufandas grises")
G1.add_edge("bikinis rosados", "gorras azules")
G1.add_edge("botas negras", "bufandas grises")
G1.add_edge("chaquetas verdes", "camisas blancas")
G1.add_edge("sombreros marrones", "camisas blancas")
G1.add_edge("chaquetas verdes", "botas negras")
G1.add_edge("sombreros marrones", "botas negras")


for nodo in G1.nodes.items():
    #print(nodo)
    for nodo2 in G1.nodes.items():
        if nodo2 == nodo:
            pass
        else:
            peso = calcular_peso(nodo, nodo2)
            print(f"Enlace de {nodo[0]} a {nodo[0]} con peso {peso}")
            G1.add_edge(nodo [0], nodo2[0], weight = peso)

nx.draw(G1, with_labels = True)
plt.show()