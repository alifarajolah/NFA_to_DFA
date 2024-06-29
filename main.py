import networkx as nx
import matplotlib.pyplot as plt

# تعریف گراف
G = nx.DiGraph()

# اضافه کردن رئوس (وضعیت‌ها)
G.add_nodes_from(['q0', 'q1', 'q2'])

# اضافه کردن یال‌ها (انتقالات)
G.add_edge('q0', 'q1', input='0')
G.add_edge('q0', 'q0', input='1')
G.add_edge('q1', 'q2', input='1')
G.add_edge('q1', 'q1', input='0')
G.add_edge('q2', 'q2', input='0')
G.add_edge('q2', 'q2', input='1')

# نمایش گراف
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_size=2000, node_color='skyblue', font_size=20, font_weight='bold', arrowsize=20)
plt.show()
