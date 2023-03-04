s=input()

def right_seq(s):
    d = {'}':'{',
         ']':'[',
         ')':'('}
    stack=[]
    for c in s:
        if c in d:
            if len(stack)!=0:
                top_element = stack.pop()
            else:
                top_element='#'
            if d[c] !=top_element:
                return False

        else:
            stack.append(c)
    return not stack
print('yes' if right_seq(s) else 'no')
