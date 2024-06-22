from itertools import permutations
def calculate_route_distance(graph, route):
    total_distance = 0
    for i in range(len(route) - 1):
        total_distance += graph[route[i]][route[i + 1]]
    total_distance += graph[route[-1]][route[0]]  
    return total_distance

def travelling_salesman(graph, start):
 
    vertices = list(graph.keys())
    vertices.remove(start)
    
    all_permutations = permutations(vertices)
    
    min_distance = float('inf')
    best_route = None
    
    for perm in all_permutations:
        current_route = [start] + list(perm)
        current_distance = calculate_route_distance(graph, current_route)
        
        if current_distance < min_distance:
            min_distance = current_distance
            best_route = current_route
            
    return best_route, min_distance

graph = {
    'A': {'A': 0, 'B': 10, 'C': 15, 'D': 20},
    'B': {'A': 10, 'B': 0, 'C': 35, 'D': 25},
    'C': {'A': 15, 'B': 35, 'C': 0, 'D': 30},
    'D': {'A': 20, 'B': 25, 'C': 30, 'D': 0}
}

start_city = 'A'
best_route, min_distance = travelling_salesman(graph, start_city)

print(f"The shortest route is: {' -> '.join(best_route)} with a distance of {min_distance}")
