ls = str(input()).split(" ")
rows,cols = int(ls[0]),int(ls[1])

grid = []
for i in range(rows):
    grid.append(list(input()))

islands = 0

def markIslands(r: int, c: int):
    if r<0 or r>=rows or c<0 or c>=cols or grid[r][c] != "#": return
    
    grid[r][c] = "."
    
    markIslands(r-1,c)
    markIslands(r+1,c)
    markIslands(r,c+1)
    markIslands(r,c-1)
    
for i in range(rows):
    for j in range(cols):
        if grid[i][j] == "#":
            islands += 1
            markIslands(i,j)
                
print(islands)