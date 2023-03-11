k=int(input())
X = []
Y = []
for _ in range(k):
    a,b=map(int,input().split())
    X.append(a)
    Y.append(b)

def resh(x,y):
    print(min(x),min(y),max(x),max(y))
resh(X,Y)
