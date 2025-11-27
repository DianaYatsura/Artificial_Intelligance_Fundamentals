
def search_word(grid, word):
    """
    Search for a word within a grid of letters.

    This function searches for the given word in the grid by checking all possible
    directions (horizontal, vertical, and diagonal) starting from each cell.

    Args:
    grid (list of list of str): A 2D grid of letters.
    word (str): The word to search for.

    Returns:
    bool: True if the word is found in the grid, False otherwise.
    """
    # Define possible directions (horizontal, vertical, diagonal)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
    rows = len(grid)
    cols = len(grid[0])
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] != word[0]:
                continue
            for dr, dc in directions:
                rr = r
                cc = c
                match = True
                for i in range(len(word)):
                    if rr < 0 or rr >= rows or cc < 0 or cc >= cols:
                        match = False
                        break
                    if grid[rr][cc] != word[i]:
                        match = False
                        break
                    rr += dr
                    cc += dc
                if match:
                    return True
    return False

def find_words(grid, words):
    """
    Find words within a grid of letters.

    This function searches for words in the given grid by calling the search_word function
    for each word to be found.

    Args:
    grid (list of list of str): A 2D grid of letters.
    words (list of str): A list of words to find in the grid.

    Returns:
    list of str: A list of words found in the grid.
    """
    result = []
    for word in words:
        if search_word(grid, word):
            result.append(word)
    return result

# Example usage:
grid = [['A', 'B', 'C', 'D'], ['E', 'F', 'G', 'O'], ['I', 'J', 'K', 'G'], ['M', 'N', 'H', 'P']]
word_list = ["HELLO", "WORLD", "HI", "FOOD", "DOG", "GOD"]
found_words = find_words(grid, word_list)
print("Found words:", found_words)
