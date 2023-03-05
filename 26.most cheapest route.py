mat= []
n,m = map(int,input().split())
for i in range(n):
    a=list(map(int,input().split()))[:m]
    mat.append(a)


def resh(grid):
    a = len(grid)
    b = len(grid[0])
    for i in range(1, b):
        grid[0][i] += grid[0][i-1]
    for i in range(1, a):
        grid[i][0] += grid[i-1][0]
    for i in range(1, a):
        for j in range(1, b):
            grid[i][j] += min(grid[i-1][j], grid[i][j-1])
    return grid[-1][-1]
print(resh(mat))
