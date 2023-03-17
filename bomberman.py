def bomber_man(n, grid):
    # Convert the grid to a 2D list of characters
    grid = [list(row) for row in grid]

    # Define a helper function to plant bombs
    def plant_bombs():
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '.':
                    grid[i][j] = 'O'

    # Define a helper function to detonate bombs
    def detonate_bombs():
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 'O':
                    # Detonate the bomb and its neighbors
                    grid[i][j] = '.'
                    if i > 0:
                        grid[i-1][j] = '.'
                    if i < len(grid)-1:
                        grid[i+1][j] = '.'
                    if j > 0:
                        grid[i][j-1] = '.'
                    if j < len(grid[0])-1:
                        grid[i][j+1] = '.'

    # Simulate the bomber man game for n seconds
    for t in range(n):
        if t == 0:
            continue
        elif t == 1:
            # Do nothing
            pass
        elif t % 2 == 0:
            # Plant bombs every even second
            plant_bombs()
        else:
            # Detonate bombs every odd second
            detonate_bombs()

    # Convert the 2D list of characters back to a list of strings
    return [''.join(row) for row in grid]
