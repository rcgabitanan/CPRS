class Node:
    def __init__(self, name):
        self.name = name
        self.connected_vertices = []  # Initialize as a list to hold connections with weights

    def get_name(self):
        return self.name

    def get_connected_vertices(self):
        return self.connected_vertices

    def append_connected_vertices(self, connected, weight):
        # Appending as tuple (connected node, weight) to store connection and weight together
        self.connected_vertices.append((connected, weight))

    def __repr__(self):
        return f"Node({self.name})"

    def __hash__(self):
        return hash(self.name)

    def __eq__(self, other):
        return self.name == other.name
