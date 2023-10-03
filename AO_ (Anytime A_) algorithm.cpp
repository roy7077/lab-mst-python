import heapq

class Node:
    def __init__(self, position, parent=None, g=0, h=0):
        self.position = position
        self.parent = parent
        self.g = g  # Cost from start node to this node
        self.h = h  # Heuristic (estimated cost from this node to goal)
        self.f = g + h  # Total cost (f = g + h)

    def __lt__(self, other):
        # This is used for comparing nodes when pushing them into the priority queue (heap)
        return self.f < other.f

def ao_star(grid, start, goal, max_iterations=float('inf')):
    # Define possible movement directions (4 or 8 directions depending on the problem)
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    # Create the start and goal nodes
    start_node = Node(start)
    goal_node = Node(goal)

    # Initialize the open set and a list to store the best solution found so far
    open_set = []
    best_solution = None

    # Add the start node to the open set
    heapq.heappush(open_set, start_node)

    iterations = 0

    while open_set and iterations < max_iterations:
        # Get the node with the lowest f-score from the open set
        current_node = heapq.heappop(open_set)

        # Check if we have reached the goal
        if current_node.position == goal_node.position:
            best_solution = current_node
            max_iterations = iterations  # Update max_iterations to explore further
            continue

        for direction in directions:
            # Calculate the neighbor's position
            neighbor_position = (current_node.position[0] + direction[0], current_node.position[1] + direction[1])

            # Check if the neighbor is within the grid boundaries
            if (
                0 <= neighbor_position[0] < len(grid) and
                0 <= neighbor_position[1] < len(grid[0])
            ):
                # Check if the neighbor is a valid path (not blocked)
                if grid[neighbor_position[0]][neighbor_position[1]] == 0:
                    neighbor_g = current_node.g + 1  # Assuming a cost of 1 for each step
                    neighbor_h = abs(neighbor_position[0] - goal_node.position[0]) + \
                                 abs(neighbor_position[1] - goal_node.position[1])
                    neighbor_node = Node(neighbor_position, current_node, neighbor_g, neighbor_h)

                    # Check if the neighbor is already in the open set with a lower f-score
                    for open_node in open_set:
                        if neighbor_node.position == open_node.position and neighbor_node.g >= open_node.g:
                            break
                    else:
                        heapq.heappush(open_set, neighbor_node)

        iterations += 1

    # Trace back the best solution found so far
    path = []
    while best_solution is not None:
        path.append(best_solution.position)
        best_solution = best_solution.parent
    return path[::-1]  # Reverse the path to get it from start to goal

# Example usage:
grid = [
    [0, 0, 0, 0, 0],
    [0, 1, 1, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0]
]
start = (0, 0)
goal = (4, 4)
path = ao_star(grid, start, goal)
print(path)
