from collections import deque
def bfs(start, goal, capacities):
    queue = deque([("", start)])  
    visited = set()
    visited.add(start)
    
    while queue:
        history, current_state = queue.popleft()
        
        if current_state == goal:
            return history
        for action, state in generate_states(current_state, capacities):
            if state not in visited:
                visited.add(state)
                queue.append((history + action, state))
    
    return "No solution found"

def generate_states(current_state, capacities):
    states = []
    jug1, jug2 = current_state

    states.append(("Fill jug1\n", (capacities[0], jug2)))
    states.append(("Fill jug2\n", (jug1, capacities[1])))
    states.append(("Empty jug1\n", (0, jug2)))
    states.append(("Empty jug2\n", (jug1, 0)))
    pour_amount = min(jug1, capacities[1] - jug2)
    states.append(("Pour jug1 to jug2\n", (jug1 - pour_amount, jug2 + pour_amount)))
    pour_amount = min(jug2, capacities[0] - jug1)
    states.append(("Pour jug2 to jug1\n", (jug1 + pour_amount, jug2 - pour_amount)))
    
    return states

if __name__ == "__main__":
    capacities = (4, 3)  
    start = (0, 0)  
    goal = 2        
    
    solution = bfs(start, (goal, 0), capacities)  
    
    if solution == "No solution found":
        print("No solution exists.")
    else:
        print("Solution steps:")
        print(solution)
