s=input()
s = s.replace(' ','')


def resh(s):
    stack=[]
    for c in s:
        if c not in "+-*":
            stack.append(int(c))
        else:
            r,l = stack.pop(),stack.pop()
            if c =='+':
                stack.append(r+l)
            if c=='-':
                stack.append(l-r)
            if c=='*':
                stack.append(r*l)
    return stack.pop()
print(resh(s))
