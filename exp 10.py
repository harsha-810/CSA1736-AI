import heapq

class Node:
    def __init__(self, position, g, h):
        self.position = position
        self.g = g
        self.h = h  
        self.f = g + h

    def __lt__(self, other):
        return self.f < other.f

def astar(graph, start, goal, heuristic):
    open_set = []
    heapq.heappush(open_set, Node(start, 0, heuristic[start]))
    came_from = {}
    g_score = {node: float('inf') for node in graph}
    g_score[start] = 0

    while open_set:
        current = heapq.heappop(open_set).position

        if current == goal:
            return reconstruct_path(came_from, current)

        for neighbor, cost in graph[current].items():
            tentative_g_score = g_score[current] + cost
            if tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score = tentative_g_score + heuristic[neighbor]
                heapq.heappush(open_set, Node(neighbor, tentative_g_score, heuristic[neighbor]))

    return None  

def reconstruct_path(came_from, current):
    total_path = [current]
    while current in came_from:
        current = came_from[current]
        total_path.append(current)
    total_path.reverse()
    return total_path

graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

heuristic = {
    'A': 7,
    'B': 6,
    'C': 2,
    'D': 0 
}

start_node = 'A'
goal_node = 'D'
path = astar(graph, start_node, goal_node, heuristic)

print(f"The shortest path from {start_node} to {goal_node} is: {' -> '.join(path)}")
