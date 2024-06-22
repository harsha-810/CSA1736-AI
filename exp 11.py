def is_valid(graph, color_map, node, color):
    for neighbor in graph[node]:
        if color_map.get(neighbor) == color:
            return False
    return True

def map_coloring(graph, colors, color_map, node):
    if node is None:
        return True

    for color in colors:
        if is_valid(graph, color_map, node, color):
            color_map[node] = color
            next_node = get_next_node(graph, color_map)
            if map_coloring(graph, colors, color_map, next_node):
                return True
            color_map[node] = None  

    return False

def get_next_node(graph, color_map):
    for node in graph:
        if node not in color_map or color_map[node] is None:
            return node
    return None

def main():
   
    graph = {
        'A': ['B', 'C', 'D'],
        'B': ['A', 'C', 'E'],
        'C': ['A', 'B', 'D', 'E'],
        'D': ['A', 'C', 'E'],
        'E': ['B', 'C', 'D']
    }

    colors = ['Red', 'Green', 'Blue']

    color_map = {node: None for node in graph}
    start_node = get_next_node(graph, color_map)

    if map_coloring(graph, colors, color_map, start_node):
        print("Solution found:")
        for node in color_map:
            print(f"{node}: {color_map[node]}")
    else:
        print("No solution found.")

if __name__ == "__main__":
    main()
