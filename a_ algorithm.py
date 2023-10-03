import heapq

class Node:
    def __init__(self, position, parent=None):
        self.position = position
        self.parent = parent
        self.g = 0  # Cost from start node to this node
        self.h = 0  # Heuristic (estimated cost from this node to goal)
        self.f = 0  # Total cost (f = g + h)

    def __lt__(self, other):
        # This is used for comparing nodes when pushing them into the priority queue (heap)
        return self.f < other.f

def astar(grid, start, goal):
    # Define possible movement directions (4 or 8 directions depending on the problem)
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    # Create the start and goal nodes
    start_node = Node(start)
    goal_node = Node(goal)

    # Initialize the open and closed sets
    open_set = []
    closed_set = set()

    # Add the start node to the open set
    heapq.heappush(open_set, start_node)

    while open_set:
        # Get the node with the lowest f-score from the open set
        current_node = heapq.heappop(open_set)

        # Check if we have reached the goal
        if current_node.position == goal_node.position:
            path = []
            while current_node is not None:
                path.append(current_node.position)
                current_node = current_node.parent
            return path[::-1]  # Reverse the path to get it from start to goal

        # Add the current node to the closed set
        closed_set.add(current_node.position)

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
                    neighbor_node = Node(neighbor_position, current_node)

                    # Calculate the g, h, and f scores
                    neighbor_node.g = current_node.g + 1  # Assuming a cost of 1 for each step
                    neighbor_node.h = abs(neighbor_node.position[0] - goal_node.position[0]) + \
                                      abs(neighbor_node.position[1] - goal_node.position[1])
                    neighbor_node.f = neighbor_node.g + neighbor_node.h

                    # Check if the neighbor is already in the closed set with a lower f-score
                    if neighbor_position in closed_set:
                        continue

                    # Check if the neighbor is already in the open set with a lower f-score
                    for open_node in open_set:
                        if neighbor_node.position == open_node.position and neighbor_node.g >= open_node.g:
                            break
                    else:
                        heapq.heappush(open_set, neighbor_node)

    # If no path is found, return an empty list
    return []

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
path = astar(grid, start, goal)
print(path)