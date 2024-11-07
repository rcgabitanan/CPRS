import random
from node import Node
import heapq

def create_graph(n, m):
    # Create nodes and store them in a dictionary for easy access
    nodes = {f"x{i}": Node(f"x{i}") for i in range(n)}

    for node in nodes.values():
        num_connections = random.randint(1, m)  # At least 1 connection per node
        while len(node.get_connected_vertices()) < num_connections:
            other_node = random.choice(list(nodes.values()))
            if other_node != node and other_node.get_name() not in [c[0] for c in node.get_connected_vertices()]:
                weight = random.randint(1, 10)
                node.append_connected_vertices(other_node.get_name(), weight)
                other_node.append_connected_vertices(node.get_name(), weight)  # Ensure bidirectional connection
    
    return nodes

def dijkstra(nodes, start, end):
    # Priority queue for shortest path search
    queue = [(0, start)]
    distances = {node: float('inf') for node in nodes}
    distances[start] = 0
    previous_nodes = {node: None for node in nodes}

    while queue:
        current_distance, current_node = heapq.heappop(queue)

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in nodes[current_node].get_connected_vertices():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_nodes[neighbor] = current_node
                heapq.heappush(queue, (distance, neighbor))

    path, node = [], end
    while previous_nodes[node] is not None:
        path.append(node)
        node = previous_nodes[node]
    path.append(start)
    path.reverse()

    return path, distances[end]

def main():
    n = int(input("Enter the number of nodes: "))
    m = n - 1
    
    nodes = create_graph(n, m)

    # Display generated nodes and connections for verification
    for node_name, node in nodes.items():
        print(f"Node {node_name} connections: {node.get_connected_vertices()}")

    start_node = input("Enter the starting node: ")
    end_node = input("Enter the destination node: ")

    if start_node in nodes and end_node in nodes:
        path, distance = dijkstra(nodes, start_node, end_node)
        print(f"Minimum path from {start_node} to {end_node}: {' -> '.join(path)}")
        print(f"Minimum distance: {distance}")
    else:
        print("Invalid start or end node.")

if __name__ == "__main__":
    main()
