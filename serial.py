import math

def get_status(above, inline, below, j, w):
    living_neighbors = 0
    neighbors = []
    neighbors.append(above[(j-1)%w])
    neighbors.append(above[j])
    neighbors.append(above[(j+1)%w])
    neighbors.append(inline[(j+1)%w])
    neighbors.append(below[(j+1)%w])
    neighbors.append(below[(j)])
    neighbors.append(below[(j-1)%w])
    neighbors.append(inline[(j-1)%w])

    for i in range(len(neighbors)):
        living_neighbors += 1 if (neighbors[i] == 'O') else 0

    if (inline[j] == 'O'):
        status = 1
        if (living_neighbors < 2): return '.'
        for i in range(2,int(math.sqrt(living_neighbors))+1):
            if (living_neighbors%i) == 0:
                return '.'
        return 'O'

    return 'O' if living_neighbors % 2 != 0 else '.'

grid = []
with open("test2.in", "r") as f:
        grid = f.readlines()


l = len(grid)
w = len(grid[0])-1


new_grid = [ ['']*w for i in range(l)]
grid = [[char for char in grid[i]] for i in range(l)]

for k in range(101):
    for i in range(l):
        for j in range(w):
            new_grid[i][j] = get_status(grid[(i-1)%l][0:w], grid[i][0:w], grid[(i+1)%l][0:w],j, w)
    for i in range(l):
        for j in range(w):
            grid[i][j] = new_grid[i][j]

with open("test.out", "w") as txt_file:
    for line in new_grid:
        txt_file.write("".join(line) + "\n") 