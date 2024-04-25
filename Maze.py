def solveMaze(board: list, start: tuple, end: tuple):   
    rows,cols = len(board),len(board[0]) 
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    queue = [start]
    visited = [[False] * cols for _ in range(rows)]
    parent = [[None] * cols for _ in range(rows)]
    
    start_row, start_col = start
    visited[start_row][start_col] = True

    while queue:
        currCell = queue.pop(0)

        if currCell == end:
            path = []
            while currCell != start:
                path.append(currCell)
                currCell = parent[currCell[0]][currCell[1]]
            path.append(start)
            path.reverse()
            return path

        curr_row, curr_col = currCell
        
        for dr, dc in directions:
            neighbor_row, neighbor_col = curr_row + dr, curr_col + dc
            if (
                0 <= neighbor_row < rows
                and 0 <= neighbor_col < cols
                and board[neighbor_row][neighbor_col] != "X"
                and not visited[neighbor_row][neighbor_col]
            ):
                queue.append((neighbor_row, neighbor_col))
                visited[neighbor_row][neighbor_col] = True
                parent[neighbor_row][neighbor_col] = (curr_row, curr_col)

    return None  

maze = []

ls = str(input()).split(" ")
rows,cols = int(ls[0]), int(ls[1])

for i in range(rows):
    inpLines = str(input()).split(" ")
    for i in range(cols):
        if inpLines[i] == "0": inpLines[i] = " "
    maze.append(inpLines)
    
start,end = None,None

for i in range(rows):
    for j in range(cols):
        if maze[i][j] == "A":
            start = (i, j)
        elif maze[i][j] == "B":
            end = (i, j)
            
path = solveMaze(maze, start, end)

if path:
    for row, col in path:
        maze[row][col] = '*'
    maze[start[0]][start[1]] = 'A'
    maze[end[0]][end[1]] = 'B'
    for row in maze:
        result = ''
        for i in range(cols):
            if i == cols-1: result += row[i]
            else: result += row[i] + " "
        print(f"|{result}|")
else:
    print("No path found.")