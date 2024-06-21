from queue import PriorityQueue

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

goal_state = (1, 2, 3, 4, 5, 6, 7, 8, 0)

def find_empty(puzzle):
    return puzzle.index(0)
def get_moves(puzzle):
    empty_index = find_empty(puzzle)
    empty_row = empty_index // 3
    empty_col = empty_index % 3
    possible_moves = []
    
    for direction in directions:
        new_row = empty_row + direction[0]
        new_col = empty_col + direction[1]
        
        if 0 <= new_row < 3 and 0 <= new_col < 3:
            new_index = new_row * 3 + new_col
            new_puzzle = list(puzzle)
            new_puzzle[empty_index], new_puzzle[new_index] = new_puzzle[new_index], new_puzzle[empty_index]
            possible_moves.append(tuple(new_puzzle))
            
    return possible_moves

def manhattan_distance(puzzle):
    distance = 0
    for i in range(3):
        for j in range(3):
            value = puzzle[i * 3 + j]
            if value != 0:
                target_row = (value - 1) // 3
                target_col = (value - 1) % 3
                distance += abs(target_row - i) + abs(target_col - j)
    return distance

def solve_8_puzzle(initial_state):
    pq = PriorityQueue()
    pq.put((0, initial_state))
    came_from = {initial_state: None}
    cost_so_far = {initial_state: 0}
    
    while not pq.empty():
        current_cost, current_state = pq.get()
        
        if current_state == goal_state:
            break
        
        for next_state in get_moves(current_state):
            new_cost = cost_so_far[current_state] + 1
            if next_state not in cost_so_far or new_cost < cost_so_far[next_state]:
                cost_so_far[next_state] = new_cost
                priority = new_cost + manhattan_distance(next_state)
                pq.put((priority, next_state))
                came_from[next_state] = current_state
    
    
    path = []
    state = goal_state
    while state != initial_state:
        path.append(state)
        state = came_from[state]
    path.append(initial_state)
    path.reverse()
    
    return path


if __name__ == "__main__":
    initial_state = (1, 2, 3, 4, 5, 6, 0, 7, 8)  
    solution_path = solve_8_puzzle(initial_state)
    
    print("Solution steps:")
    for i, state in enumerate(solution_path):
        print(f"Step {i}:")
        for j in range(3):
            print(state[j * 3:(j + 1) * 3])
        print()
