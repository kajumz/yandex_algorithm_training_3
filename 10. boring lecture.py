s = input()

def resh(st):
    dic = {}
    n=len(st)
    for i in range(n):
        dic[st[i]] = dic.get(st[i],0) + (i+1)*(n-i)
    sorted(dic.items())
    myKeys = list(dic.keys())
    myKeys.sort()
    sorted_dict = {i: dic[i] for i in myKeys}
    for k,v in sorted_dict.items():
        print(k+':',v)
resh(s)
