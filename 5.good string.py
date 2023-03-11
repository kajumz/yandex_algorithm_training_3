n=int(input())
a = []
for _ in range(n):
    a.append(int(input()))


def resh(arr):
    n=len(arr)-1
    cnt=0
    for i in range(n):
        cnt+=min(arr[i],arr[i+1])
    print(cnt)

resh(a)
