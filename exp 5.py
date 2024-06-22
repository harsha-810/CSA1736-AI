from collections import deque

class State:
    def __init__(self, missionaries, cannibals, boat_position):
        self.missionaries = missionaries
        self.cannibals = cannibals
        self.boat_position = boat_position
        
    def is_valid(self):
        if self.missionaries < 0 or self.cannibals < 0 or self.missionaries > 3 or self.cannibals > 3:
            return False
        if self.missionaries > 0 and self.missionaries < self.cannibals:
            return False
        if 3 - self.missionaries > 0 and 3 - self.missionaries < 3 - self.cannibals:
            return False
        return True
    
    def is_goal(self):
        return self.missionaries == 0 and self.cannibals == 0 and self.boat_position == 'right'
    
    def __eq__(self, other):
        return self.missionaries == other.missionaries and self.cannibals == other.cannibals and self.boat_position == other.boat_position
    
    def __hash__(self):
        return hash((self.missionaries, self.cannibals, self.boat_position))
    
    def __str__(self):
        return f"Missionaries: {self.missionaries}, Cannibals: {self.cannibals}, Boat: {self.boat_position}"
    
def successors(state):
    children = []
    if state.boat_position == 'left':
        for i in range(1, 3):
            new_state = State(state.missionaries - i, state.cannibals - i, 'right')
            if new_state.is_valid():
                children.append(new_state)
        new_state = State(state.missionaries - 1, state.cannibals, 'right')
        if new_state.is_valid():
            children.append(new_state)
        new_state = State(state.missionaries, state.cannibals - 1, 'right')
        if new_state.is_valid():
            children.append(new_state)
        new_state = State(state.missionaries - 2, state.cannibals, 'right')
        if new_state.is_valid():
            children.append(new_state)
        new_state = State(state.missionaries, state.cannibals - 2, 'right')
        if new_state.is_valid():
            children.append(new_state)
    if state.boat_position == 'right':
        for i in range(1, 3):
            new_state = State(state.missionaries + i, state.cannibals + i, 'left')
            if new_state.is_valid():
                children.append(new_state)
        new_state = State(state.missionaries + 1, state.cannibals, 'left')
        if new_state.is_valid():
            children.append(new_state)
        new_state = State(state.missionaries, state.cannibals + 1, 'left')
        if new_state.is_valid():
            children.append(new_state)
        new_state = State(state.missionaries + 2, state.cannibals, 'left')
        if new_state.is_valid():
            children.append(new_state)
        new_state = State(state.missionaries, state.cannibals + 2, 'left')
        if new_state.is_valid():
            children.append(new_state)
    return children

def bfs(start):
    queue = deque([([], start)])
    visited = set()
    visited.add(start)
    
    while queue:
        path, state = queue.popleft()
        
        if state.is_goal():
            return path + [state]
        
        for child in successors(state):
            if child not in visited:
                visited.add(child)
                queue.append((path + [state], child))
    
    return None

def print_solution(solution):
    for i, state in enumerate(solution):
        print(f"Step {i}: {state}")
    print(f"Step {len(solution)}: Goal")

if __name__ == "__main__":
    initial_state = State(3, 3, 'left')
    solution = bfs(initial_state)
    
    if solution:
        print("Solution found:")
        print_solution(solution)
    else:
        print("No solution found.")
