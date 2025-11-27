from collections import deque


def is_valid(cell, grid):
    """
    Check if a cell is a valid open cell in the grid.

    Args:
    cell (tuple): The cell coordinates (row, col).
    grid (list of list of str): A 2D grid of characters.

    Returns:
    bool: True if the cell is a valid open cell, False otherwise.
    """
    x, y = cell
    rows = len(grid)
    cols = len(grid[0])
    if x >= rows or x < 0 or y >= cols or y < 0:
        return False
    if grid[x][y] == 'X':
        return False
    return True


def get_neighbors(cell, grid):
    """
    Get neighboring cells that are valid open cells in the grid.

    Args:
    cell (tuple): The cell coordinates (row, col).
    grid (list of list of str): A 2D grid of characters.

    Returns:
    list of tuple: List of neighboring cell coordinates [(row1, col1), (row2, col2), ...].
    """
    neighbors = []
    x, y = cell
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for dx, dy in directions:
        new_cell = (x + dx, y + dy)
        if is_valid(new_cell, grid):
            neighbors.append(new_cell)
    return neighbors


def find_shortest_path(grid, start, target):
    """
    Find the shortest path from the starting point to the target point on a grid.

    This function uses a breadth-first search (BFS) algorithm to find the shortest path
    from the starting point to the target point on the grid. The grid is represented as
    a 2D list of characters, where 'S' is the starting point, 'E' is the target point,
    'X' are blocked cells, and ' ' (space) are open cells.

    Args:
    grid (list of list of str): A 2D grid of characters.
    start (tuple): The starting point coordinates (row, col).
    target (tuple): The target point coordinates (row, col).

    Returns:
    list of tuple: The shortest path as a list of coordinate tuples [(row1, col1), (row2, col2), ...].
                   An empty list is returned if there is no valid path.
    """
    queue = deque([(start, [start])])
    visited = set([start])
    result = []
    while queue:
        (x, y), path = queue.popleft()
        if (x, y) == target:
            return path
        for neighbor in get_neighbors((x,y), grid):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))
    return result

# Example usage:
grid = [
    ['S', ' ', ' ', ' ', ' '],
    ['X', 'X', ' ', ' ', 'E'],
    [' ', ' ', 'X', ' ', ' '],
    ['X', 'X', ' ', 'X', ' '],
    [' ', ' ', ' ', ' ', ' ']
]

start_point = (0, 0)
end_point = (1, 4)

shortest_path = find_shortest_path(grid, start_point, end_point)
print("Shortest Path:", shortest_path)
