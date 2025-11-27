
def dfs(maze, row, col, visited, solution_path):
    """
    Depth-First Search (DFS) algorithm to explore the maze and find a path from
    the current cell to the exit point 'E'.

    Args:
    maze (list): list of lists which represents the maze.
    row (int): The current row coordinate.
    col (int): The current column coordinate.
    visited (list of list of bool): A 2D grid representing visited cells in the maze.
    solution_path (list of tuple): A list of coordinate tuples representing the solution path.

    Returns:
    bool: True if a valid path is found from the current cell to 'E', False otherwise.
    """
    rows = len(maze)
    if rows > 0:
        cols = len(maze[0])
    else:
        cols = 0

    if row < 0 or row >= rows or col < 0 or col >= cols:
        return False

    if maze[row][col] == 'X' or visited[row][col]:
        print(f'Skipping: {row},{col}')
        return False

    visited[row][col] = True
    solution_path.append((row, col))

    print(f'Visiting: {row},{col} | Path: {solution_path}')

    if maze[row][col] == 'E':
        print("Exit found!")
        return True

    if (dfs(maze, row - 1, col, visited, solution_path) or
        dfs(maze, row + 1, col, visited, solution_path) or
        dfs(maze, row, col - 1, visited, solution_path) or
        dfs(maze, row, col + 1, visited, solution_path)):
        return True

    solution_path.pop()
    return False


def solve_maze(maze):
    """
    Solve a maze using Depth-First Search (DFS) algorithm.

    Args:
    maze (list of list of str): A 2D grid representing the maze.

    Returns:
    list of tuple: The solution path as a list of coordinate tuples [(row1, col1), (row2, col2), ...].
                   An empty list is returned if there is no valid path.
    """
    # Find the starting point
    # Initialize the visited array and solution_path list

    start_row = None
    start_col = None
    rows = len(maze)
    if rows > 0:
        cols = len(maze[0])
    else:
        cols = 0

    for r in range(rows):
        for c in range(cols):
            if maze[r][c] == 'S':
                start_row, start_col = r, c
                break

    visited = []
    solution_path = []

    for r in range(rows):
        row = []
        for c in range(cols):
            row.append(False)
        visited.append(row)

    path_found = dfs(maze, start_row, start_col, visited, solution_path)
    if path_found:
        return solution_path
    else:
        return []

# Example usage:
maze = [
    ['S', ' ', 'X', 'X', 'E'],
    ['X', ' ', ' ', 'X', ' '],
    ['X', 'X', ' ', ' ', ' '],
    [' ', 'X', 'X', 'X', ' '],
    [' ', ' ', ' ', ' ', ' ']
]

path = solve_maze(maze)
print("Solution Path:", path)
