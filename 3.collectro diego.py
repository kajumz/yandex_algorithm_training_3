n=int(input())
l_d = list(map(int,input().split()))[:n]
k=int(input())
l_k = list(map(int,input().split()))[:k]

def bin_search(num, arr):
    l,r=0,len(arr)-1
    cnt=0
    while l<=r:
        m=int((l+r)/2)
        if arr[m]<num:
            cnt=m+1
            l=m+1
        else:
            r=m-1
    print(cnt)

def resh(l_d,l_k):
    a = sorted(set(l_d))
    for num in l_k:
        bin_search(num,a)
resh(l_d,l_k)
