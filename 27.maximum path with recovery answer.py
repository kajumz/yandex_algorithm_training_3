mat= []
n,m = map(int,input().split())
for i in range(n):
    a=list(map(int,input().split()))[:m]
    mat.append(a)
mat1= mat



def resh(grid):
    a = len(grid)
    b = len(grid[0])
    
    for i in range(1, b):
        grid[0][i] += grid[0][i-1]
    for i in range(1, a):
        grid[i][0] += grid[i-1][0]
    for i in range(1, a):
        for j in range(1, b):
            grid[i][j] += max(grid[i-1][j], grid[i][j-1])

    i=a-1
    j=b-1
    ans = []
    while i!=0 or j!=0:
        if (i>0 and j>0):
            if (grid[i-1][j]>grid[i][j-1]):
                ans.append('D')
                i-=1
            else:
                ans.append('R')
                j-=1
        elif(i>0):
            ans.append('D')
            i-=1
        elif(j>0):
            j-=1
            ans.append('R')
    print(grid[-1][-1])
    ans.reverse()
    for i in ans:
        print(i,end=' ')
resh(mat)
