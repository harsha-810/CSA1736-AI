from collections import deque

def bfs_graph(graph, start):
    visited = set()
    queue = deque([start])
    bfs_order = []

    while queue:
        vertex = queue.popleft()

        if vertex not in visited:
            visited.add(vertex)
            bfs_order.append(vertex)

            # Add all unvisited neighbors to the queue
            for neighbor in graph[vertex]:
                if neighbor not in visited:
                    queue.append(neighbor)

    return bfs_order

# Example usage:
if __name__ == "__main__":
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B', 'F'],
        'F': ['C', 'E']
    }
    start_node = 'A'
    bfs_result = bfs_graph(graph, start_node)
    print(f"BFS traversal starting from node {start_node}: {bfs_result}")
