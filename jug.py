class State:
    def __init__(self, jug1, jug2):
        self.jug1 = jug1  # Amount of water in jug 1
        self.jug2 = jug2  # Amount of water in jug 2

    def __eq__(self, other):
        return self.jug1 == other.jug1 and self.jug2 == other.jug2

    def __hash__(self):
        return hash((self.jug1, self.jug2))

def dfs(current_state, visited, target, jug1_capacity, jug2_capacity, path):
    # Check if the current state is the target state
    if current_state == target:
        return True
    
    # Mark the current state as visited
    visited.add(current_state)
    
    # Explore all possible next states
    for next_state in get_neighbors(current_state, jug1_capacity, jug2_capacity):
        if next_state not in visited:  # If the next state hasn't been visited
            path.append(next_state)  # Add to the path
            if dfs(next_state, visited, target, jug1_capacity, jug2_capacity, path):
                return True  # If a solution is found, return True
            path.pop()  # Backtrack if no solution found
    return False  # No solution found from this path

def get_neighbors(current_state, jug1_capacity, jug2_capacity):
    neighbors = []
    
    # Fill jug1
    neighbors.append(State(jug1_capacity, current_state.jug2))
    # Fill jug2
    neighbors.append(State(current_state.jug1, jug2_capacity))
    # Empty jug1
    neighbors.append(State(0, current_state.jug2))
    # Empty jug2
    neighbors.append(State(current_state.jug1, 0))
    # Pour from jug1 to jug2
    pour_amount = min(current_state.jug1, jug2_capacity - current_state.jug2)
    neighbors.append(State(current_state.jug1 - pour_amount, current_state.jug2 + pour_amount))
    # Pour from jug2 to jug1
    pour_amount = min(jug1_capacity - current_state.jug1, current_state.jug2)
    neighbors.append(State(current_state.jug1 + pour_amount, current_state.jug2 - pour_amount))
    
    return neighbors

def main():
    # Define the capacities of the jugs
    jug1_capacity = 3
    jug2_capacity = 5
    
    # Initial state (both jugs are empty)
    start_state = State(0, 0)
    # Target state (we want 2 liters in jug 1 and 0 in jug 2)
    target_state = State(2, 0)
    
    visited = set()  # To keep track of visited states
    path = [start_state]  # To store the path taken
    
    # Start the DFS search
    if dfs(start_state, visited, target_state, jug1_capacity, jug2_capacity, path):
        print("Solution found:")
        for i, state in enumerate(path):
            print(f"Step {i}: Jug 1 = {state.jug1}, Jug 2 = {state.jug2}")
    else:
        print("No solution found.")

if __name__ == "__main__":
    main()