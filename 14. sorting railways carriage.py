n = int(input())
l = list(map(int,input().split()))[:n]

def resh(array):
    stack=[]
    res = []
    n=len(array)
    for i in range(n):
        stack.append(array[i])
        while stack and stack[-1]-1==len(res):
            res.append(stack.pop())
    if not stack:
        print("YES")
    else:
        print("NO")

resh(l)
