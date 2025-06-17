# ================================
# 📘 DATA STRUCTURE CHEAT SHEET - PYTHON
# ================================


# ------------------------
# 📚 Stack (LIFO: Last-In, First-Out)
# ------------------------
# A stack is like a pile of books: the last one you put on top is the first you remove.
# Commonly used in backtracking, expression parsing, undo mechanisms.

my_stack = [10, 20, 30, 40, 50]  # Stack initialized (50 is at the top)
my_stack.append(60)             # Push operation (adds 60 on top)
print(my_stack)                 # Output: [10, 20, 30, 40, 50, 60]

my_stack.pop()                  # Pop operation (removes 60)
my_stack.pop()                  # Pop again (removes 50)
print(my_stack)                 # Output: [10, 20, 30, 40]

# Logic: Push adds to end; Pop removes from end (last in, first out)


# ------------------------
# 📬 Queue (FIFO: First-In, First-Out)
# ------------------------
# Like a real-life queue: the first person in line is the first to be served.
# Used in scheduling, buffering, and real-time systems.

from collections import deque

# deque (double-ended queue) provides efficient append and popleft
my_queue = deque(["Roger Federer", "Rafael Nadal", "Novak Djokovic"])
my_queue.append("Andre Agassi")    # Enqueue operation
my_queue.append("Pete Sampras")
print(my_queue)                    # Output: deque([...])

my_queue.popleft()                 # Dequeue operation (removes Roger)
my_queue.popleft()                 # Removes Rafael
print(my_queue)                    # Remaining: Novak, Andre, Pete

# Logic: Queue works from both ends using deque — append to right, pop from left


# ------------------------
# 🌐 Graph (Adjacency List Representation)
# ------------------------
# A graph is a collection of nodes (vertices) and edges (connections).
# Used in modeling relationships, social networks, routing algorithms.
# Adjacency list stores which nodes are connected to each other.

my_graph = {
    'A': ['B', 'C'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', 'D', 'E'],
    'D': ['B', 'C', 'E'],
    'E': ['D', 'C']
}

def define_edges(graph):
    edges = []
    for node in graph:
        for neighbor in graph[node]:
            edges.append((node, neighbor))
    return edges

print(define_edges(my_graph))
# Output: List of all directed edges between nodes

# Logic: For each node, pair it with every connected node to get all edges


# ------------------------
# 🌳 Tree (Binary Tree Example)
# ------------------------
# A tree has a root node at the top, branches (intermediate nodes), and leaf nodes.
# Binary tree: each node has at most 2 children.
# Used in databases, file systems, decision-making structures.

class Tree:
    def __init__(self, info, left=None, right=None):
        self.info = info
        self.left = left
        self.right = right

    def __str__(self):
        return f'{self.info}, Left: {self.left}, Right: {self.right}'

# Example Tree:
#           Root
#         /      \
#    Branch_1  Branch_2
#     /    \      /    \
# Leaf1 Leaf2  Leaf3 Leaf4

tree = Tree("Root", Tree("Branch_1", "Leaf_1", "Leaf_2"),
            Tree("Branch_2", "Leaf_3", "Leaf_4"))
print(tree)

# Logic: Trees help represent hierarchical data and support fast search/insertion

# ✅ Dictionary (hash maps) will be covered in the next unit.
