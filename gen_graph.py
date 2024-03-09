import networkx as nx
import matplotlib.pyplot as plt
import random

# Set a random seed
seed_value = random.randint(1, 1000)
random.seed(seed_value)

# Number of nodes
n = 10000
# Create an initial graph with a small number of nodes
G = nx.barabasi_albert_graph(5, m=3)
directed_G = nx.DiGraph(G)

# Grow the graph
for i in range(6, n):
    # Randomly choose the number of edges for the new node
    m_value = random.randint(1, 5)
    # Convert set of nodes to a list
    existing_nodes = list(G.nodes())
    # Attach the new node to existing nodes
    directed_G.add_edges_from([(i, j) for j in random.sample(existing_nodes, m_value)])

# Randomly remove some edges to make them one-sided
dell = random.randint(5, 15)
edges_to_remove = random.sample(list(directed_G.edges()), k=len(directed_G.edges())//10)
directed_G.remove_edges_from(edges_to_remove)

# Visualize the graph
pos = nx.spring_layout(directed_G)
nx.draw(directed_G, pos, with_labels=True, node_size=50, node_color='skyblue', edge_color='gray', font_size=8, connectionstyle="arc3,rad=0.1")
nx.write_graphml(directed_G, f"barabasi_albert_mixed_graph_10_{n}.graphml")

plt.show()
